import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np
import requests
from pycep_correios import get_address_from_cep, WebService
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import datetime
from datetime import datetime


class InfoDataHora:
    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)

    def executar_rest(self, cep):
        logger.debug(mensagens.INICIO_BUSCA)
        start_time = time.time()

        # response_local - Recebe o endereço a partir do CEP
        response_local = get_address_from_cep(cep['textoMensagem'][0], webservice=WebService.APICEP)

        adress = (response_local['logradouro'] + ' ' + response_local['cidade'] + ' ' + response_local['uf'])

        geolocaliza = Nominatim(user_agent="geoapi")
        coords = geolocaliza.geocode(adress)
        longitude = (coords.longitude)
        latitude = (coords.latitude) 


        tf = TimezoneFinder()
        timezone = tf.timezone_at(lng=longitude,lat=latitude)

        logger.warning(timezone)

        url_timezone = 'http://worldtimeapi.org/api/timezone/' + timezone
        data_hora_formatar = requests.get(url_timezone)

        data_hora = datetime.fromisoformat(data_hora_formatar.json()['datetime']).strftime("%d/%m/%Y, %H:%M:%S")

        return data_hora