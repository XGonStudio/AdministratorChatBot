from django.http import Http404
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from django.views.generic import ListView, DetailView


# Send list of workers to outside API in JSON
class UserListAPI(generics.ListAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserSerializer


class UserListView(ListView):
    model = User
    template_name = 'user/user-list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_admin=False)


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user-detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_admin:
            raise Http404("This user is not available.")
        return obj
