from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .form import NameForm
 
def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is the gara app")
    return response

def register(request):
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1><br>")
        response.write("Your username: " + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response 
    registerForm = RegisterForm()
    return render(request, 'gara/register.html', {'form': registerForm})  


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()
    return render(request, 'gara/name.html', {'form' : form})

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.renderers import JSONRenderer
# # from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from gara.models import Car
from gara.serializers import CarSerializer, UserSerializer
from gara.permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


