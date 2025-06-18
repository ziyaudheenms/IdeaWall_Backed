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
   path('search/filter/idea/' ,views.SearchFilter ),
   path('search/filter/Category/<int:pk>/' ,views.CategorySeachFilter ),
   path('search/filter/name/' ,views.SearchFilterByName ),

]
