from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
import folium
import io
import csv
import pandas as pd
import sys
class maps_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.maps_tab = tab
        self.control_maps()

    def control_maps(self):
        layout = QtWidgets.QVBoxLayout(self.maps_tab)
        df = pd.read_csv('nationalparks.csv', usecols=['longitude', 'latitude', 'details', ])
        df.columns = ['Longitude', 'Latitude', 'Name']


        coordinate = (48.31521, -114.66929)
        map = folium.Map(
            title="Map",
            zoom_start=3,
            location=coordinate,
            control_scale=True
        )

        for i, row in df.iterrows():
            iframe = folium.IFrame('Name:' + str(row["Name"]))
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            folium.Marker(location=[row['Latitude'], row['Longitude']],
                          popup=popup, c=row['Name']).add_to(map)


        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QtWebEngineWidgets.QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        self.maps_tab.setLayout(layout)








