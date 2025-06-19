from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import IdeaCard ,Profile ,Likes ,IdeaPostComments ,Category
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.timesince import timesince
from django.utils.timezone import now
class ViewAllPostsSeralizer(serializers.ModelSerializer):
    Author = serializers.SerializerMethodField()
    no_of_likes = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    date_of_post = serializers.SerializerMethodField()
    designation_of_author = serializers.SerializerMethodField()
    avatar_of_Author = serializers.SerializerMethodField()
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
    def get_date_of_post(self,instance):
       
        if not instance.date_of_post:
            return None

        delta = timesince(instance.date_of_post, now())
        parts = delta.split(', ')
        if 'day' in parts[0]:
            return parts[0] + ' ago'
        return parts[0] + ' ago'
    def get_designation_of_author(self,instance): 
        return instance.team.team_number     
    def get_avatar_of_Author(self, instance):
        try:
            profile = Profile.objects.get(user=instance.Author)
            if profile.Avatar_Image:
                request = self.context.get('request')
                return request.build_absolute_uri(profile.Avatar_Image.url) if request else profile.Avatar_Image.url
            return None
        except Profile.DoesNotExist:
            return None 
        
        
    


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
    

