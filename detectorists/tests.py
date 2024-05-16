from django.contrib.auth.models import User
from .models import Detectorist
from django.test import TestCase


class UserDetectoristCountTest(TestCase):
    # make sure that the user is always extended with the detectorist model
    def test_user_detectorist_count(self):
        user_count = User.objects.count()
        detectorist_count = Detectorist.objects.count()
        self.assertEqual(user_count, detectorist_count)
