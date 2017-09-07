# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .form import RegisterForm
 
# def index(request):
#     response = HttpResponse()
#     response.write("<h1>Welcome</h1>")
#     response.write("This is the gara app")
#     return response

# def register(request):
#     if request.method == 'POST':
#         response = HttpResponse()
#         response.write("<h1>Thanks for registering</h1><br>")
#         response.write("Your username: " + request.POST['username'] + "</br>")
#         response.write("Your email: " + request.POST['email'] + "</br>")
#         return response 
#     registerForm = RegisterForm()
#     return render(request, 'gara/register.html', {'form': registerForm})  


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from gara.models import Car
from gara.serializers import CarSerializer

@csrf_exempt
def car_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def car_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car.delete()
        return HttpResponse(status=204)