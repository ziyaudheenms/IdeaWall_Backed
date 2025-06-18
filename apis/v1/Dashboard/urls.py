from django.urls import path,include
from . import views
urlpatterns = [
    
   path("",views.VerifyTest),
   path("viewAllPosts/",views.ShowAllPosts),
   path("viewSinglePage/<int:pk>/",views.ShowSinglePage),
   path('Like/<int:pk>/' ,views.PostLikeUpdate ),
   path('comment/<int:pk>/' ,views.CreateComment ),
   path('comment/page/<int:pk>/' ,views.PageComment ),
   path('create/idea/' ,views.CreateIdeaPost ),

]
