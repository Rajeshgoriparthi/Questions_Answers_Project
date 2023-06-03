from django.db import models

# Create your models here.

from django.contrib.auth.models import User 


class Questions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.TextField()

    def __str__(self):
        return self.questions


class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answerd_by=models.TextField()


    def __str__(self):
        return self.answerd_by
