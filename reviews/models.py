from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """Model class for the reviews app"""
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To display the reviews by created_on in ascending order """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits review"""
        return reverse('testimonials')

    def __str__(self):
        return f"Testimonial: Review by {self.name}"
