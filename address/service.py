import pandas as pd
from PropsAMC.settings import MEDIA_ROOT,GEO_CODING_URL,KEY
from xlrd import XLRDError
import os
import requests
class Service:
    """ Class to handle all the process related to Ge-Coding of adressess
    """
    def is_valid_file(self,file_loc):
        """ to validate if the excel file is correct or not """
        try:
            pd.read_excel(file_loc)
            return True
        except XLRDError as error:
            return False

    def process_geo_location(self,f):
        """ 
        function to process file sent using form, 
        and update its content by appending lat long labels right to it
        the first column will be Address, second will be latitude, third will be longitude
        """
        file_loc = os.path.join(MEDIA_ROOT,f)
        if not self.is_valid_file(file_loc):
            return False
        df = pd.read_excel(file_loc,header=None)
        addresses = df[0]
        latitudes = []
        longitudes = []
        for adr in addresses:
            lat,lng = self.get_lat_lang(adr)
            latitudes.append(lat)
            longitudes.append(lng)
        df[1] = latitudes
        df[2] = longitudes
        df.columns  = ['Address','latitude','longitude']
        df.to_excel(file_loc)
        return True

    def get_lat_lang(self,address):
        """ Actual function to handle lat-lang values         
        """
        params = {}
        params['address'] = address
        params['key'] = KEY
        data = requests.get(GEO_CODING_URL,params=params)
        if data.status_code == 200:
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lat']
            return lat,lng
        return None,None


service = Service()

