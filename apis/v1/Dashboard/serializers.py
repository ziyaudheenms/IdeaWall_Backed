from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import IdeaCard ,Profile ,Likes ,IdeaPostComments ,Category


class ViewAllPostsSeralizer(serializers.ModelSerializer):
    Author = serializers.SerializerMethodField()
    no_of_likes = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = IdeaCard
        fields = "__all__"

    def get_Author(self,instance):
        return instance.Author.username
    def get_no_of_likes(self,instance):
        total_no_of_likes = Likes.objects.filter(IdeaPost = instance).count()
        return total_no_of_likes
    def get_category(self,instance):
       
        return instance.category.title

        
    


class ViewSinglePageSerializer(serializers.ModelSerializer):
    Author = serializers.SerializerMethodField()
    github_link = serializers.SerializerMethodField()
    designation_of_author = serializers.SerializerMethodField()
    no_of_likes = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = IdeaCard
        fields = "__all__"

    def get_Author(self,instance):
        return instance.Author.username
    def get_github_link(self,instance):
        User_profile = Profile.objects.get(user = instance.Author)
        link = User_profile.github_link
        return link
    def get_designation_of_author(self,instance):
        User_profile = Profile.objects.get(user = instance.Author)
        designation = User_profile.designation
        return designation
    def get_no_of_likes(self,instance):
        total_no_of_likes = Likes.objects.filter(IdeaPost = instance).count()
        return total_no_of_likes
    def get_category(self,instance):
       
        return instance.category.title


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = IdeaPostComments

    def get_user(self , instance):
        return instance.user.username
    

