from rest_framework import generics, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import  UserSerializer , UserRegisterSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        user = serializer.save()
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        
        activation_path = reverse('accounts:activate', kwargs={'uidb64': uid, 'token': token})
        
        current_site = get_current_site(self.request)
        activation_link = f"http://{current_site.domain}{activation_path}"
        subject = 'Activate your Geometry Gym account'
        message = f'Hi {user.username},\n\nUse the link to activate your account:\n{activation_link}\n\nIf you did not request this, ignore.'
        send_mail(subject, message, None, [user.email], fail_silently=False)

class ActivateView(generics.GenericAPIView):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'detail': 'Account activated successfully'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Activation link is invalid'}, status=status.HTTP_400_BAD_REQUEST)

# Custom TokenObtainPair to block unverified users
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # self.user is the authenticated user
        if not self.user.is_active:
            raise serializers.ValidationError('Account is not activated. Please check your email.')
        # optionally add user data
        data['user'] = UserSerializer(self.user).data
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "Send POST request with username, email, password, role"})

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
