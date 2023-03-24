from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_type=models.CharField(max_length=20)
    test_date = models.DateTimeField('date published')
    score=models.IntegerField(default=0)
    def __str__(self):
        return str(self.score)