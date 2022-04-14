from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    idNo = models.IntegerField(default=0)
    bio = models.TextField(max_length=254, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    emailaddress = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
    
class Neighbourhood(models.Model):
    title = models.CharField(max_length=150, verbose_name='Neighbourhood Title', null=True, blank=True)
    description = models.TextField(max_length=254, blank=True, verbose_name='Description')
    location = models.CharField(max_length=150, verbose_name='Neighbourhood Location', null=True, blank=True)
    neighbourhood_logo = CloudinaryField('neighbourhood_logo')
    
    neighbourhood_admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Neighbourhood Admin')
    health_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Health Department')
    police_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Police Department')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    
    def get_neighbourhoods(self):
        neighbourhoods = Neighbourhood.objects.all()
        return neighbourhoods
    def create_neigbourhood(self):
        self.save()
    def delete_neigbourhood(self):
        self.delete()
    def find_neigbourhood(self,neigborhood_id):
        neigbourhood = Neighbourhood.objects.filter(self = neigborhood_id)
        return neigbourhood
    def update_neighborhood(self, id, title, location, county, neighbourhood_logo):
        update = Neighbourhood.objects.filter(id = id).update(title = title , location = location, county = county, neighbourhood_logo = neighbourhood_logo)
        return update
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = 'Neighbourhoods'
    
    
