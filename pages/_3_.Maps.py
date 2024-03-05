import streamlit as st
#from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
import requests
# pip install streamlit-folium? 

ad = st.text_input("Enter an address: ")
try :
    data = requests.get(f'https://geocode.xyz/{ad}?json=1')
except:
    latlon = []


icon_ = folium.Icon(color = "blue",
                    prefix = "fa",
                    icon = "rocket",
                    icon_color = "black"
                    )

latlon = [41.3977737, 2.1904561]
the_data = {"location": latlon, "tooltip": "Ironhack", "icon": icon_}
marker = folium.Marker(**the_data)

map_1 = folium.Map(location = latlon, zoom_start = 15)
marker.add_to(map_1)
folium_static(map_1)