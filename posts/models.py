from django.db import models


class Post(models.Model):
  """Model definition for Post."""

  text = models.TextField()

  class Meta:
    """Meta definition for Post."""

    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    """Unicode representation of Post."""
    return self.text[:50]
