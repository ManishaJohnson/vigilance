from django.shortcuts import render
import pandas as pd
from .preprocess import PreprocessingData



def gp_home(request):
    return render(request,'mapping/gp_home.html')

def burglary(request):
    return render(request,'mapping/burglary.html')


def districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/ndps.csv","ndps")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)
    return render(request,'mapping/districtMap.html',context)


def gambling_districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/gambling.csv","gambling")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)

    return render(request,'mapping/districtMap.html',context)


def arms_districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/arms.csv","arms")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)

    return render(request,'mapping/districtMap.html',context)

def mining_districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/mining.csv","mining")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)

    return render(request,'mapping/districtMap.html',context)

def traffic_districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/trafficking.csv","trafficking")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)

    return render(request,'mapping/districtMap.html',context)

def goonda_districtMap(request):
    pre_proc=PreprocessingData()
    data,states,context,date=pre_proc.initializing_proc("static/csv/goonda.csv","goonda")
    if request.method=='POST':
        state=request.POST['dropdown']
        context=pre_proc.display_ele(data,date,state,states)
        return render(request,'mapping/districtMap.html',context)

    return render(request,'mapping/districtMap.html',context)

