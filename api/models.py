from django.db import models

STATE_CHOICE = ((
 ('Bihar','Bihar'),
 ('Jharkhand','Jharkhand'),
 ('West Bengal','West Bengal'),
))

class Profile(models.Model):
  name= models.CharField(max_length=100)
  email = models.EmailField()
  dob = models.DateField(auto_now=False, auto_now_add=False)
  state = models.CharField(choices=STATE_CHOICE, max_length=50)
  gender= models.CharField(max_length=100)
  location= models.CharField(max_length=100)
  pimage = models.ImageField(upload_to='pimages', blank=True)
  rdoc = models.FileField(upload_to='rdocs', blank=True)


# custom model manager
class AvailableBookManager(models.Manager):
    # overridding queryset
    def get_queryset(self):
        # Only return books that are marked as available
        return super().get_queryset().filter(is_available=True)

    # Adding extra method  to model manager
    def by_author(self, author_name):
        # Filter books by a specific author
        return self.get_queryset().filter(author=author_name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # New price field

    # Linking to the custom manager
    objects = models.Manager()  # Default manager
    available_books = AvailableBookManager()  # Custom manager

    def __str__(self):
        return self.title
