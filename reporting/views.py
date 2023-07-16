from django.shortcuts import render,redirect
import pandas as pd
from django.contrib import messages

# Create your views here.
def crime(request):
	data=pd.read_csv("static/csv/goonda.csv")
	states=data['State/UT'].unique().tolist()
	print(type(data.columns))
	context={
	'states':states
	}
	if request.method=='POST':
		state=request.POST['state']
		district=request.POST['district']
		crime=request.POST['crime']
		date=request.POST['date']
		count=request.POST['count']
		path="static/csv/"+crime+".csv"
		data=pd.read_csv(path)
		if date in data.columns:
			row=data[(data['State/UT']==state) & (data['District']==district)].index
			data.loc[row,date]=count
			data.to_csv(path, encoding='utf-8', index=False)
			return redirect('admin-profile')
		else:
			data[date] = data.apply(lambda x: 0, axis=1)
			row=data[(data['State/UT']==state) & (data['District']==district)].index
			data.loc[row,date]=count
			data.to_csv(path, encoding='utf-8', index=False)

	return render(request,'reporting/report_crime.html',context)


