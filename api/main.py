from unittest import result
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
import geopy
from geopy.geocoders import Nominatim
from tqdm import tqdm
import json 
import joblib
import time

app = FastAPI()
geolocator = Nominatim(user_agent="user_agent")


#latitude = -12.056869606837
#longitude = -76.957944072783
#geom = f'{latitude}, {longitude}'
#final_object = geolocator.reverse(geom)

#results = {
#    "address": final_object.address,
#    "point": final_object.point,
#    "data": final_object.raw
#}
#print(results)

@app.get("/")
async def root():
    return {"message": "Hello World!! Amigo, welcome to my API!!"}


@app.get("/addresses/lat={latitude}&lng={longitude}")
def get_address(latitude: float, longitude: float, response: Response):
    geom = f'{latitude}, {longitude}'
    final_object = None

    try:
        final_object = geolocator.reverse(geom)
        attempt = 1
    except:
        time.sleep(2)
        try:
            final_object = geolocator.reverse(geom)
            attempt = 2
        except:
            time.sleep(3)
            try:
                final_object = geolocator.reverse(geom)
                attempt = 3
            except:
                time.sleep(5)
                final_object = geolocator.reverse(geom)
                attempt = 4
            print(final_object)
    raw_info = final_object.raw

    
    print(final_object)
    results = {
        "data": dict(raw_info),
        "attempt":attempt 

    }
    return results




