from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from dashboard.models import IdeaCard ,Likes ,IdeaPostComments ,Category
from .serializers import ViewAllPostsSeralizer , ViewSinglePageSerializer ,CommentSerializer

@api_view(['GET'])
def VerifyTest(request):
    return Response("Functioning of the django project verified")

@api_view(['GET'])
def ShowAllPosts(request):
    AllPosts = IdeaCard.objects.all()
    context={
        "request" : request
    }
    serialized_data = ViewAllPostsSeralizer(instance = AllPosts , many = True , context = context)
    responce_data ={
        "status_code":5000,
        "message": serialized_data.data,
        
    }
    return Response(responce_data)

@api_view(['GET'])
def ShowSinglePage(request,pk):
    if IdeaCard.objects.filter(pk =pk).exists():
        instance = IdeaCard.objects.get(pk = pk)
        context={
        "request" : request
        }
        serialized_data = ViewSinglePageSerializer(instance = instance , many = False,context = context)
        responce_data ={
        "status_code":5000,
        "message": serialized_data.data,
        
        }
        return Response(responce_data)
    else:
        responce_data ={
        "status_code":5001,
        "message": "oops! Page not found",
        
        }
        return Response(responce_data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PostLikeUpdate(request , pk):
    if IdeaCard.objects.filter(pk =pk).exists():
        post = IdeaCard.objects.get(pk =pk )
        if Likes.objects.filter(IdeaPost = post).exists():
            instance = Likes.objects.filter(IdeaPost = post)
            if instance.filter(user = request.user).exists():
                instance.get(user = request.user).delete()
                responce_data = {
                "status_code" : 5001,
                "data" : "disliked successfully"
                }
                return Response(responce_data)
            else:
                Likes.objects.create(
                    user = request.user,
                    IdeaPost = post
                )
                responce_data = {
                "status_code" : 5000,
                "data" : "liked successfully"
                }
                return Response(responce_data)
            responce_data = {
                "status_code" : 5000,
                "data" : "Successfully enterde"
            }
            return Response(responce_data)
        else:
            Likes.objects.create(
                user = request.user,
                IdeaPost = post
            )
            responce_data = {
                "status_code" : 5000,
                "data" : "Successfully liked"
            }
            return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 5001,
            "data" : "opps!page not found"
        }
        return Response(responce_data)
    
    

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateComment(request , pk):

    if IdeaCard.objects.filter(pk = pk).exists():
        text = request.data['text']
        IdeaPostInstance = IdeaCard.objects.get(pk = pk )
        IdeaPostComments.objects.create(
            user = request.user,
            text = text,
            IdeaPost = IdeaPostInstance
        )
        responce_data = {
            "stauts_code" : 5000,
            "data" : "Comment created successfully!"
        }
        return Response(responce_data)
    else:
        responce_data = {
            "stauts_code" : 5000,
            "data" : "idea doesn't exists!"
        }
        return Response(responce_data)
    
@api_view(['GET'])
def PageComment(request , pk):
    if IdeaCard.objects.filter(pk = pk).exists():
        Idea = IdeaCard.objects.get(pk = pk)
        instance = IdeaPostComments.objects.filter(IdeaPost = Idea) 
        context={
        'request' :request
        }
        serializedData = CommentSerializer(instance=instance , many=True ,context = context)
        responce_data = {
            'status_code' : 5000,
            'data' : serializedData.data
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code' : 5001,
            'data' : 'Idea not found'
        }
        return Response(responce_data)
   


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateIdeaPost(request):
    Title_of_Idea = request.data['Title']
    category = request.data['Category']
    Hero_Image = request.data['Hero_img']
    categories = request.data['Category']
    description = request.data['content']
    website_link = request.data['website_link']
    category_instance = Category.objects.get(id = category)
    
    IdeaCard.objects.create(
        Author = request.user,
        category = category_instance,
        Hero_Image = Hero_Image,
        Title_of_Idea = Title_of_Idea,
        description = description,
        website_link = website_link
    )
    responce_data = {
        'status_code' : 5000,
        "data" : "Idea created successfully"
    }
    return Response(responce_data)
   

