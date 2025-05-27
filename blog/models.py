from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    @property
    def short_body(self):
        return self.body[:10]
    
    def get_absolute_url(self):
        # We don't use reverse_lazy here because this is a model method that will be called
        # after the URL patterns are already loaded, so regular reverse() is sufficient
        return reverse("post_detail", args=[str(self.id)])
    

     