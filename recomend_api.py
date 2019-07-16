# -*- coding: utf-8 -*-

import httplib2
import json
import geocode_api


cord = str(geocode_api.cord)

if cord == "O endereço não foi encontrado.":
    print(cord)
    exit()

food_type = str(input('Que tipo de local está buscando? '))

def recommendation_local(cord, food_type):

#Definição de váriaveis pra uso na URL

    foursq_cli_id = "IK2XKMCKTAT03HXBNB0KUX3ETFMKF2PKVUYL5I3FHR5CVTAY"
    foursq_cli_secret = "04Y2SVOT0D2DBMYSALDZE0AX0MATO3IZZYPXL41V1IGV0LLX"
    foursq_vers = "20190425"
    food_typeURL = food_type.replace(" ", "+")
    cordURL = cord.replace(" ", "+")

    #GET de informações gerais

    url = (f'https://api.foursquare.com/v2/venues/search?client_id={foursq_cli_id}&client_secret={foursq_cli_secret}&query={food_typeURL}&v={foursq_vers}&ll={cordURL}')
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)


    if 'venues' in result['response']:
        len_venues = len(result['response']['venues']) - 1
        i = 0
    else:
        print(result)
        print("Nenhum local encontrado.")
        exit()
    
    while i <= 4:

        # Selecionando informações gerais

        if(result['response']['venues'][i]):

            if 'id' in result['response']['venues'][i]:
                local_id = result['response']['venues'][i]['id']
            else:
                local_id = "Não informado."
            if 'categories' in result['response']['venues'][i] and 'name' in result['response']['venues'][i]['categories'][0]:
                local_type = result['response']['venues'][i]['categories'][0]['name']
            else:
                local_type = "Não informado."

            if 'name' in result['response']['venues'][i]:
                local_name = result['response']['venues'][i]['name']
            else:
                local_name = "Não informado."
            if 'location' in result['response']['venues'][i] and 'formattedAddress' in result['response']['venues'][i]['location']:
                local_address = result['response']['venues'][i]['location']['formattedAddress'][0]
            else:
                local_address = "Não informado."
        else:
            print("Estabelecimento não encontrado.")

        #GET de informações específicas

        url_details = ( f'https://api.foursquare.com/v2/venues/{local_id}?client_id={foursq_cli_id}&v={foursq_vers}&client_secret={foursq_cli_secret}')
        h_det = httplib2.Http()
        response_det, content_det = h_det.request(url_details, 'GET')
        result_det = json.loads(content_det)

        #Selecionando informações específicas

        if result_det['response'] and result_det['response']['venue']:

            if 'bestPhoto' in result_det['response']['venue']:
                prefix = result_det['response']['venue']['bestPhoto']['prefix']
                suffix = result_det['response']['venue']['bestPhoto']['suffix']
                local_photo = f"{prefix}500x500{suffix}"

            elif 'photo' in result_det['response']['venue']:
                prefix = result_det['response']['venue']['photo']['prefix']
                suffix = result_det['response']['venue']['photo']['suffix']
                local_photo = f"{prefix}500x500{suffix}"
            else: 
                local_photo = "Nenhuma foto encontrada"
        else:
            local_photo = "Nenhuma foto encontrada"


        local_info = f'{i+1}º Restaurante: \n\nTipo: {local_type}\nNome: {local_name}\nEndereço: {local_address}\nFoto: {local_photo}'
        barra = "\n------------------------------------------------------------\n"

        print (barra, local_info, barra)
        i = i + 1

    return(exit())
print (recommendation_local(cord, food_type))




