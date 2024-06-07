## @file digikeyAPI.py
#  @brief This file contains the digikeyAPI class which is used to interact with the Digikey API.
#  @author Your Name
#  @date Date
#
#  This file contains the digikeyAPI class. This class is used to set up the environment for the Digikey API,
#  retrieve data from the API, and handle the data returned from the API. It also includes functionality to
#  check if data already exists and to force an update of the data.
#
#  ## Usage
#  1. Install the digikey-api Python package. You can do this by running the following command in your terminal:
#     ```
#     py -m pip install digikey-api
#     ```
#  2. Instantiate the digikeyAPI class.
#  3. Use the `get` method of the digikeyAPI class to retrieve data from the Digikey API.
#     The `get` method takes three parameters:
#     - `dkpn`: The part number to retrieve data for.
#     - `parameter`: An optional parameter to specify a specific data field to retrieve.
#     - `force_update`: An optional boolean parameter. If set to True, the data will be retrieved from the API even if it already exists locally.
#
#  ## Example
#  ```python
#  from digikeyAPI import digikeyAPI
#
#  # Instantiate the digikeyAPI class
#  dk = digikeyAPI()
#
#  # Set the Digikey part number to retrieve data for
#  dkpn = '296-6501-1-ND'
#
#  # Retrieve data for a specific part number
#  data = dk.get(dkpn, 'Operating Temperature')
#  print(data)
#  ```

import os
import digikey
import csv
from colorama import init, Fore

class digikeyAPI:
    def __init__(self):

        color = init(autoreset=True)

        os.environ['DIGIKEY_CLIENT_ID'] = 'oxzSJA20fAR2CnbW1qeksGeAKBOSO7gr'
        os.environ['DIGIKEY_CLIENT_SECRET'] = '2G0nhB5i9u7Gb1ig'
        os.environ['DIGIKEY_CLIENT_SANDBOX'] = 'False'
        os.environ['DIGIKEY_STORAGE_PATH'] = 'C:\\Users\\sdamk\\digikey'

    def get(self,dkpn,parameter='',force_update=False):

        api_limit = {}
        returnValue = 0

        alreadyExists = self.find(dkpn,'data\\')
        if alreadyExists != 0 and force_update == False:
            print(Fore.GREEN + "Data for "+dkpn+" is already saved!")
            with open(alreadyExists, newline='', encoding="utf8") as csvfile:
                for row in csv.reader(csvfile):
                    if row[0] == parameter:
                        return row[2]
            return 0

        try:
            part = digikey.product_details(dkpn,api_limits=api_limit)
            print(Fore.YELLOW + str(api_limit))
            filestream = open('data\\'+dkpn,"w",encoding='utf8')
            for item in part.parameters:
                filestream.write(str(item.parameter))
                filestream.write(',')
                filestream.write(str(item.parameter_id))
                filestream.write(',')
                filestream.write(str(item.value))
                filestream.write(',')
                filestream.write(str(item.value_id))
                filestream.write('\n')
                if item.parameter==parameter:
                    returnValue = item.value
            filestream.close
        except:
            print(Fore.RED + "Error! Unable to connect to Digikey API!")

        return returnValue

    def find(self,name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
            return 0