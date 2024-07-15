from rest_framework import generics
from .serializers import UserSerializer
from .models import User


# Send list of workers to outside API in JSON
class UserListAPI(generics.ListAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserSerializer

    # TODO: обробити отримання даних про користувача чату (ім'я, номер телефону) в окрему модель для подальшої розсилки
    def post(self, request, *args, **kwargs):
        pass