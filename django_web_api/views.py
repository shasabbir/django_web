from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class BookListApiView(APIView):
    # add permission to check if user is authenticated
#    authentication_classes = [SessionAuthentication, BasicAuthentication]
#    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Book items for given requested user
        '''
        Books = Book.objects.filter(user = request.user.id)
        serializer = BookSerializer(Books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Book with given Book data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': 1
        }
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)