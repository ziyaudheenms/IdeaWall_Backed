from django.contrib import admin
from .models import Profile , IdeaCard , Category ,Likes , IdeaPostComments ,Team
# Register your models here.
admin.site.register(Profile)
admin.site.register(IdeaCard)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(IdeaPostComments)
admin.site.register(Team)