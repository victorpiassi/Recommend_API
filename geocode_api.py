import httplib2
import json

address = str(input("Informe o endereço: "))

def geocode_location(address): 
    opencg_api_key = "172618d2d8e34bb591010fdc091c6739"
    addressURL = address.replace(" ", "+") 
    url = (f'https://api.opencagedata.com/geocode/v1/json?q={addressURL}&key={opencg_api_key}')
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    if result['results']:
        lat = result['results'][0]['geometry']['lat']
        lng = result['results'][0]['geometry']['lng']
        cord = (f"{lat}, {lng}")
    else:  
        cord = "O endereço não foi encontrado."
    return cord

cord = geocode_location(address)
