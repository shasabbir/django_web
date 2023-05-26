from django.urls import re_path as url
from django.urls import path, include
# from .views import (
#     BookListApiView,
# )
from .Controller.BookController import BookListApiView

urlpatterns = [
    path('view', BookListApiView.as_view()),
]