from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        # Create a user for the test
        User.objects.create_user(username='testUser', password='pass')

    def test_can_list_posts(self):
        # Test if the API can list posts
        adam = User.objects.get(username='testUser')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        # Test if a logged in user can create a post
        self.client.login(username='testUser', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # Test if the not logged in user can't create a post
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        # Create two users and tow posts for the tests
        testUser = User.objects.create_user(
            username='testUser',
            password='pass'
        )
        magnus = User.objects.create_user(username='magnus', password='pass')
        Post.objects.create(
            owner=testUser, title='a title', content='testUsers content'
        )
        Post.objects.create(
            owner=magnus, title='another title', content='magnus content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        # Test if the API can retrieve a post using a valid ID
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        # Test if the API can't retrieve a post using an invalid ID
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        # Test if a user can update their own post
        self.client.login(username='testUser', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        # Test if a user can't update another user's post
        self.client.login(username='testUser', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
