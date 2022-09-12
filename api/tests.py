from django.test import TestCase
from .models import Articles, Profile
# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(name="John", nicknaem = "johnny", avatar ="images", email="sarowiwa78@gmail.com", bio="i am a wrter and a poet", date_of_birth="1990-12-12")
        self.profile.save()
        self.assertEqual(self.profile.name, "John")
        return self.profile