from typing import List
import requests
from bs4 import BeautifulSoup
import json
from .property import Property
import traceback

def parse_property(url: str, properties: List[Property]) -> Property:
    """Scrapes data from given url (from https://www.immoweb.be) into a Property object and returns it"""

    # Request the url & turn response into soup
    try:
        r = requests.get(url,timeout=20)
        if r.status_code != 200:
            print(r.status_code)
        else:
            try:
                soup = BeautifulSoup(r.content, "html.parser")
                # Create a new property to assign values
                new_property = Property()

                # Turn relevant data from html tag script into JSON to extract data
                script = soup.find_all("script")[1]
                json_str = script.text.strip()
                json_str = json_str.split("[")[1].strip()
                json_str = json_str.split("]")[0].strip()
                json_str = json_str.replace("'", '"')
                json_data = json.loads(json_str)

                # Extract data and store into property object
                new_property.type = json_data["classified"]["type"]
                new_property.sub_type = json_data["classified"]["subtype"]
                new_property.price = json_data["classified"]["price"]
                new_property.type_of_sale = json_data["classified"]["transactionType"]
                new_property.amount_of_rooms = json_data["classified"]["bedroom"]["count"]

                if (json_data["classified"]["kitchen"]["type"] == "not installed") or (
                    json_data["classified"]["kitchen"]["type"] == "not installed"
                ):
                    new_property.has_full_kitchen = False
                else:
                    new_property.has_full_kitchen = True

                if json_data["classified"]["outdoor"]["garden"]["surface"] != "":
                    new_property.has_garden = True
                    new_property.garden_area = json_data["classified"]["outdoor"]["garden"][
                        "surface"
                    ]
                else:
                    new_property.has_garden = False
                    new_property.garden_area = 0

                if json_data["classified"]["outdoor"]["terrace"]["exists"] == "true":
                    new_property.has_terrace = True
                else:
                    new_property.has_terrace = False
                    new_property.terrace_area = 0

                if json_data["classified"]["land"]["surface"] != "":
                    new_property.surface_area_plot = int(
                        json_data["classified"]["land"]["surface"]
                    )

                if json_data["classified"]["wellnessEquipment"]["hasSwimmingPool"] == "true":
                    new_property.has_pool = True
                else:
                    new_property.has_pool = False

                new_property.building_state = json_data["classified"]["building"]["condition"]

                # Turn relevant data from html tag script into JSON to extract data
                script = soup.find_all("script")[6]
                json_str = script.text.strip()
                json_str = json_str.split(" = ")[1].strip()
                
                json_str = json_str.split('"property":')[1].strip()
                
                # One datapoint is in another list so we keep a seperate json string to use later
                json_furnished = json_str.split(',"publication"')[1].strip()
                json_furnished = '{"publication"' + json_furnished[:-1]

                json_str = json_str.split(',"publication"')[0].strip()
                json_data = json.loads(json_str)

                # Extract more data and store into property object
                new_property.locality = json_data["location"]["locality"]
                new_property.area = json_data["netHabitableSurface"]

                if json_data["fireplaceExists"] == True:
                    new_property.has_open_fire = True
                else:
                    new_property.has_open_fire = False

                try:
                    if json_data["building"]["facadeCount"] != None:
                        new_property.amount_of_facades = json_data["building"]["facadeCount"]
                except TypeError:
                    new_property.amount_of_facades = 0

                json_data = json.loads(json_furnished)

                if json_data["transaction"]["sale"]["isFurnished"]:
                    new_property.is_furnished = True
                else:
                    new_property.is_furnished = False

                # Calculate the surface area of the land if the plot & living area are known
                if new_property.surface_area_plot == None:
                    new_property.surface_area_plot = 0
                    new_property.surface_land = 0
                    

                # return property object with all stored data
                #return new_property
                properties.append(new_property)
            except Exception as e:
                pass
                #print(e)
                #print(traceback.format_exc())
    except Exception as e:
        print(e)


    