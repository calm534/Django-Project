

# Create your views here.
from django.shortcuts import render
from .models import MyModel

def create_model_instance(request):
    MyModel.objects.create(name="Test Model")
    print("Instance created.")
    return render(request, 'index.html')

from django.shortcuts import render
from .models import MyModel
import threading

def create_model_instance(request):
    print(f"View thread: {threading.current_thread().name}")
    MyModel.objects.create(name="Test Model")
    return render(request, 'index.html')

from django.shortcuts import render
from django.db import transaction
from .models import MyModel

def create_model_instance(request):
    with transaction.atomic():
        MyModel.objects.create(name="Test Model")
        print("Model created within transaction.")
    return render(request, 'index.html')
