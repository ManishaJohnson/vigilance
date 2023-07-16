import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium import plugins

class PreprocessingData:

	def load_file(self,file_path):
		data=pd.read_csv(file_path)
		return data

	def getStates(self,data):
		states=data['State/UT'].unique().tolist()
		return states

	def transforming_data(self,data):
		data=pd.melt(data,id_vars=['State/UT','District','Latitude','Longitude'],var_name='Date',value_name='Count')
		return data

	def def_crime(self,data,crime):
		data["Crime"]=crime
		return data

	def getLastDate(self,data):
		data['Date']=pd.to_datetime(data['Date'])
		data.set_index('Date',inplace=True)
		date=data.index[-1]
		return date

	def analysis_data(self,data,date,state):
		total=data[(data.index==date)]
		total=total.loc[total["State/UT"] ==state]
		heatmap_df = total[['Latitude', 'Longitude','Count']].copy()
		analysis_df= total[['District','Count']].copy()
		return heatmap_df,analysis_df

	def getCoordinates(self,data,state):
		if (state=="SIKKIM"):
			lat=27.532972
			lon=88.512218

        #finding lat and long of state
		else:
			nom=Nominatim(user_agent="my_app")
			loc=nom.geocode(state)
			lat=loc.latitude
			lon=loc.longitude
		return lat,lon


	def initializing_proc(self,file_path,crime):
		data=self.load_file(file_path)
		states=self.getStates(data)
		data=self.transforming_data(data)
		data=self.def_crime(data,crime)
		date=self.getLastDate(data)

		context={
		'states':states
		}
		return data,states,context,date

	def display_ele(self,data,date,state,states):
		total,analysis_df=self.analysis_data(data,date,state)
		lat,lon=self.getCoordinates(data,state)

		analysis_df=analysis_df.sort_values('Count',ascending=False)
		analysis_df=analysis_df.head(15)
		analysis_df=analysis_df.to_html()

 
		map1= folium.Map(location=[lat,lon], zoom_start=6)
		plugins.HeatMap(total, min_opacity=0.4,
			blur = 18).add_to(folium.FeatureGroup(name='Heat Map').add_to(map1))
		folium.LayerControl().add_to(map1)

		map1=map1._repr_html_()
		msg="Districts in "+state+" with high crime rates"
		context={'states':states,'map':map1,'analysis':analysis_df,'msg':msg}
		return context


