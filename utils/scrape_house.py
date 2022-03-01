import pprint
import requests
from bs4 import BeautifulSoup
import bs4
import json
from property import Property

url = "https://www.immoweb.be/en/classified/villa/for-sale/de-haan/8420/9779450?searchId=621dde082ca76"
url2 = "https://www.immoweb.be/en/classified/apartment/for-sale/liege/4000/9778981?searchId=621dde458e4f5"
r = requests.get(url)

def script_to_json(script: bs4.element.Tag) -> json:
        json_str = script.text.strip()
        json_str = json_str.split('[')[1].strip()
        json_str = json_str.split(']')[0].strip()
        json_str = json_str.replace("'", '"')

        json_object = json.loads(json_str)
        return json_object



if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    
    with open("a.html","wb") as file:
        file.write(r.content)
    

    new_property = Property()

    script = (soup.find_all("script")[1])   
    json_data = script_to_json(script)

    new_property.type = json_data["classified"]["type"]
    new_property.sub_type = json_data["classified"]["subtype"]
    new_property.price = int(json_data["classified"]["price"])
    new_property.type_of_sale = json_data["classified"]["transactionType"]
    new_property.amount_of_rooms = int(json_data["classified"]["bedroom"]["count"])
    if ((json_data["classified"]["kitchen"]["type"] == "not installed") or (json_data["classified"]["kitchen"]["type"] == "not installed")):
        new_property.has_full_kitchen = False
    else:
        new_property.has_full_kitchen = True
    
    
    if (json_data["classified"]["outdoor"]["garden"]["surface"] != ""):
        new_property.has_garden = True
        new_property.garden_area = json_data["classified"]["outdoor"]["garden"]["surface"]
    else:
        new_property.has_garden = False
        new_property.garden_area = 0
    
    if(json_data["classified"]["outdoor"]["terrace"]["exists"] == "true"):
        new_property.has_terrace = True
    else:
        new_property.has_terrace = False

    if(json_data["classified"]["land"]["surface"] != ""):
        new_property.surface_area_plot = int(json_data["classified"]["land"]["surface"])
    
    if(json_data["classified"]["wellnessEquipment"]["hasSwimmingPool"] == "true"):
        new_property.has_pool = True
    
     

    script = (soup.find_all("script")[6])
    json_str = script.text.strip()
    json_str = json_str.split(' = ')[1].strip()
    
    json_str = json_str.split('"property":')[1].strip()
    json_str = json_str.split(',"publication"')[0].strip()
    
    json_object = json.loads(json_str)

    print(json_object['location']['locality'])

    new_property.area = 0  
    if(new_property.surface_area_plot != None):    
        new_property.surface_land = new_property.surface_area_plot - new_property.area


    



        