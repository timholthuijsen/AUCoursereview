from django.db import models
from django.utils import timezone
from django.db import models
from django.db import models
from django.contrib.auth.models import User

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
'''
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    catalogue_nr = models.CharField(max_length=10)
    #averageRating = models.FloatField(default=0)
    def __str__(self):
        return self.course_name

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    #This is the forms approach
    comment = models.CharField(max_length=500)
    rating = models.FloatField(default=0)
    def __str__(self):
        return self.user.username

        
# Create your models here.
