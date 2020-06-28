from django.test import TestCase
from wcbn_auth.models import User

class WCBNAuthTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email="homer@springfield.com")

    def test_user_post_save(self):
        self.assertTrue(self.user.has_perm('change_user', self.user)) # user can edit self
        self.assertFalse(self.user.has_perm('delete_user', self.user)) # user can not delete self
