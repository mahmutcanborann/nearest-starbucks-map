import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

lokasyon=Nominatim(user_agent='geoapi_exercise')
konumunuz=st.text_input("Konumuzu giriniz")
konum=lokasyon.geocode(konumunuz)
if konum!=None:
    lat=konum.latitude
    lon=konum.longitude

    df=pd.read_json('https://raw.githubusercontent.com/mmcloughlin/starbucks/refs/heads/master/locations.json')

    df['lat']=lat
    df['lon']=lon

    mesafe=((df['lat']-df['latitude'])**2 + (df['lon']-df['longitude'])**2)**0.5

    df['mesafe']=mesafe

    df=df.sort_values(by="mesafe")

    df=df.head(5)
    st.map(df[['latitude','longitude']])
else:
    st.error("Böyle bir konum bulunamadı")

