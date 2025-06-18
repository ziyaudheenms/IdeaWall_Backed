from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team_lead = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Team_Lead")
    designation = models.TextField(default="I am an user")
    no_of_ideas = models.IntegerField(default=0)
    no_of_likes = models.IntegerField(default=0)
    github_link = models.TextField(default="www.github.com")

    def __str__(self) :

        return self.user.username


class Category(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
        return self.title


class IdeaCard(models.Model):
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Hero_Image = models.ImageField(upload_to='images/')
    Title_of_Idea = models.TextField()
    description = models.TextField()
    website_link = models.TextField()
    category = models.ForeignKey(Category ,on_delete=models.CASCADE ,related_name="category" )
    date_of_post = models.DateField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)
    github_link = models.TextField(default="example.com")
    designation_of_author = models.TextField(default="member")

    def __str__(self) :

        return self.Title_of_Idea

class Likes(models.Model):
    IdeaPost = models.ForeignKey(IdeaCard , on_delete=models.CASCADE,related_name="name_of_the_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class IdeaPostComments(models.Model):
    IdeaPost = models.ForeignKey(IdeaCard , on_delete=models.CASCADE,related_name="idea")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


