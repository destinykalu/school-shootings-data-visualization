import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df =pd.read_csv('shootings.csv')
#df=df.drop(['City', 'State', 'AreaType', 'School', 'Dupe', 'Source', 'Desc'])
#df =df.drop(['Unnamed: 10','Unnamed: 11'], axis =1)
#f.to_csv('shootings.csv',index =False)
df['Date']=pd.to_datetime(df['Date'], format ='%m/%d/%Y',errors='coerce')
df['Year']=df['Date'].dt.year

df['five_years']=(df['Year']//5)*5
df_grouped=df.groupby('five_years',as_index=False)[['Fatalities','Wounded']].sum()
# Create readable interval labels

colors=['pink','lightpink','deeppink','salmon','tomato','crimson','firebrick','darkred']
plt.bar(df_grouped['five_years'].astype(str),df_grouped['Fatalities']+df_grouped['Wounded'],color=colors, edgecolor='gray',linewidth=1.5)

xa=plt.xlabel('5 Year Intervals')
xa.set_fontstyle('italic')
ya=plt.ylabel('Total Victims')
ya.set_fontstyle('italic')
title= plt.title('Number of Victims due to Gun Violence in Schools')
title.set_fontweight('bold')
plt.show()