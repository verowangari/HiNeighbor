
from django.test import TestCase
from .models import Business,NeighbourHood, Profile, Post

# Set up method 
# Set up method 
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='Veronica')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

#Testing Save Method

    

    

# Set up method        


class PostTestClass(TestCase):
    def setUp(self):
        self.post=Post(post='new post')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post)) 


   
        
             



#  Set up method   

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood=NeighbourHood(name='Veronica')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))  

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business=Business(email='test@mail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))           





        





        


