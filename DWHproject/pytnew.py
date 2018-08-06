import csv
import pandas as pd
import io
import numpy as np

##inputfile = csv.reader(open('census.csv','r'))
cols=['Year','Geocode','Geolevel','Geoname','Gnr','Gnrlf',
'Dataflag','Altgeo','Info','Infoid','Notes','Total','Male','Female']
dt_cols={'Year':int,'Geocode':int,'Geolevel':float,'Geoname':str,'Gnr':float,'Gnrlf':float,
'Dataflag':float,'Altgeo':float,'Info':str,'Infoid':int,'Notes':float,'Total':float,'Male':float,'Female':float}
##df=pd.DataFrame(np.empty(0,dtype=dt_cols))
try:
    df = pd.read_csv('newfile.csv', skiprows=1, index_col=False, names=cols, low_memory=False)## dtype=dt_cols)
except CParserError:
    print("Something wrong the file")

##df = pd.read_csv('newfile.csv',skiprows=1, index_col=False, names=cols, low_memory=False)## dtype=dt_cols)
##time.sleep(3)
print("imported data--------")
print(df.head(3))
print("number of rows before filter: ",df.shape[0])
print("filtering nova scotia cities/towns------")
filter_list = ['Amherst','Antigonish','Bedford','Bridgewater','Digby','Glace Bay','Inverness','New Waterford','Halifax','Kentville',
'Middleton','New Glasgow','Sydney Mines','Shelburne','Cape Breton - Sydney','Truro',
'Wolfville','Yarmouth','Chester','Berwick','Hantsport','Lunenburg','Springhill',
'Lake Echo','Hayes Subdivision','Brookside','Still Water Lake','Enfield - Lantz','English Corner', 'Port Williams',
'Howie Centre','Pictou']
#df[df.Geoname.isin(filter_list)]
df1=df.loc[df['Geoname'].isin(filter_list)]
print("number of rows after filter:  ",df1.shape[0])
##df.columns = ['code', 'geo_name', 'lang', 'lang_id', 'total', 'men', 'women']
##df.apply(lambda x: pd.lib, infer_dtype(x.values))

#for i, row in df.iterrows():
   # print(row)
 #   d=df['Info'].replace(['-',','],['',' '],regex = True)
  #  d1=df['Geoname'].replace(['Amherst'],['Amherst'],regex = True)

#d2=pd.concat([d,d1],axis=1)
print("dropped data------")
df2=df1.drop(["Year", "Geolevel","Gnr","Gnrlf","Dataflag","Altgeo","Notes","Male","Female"], axis=1)
df2.to_csv('dropdata.csv',index=False,encoding='utf-8')
print(df2.head(3))
print("infoid 34 to 38  data(distribution of pop)----")
df3 = df2[df1.Infoid > 36]
#df2=df1[(df1['Infoid']<100) and (df1['Infoid']>660)]
print("head data--------------")
print(df3.head(3))
print("tail data--------------")
print(df3.tail(3))
print("infoid les than 39-----")
df4=df3[df3.Infoid < 39]
print("head data-------------")
print(df4.head(3))
print("tail data-------------")
print(df4.tail(3))##d4
print("infoid 8 to 24  data(avg age groups)----")
df5 = df2[df1.Infoid > 7]
#df2=df1[(df1['Infoid']<100) and (df1['Infoid']>660)]
print("head data--------------")
print(df5.head(3))
print("tail data--------------")
print(df5.tail(3))
print("infoid les than 39-----")
df6=df5[df5.Infoid < 25]
print("head data-------------")
print(df6.head(3))
print("tail data-------------")
print(df6.tail(3))##df6
print("infoid 711 to 723  data(after tax income)----")
df7 = df2[df1.Infoid > 710]
#df2=df1[(df1['Infoid']<100) and (df1['Infoid']>660)]
print("head data--------------")
print(df7.head(3))
print("tail data--------------")
print(df7.tail(3))
print("infoid les than 39-----")
df8=df7[df7.Infoid < 724]
print("head data-------------")
print(df8.head(3))
print("tail data-------------")
print(df8.tail(3)) ##df8
print("infoid 847 to 851  data(low income status)----")
df9 = df2[df1.Infoid > 846]
#df2=df1[(df1['Infoid']<100) and (df1['Infoid']>660)]
print("head data--------------")
print(df9.head(3))
print("tail data--------------")
print(df9.tail(3))
print("infoid les than 852-----")
df10=df9[df9.Infoid < 852]
print("head data-------------")
print(df10.head(3))
print("tail data-------------")
print(df10.tail(3)) ##df10
print("infoid 112-119 data(languages)----")
df11=df2[df1.Infoid > 111]
print("head data----------------")
print(df11.head(3))
print("tail data-----------------")
print(df11.tail(3))
df12=df11[df11.Infoid <120]
print("head data------------")
print(df12.head(3))
print("tail data------------")
print(df12.tail(3)) ##df12
print("infoid 376-380 data(languages)----")
df13=df2[df1.Infoid > 374]
print("head data----------------")
print(df13.head(3))
print("tail data-----------------")
print(df13.tail(3))
df14=df13[df13.Infoid <381]
print("head data------------")
print(df14.head(3))
print("tail data------------")
print(df14.tail(3)) ##df14
print("infoid 121-375 data(languages)----")
df15=df2[df1.Infoid > 120]
print("head data----------------")
print(df15.head(3))
print("tail data-----------------")
print(df15.tail(3))
df16=df15[df15.Infoid <376]
print("head data------------")
print(df16.head(3))
print("tail data------------")
print(df16.tail(3)) 
df17=df16.loc[df16['Info'].str.contains('languages', regex=False, case=False, na=False)] ##df17
#for i, row in df3.iterrows():
#    df4=df3['Info'].replace(['%'],['percentage'],regex = True)

##df7=pd.concat([df4,df6],axis=0)
df18=df4.append(df6)
df19=df18.append(df8)
df20=df19.append(df10)
df20.to_csv('withoutlang.csv',index=False,encoding='utf-8')
df21=df14.append(df12)
df22=df21.append(df17)
df22.to_csv('lang.csv',index=False,encoding='utf-8')
print("writing to csv-----")
#print(df23.head(3))
#df23.to_csv('censusnewnew.csv',index=False,encoding='utf-8')
#df2.replace('...','', regex=True)
#df2.fillna(0)
print("reshaping----------")
##df16['Info_Infoid']=df16['Info']+'_'+df16['Infoid'].astype(str)
df20.loc[:,'Info_Infoid']=df20.Infoid.map(str) + "_" + df20.Info
df22.loc[:,'Info_Infoid']=df22.Infoid.map(str) + "_" + df22.Info
#df16.to_csv('conact.csv',index=False,encoding='utf-8')
df23=df20.drop(["Infoid"],axis=1)
df26=df22.drop(["Infoid"],axis=1)
df24=df23.drop(["Info"],axis=1)
df27=df26.drop(["Info"],axis=1)
df25=df24.pivot_table(['Total'],['Geocode','Geoname'],['Info_Infoid'], aggfunc='first')
df28=df27.pivot_table(['Total'],['Geocode','Geoname'],['Info_Infoid'], aggfunc='first')
##df19=df18.drop(["Infoid"],axis=1)
print("writing to pivoted csv----")
print(df25.head(3))
df25.to_csv('pivot.csv',index=True,encoding='utf-8')
df28.to_csv('langpivot.csv',index=True,encoding='utf-8')
