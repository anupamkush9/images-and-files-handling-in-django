from rest_framework.response import Response
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class AvailableBooksAPIView(APIView):
    def get(self, request):
        author_name = request.query_params.get('author', None)
        if author_name:
            book_custom_model_manager_objs = Book.available_books.by_author(author_name)
            book_default_model_manager_objs = Book.objects.filter(author = author_name)
        else:
            book_custom_model_manager_objs = Book.available_books.all()  # Fetch all available books
            book_default_model_manager_objs = Book.objects.all()  # Fetch all books

        # Serialize the queryset
        custom_model_manager_serializer = BookSerializer(book_custom_model_manager_objs, many=True)
        default_model_manager_serializer = BookSerializer(book_default_model_manager_objs, many=True)
        
        return Response({"custom_model_manager":custom_model_manager_serializer.data, 
                         "default_model_manager_serializer":default_model_manager_serializer.data}, status=status.HTTP_200_OK)


class ProfileView(APIView):
  def post(self, request, format=None):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Resume Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
  
  def get(self, request, format=None):
    candidates = Profile.objects.all()
    serializer = ProfileSerializer(candidates, many=True)
    return Response({'status':'success', 'candidates':serializer.data}, status=status.HTTP_200_OK)

