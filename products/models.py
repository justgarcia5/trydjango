from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(blank=False, null=False)
  price = models.DecimalField(decimal_places=2, max_digits=1000)
  summary = models.TextField(blank=False, null=False)
  features = models.BooleanField(default=True)
  # email = models.EmailField()

  def get_absolute_url(self):
    return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}"
