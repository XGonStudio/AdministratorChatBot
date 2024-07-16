from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from django.views.generic import ListView, DetailView


# Send list of workers to outside API in JSON
class UserListAPI(generics.ListAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserSerializer

    # TODO: обробити отримання даних про користувача чату (ім'я, номер телефону) в окрему модель для подальшої розсилки
    def post(self, request, *args, **kwargs):
        pass


class UserListView(ListView):
    model = User
    template_name = 'user/user-list.html'
    context_object_name = 'user'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user-detail.html'
    context_object_name = 'user'
