from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os
class fooDonationAppConfigTest(TestCase):
    def test_secret_key_strength(self):
        # self.assertTrue(1==1)
        SECRET_KEY =os.environ.get("SECRET_KEY")
        # self.assertNotEqual(SECRET_KEY, "abc123")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak Password - {e}"
            self.fail(msg)



# There is a philosopy called test driven development which is tdd 