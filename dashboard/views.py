from django.shortcuts import render
import pandas as pd

# Create your views here.
def create_dashboard(request):
    return render(request,'dashboard/dashboard.html')
