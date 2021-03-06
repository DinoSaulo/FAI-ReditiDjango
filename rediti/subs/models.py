from django.db import models
from common.models import IndexedTimeStampedModel

class Thread(IndexedTimeStampedModel):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('users.User', related_name="threads", on_delete=models.CASCADE)
    subrediti = models.ForeignKey('Subrediti', related_name="threads", on_delete=models.CASCADE)
    vote_count = models.IntergerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self)
        return self.title

class Subrediti(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creator = models.ForeignKey('users.User', related_name="threads", on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self)
        return self.title

class Post(IndexedTimeStampedModel):
    content = models.TextField()
    author = models.ForeignKey('users.User', related_name="posts", on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return ("{} - {} - {}").format(self.id, self.thread, self.author)

class Subscription(models.Model):
    subrediti = models.ForeignKey('Subrediti', on_delete=models.CASCADE)
    users = models.ForeignKey('users.User', on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    class Meta:
        unique_together = [('user','sub')]

    class __str__(self):
        return('{} - {}').format(self.subrediti, self)