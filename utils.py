# © 2025 Zubair Abdullah Sadiq. All rights reserved.

import requests

def get_coordinates(location):
    api_key = "58c4999f8d87491bb1af565d800e929b"
    url = f"https://api.opencagedata.com/geocode/v1/json?q=Frauenplan+1%2C+99423+Weimar%2C+Germany&key=58c4999f8d87491bb1af565d800e929b"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        lat = data['results'][0]['geometry']['lat']
        lng = data['results'][0]['geometry']['lng']
        return lat, lng
    return None, None

def get_ngo_news():
    api_key = "bbf755c504fd4a7ca21396ced9d710f4"
    url = f"https://newsapi.org/v2/everything?q=NGO&apiKey={api_key}"
    response = requests.get(url)
    return response.json()
