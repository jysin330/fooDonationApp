from django.test import TestCase
import os
class fooDonationAppConfigTest(TestCase):
    def test_secret_key_strength(self):
        # self.assertTrue(1==1)
        SECRET_KEY =os.environ.get("SECRET_KEY")
        self.assertNotEqual(SECRET_KEY, "abc123")