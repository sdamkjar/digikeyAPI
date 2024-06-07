import os
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

os.environ['DIGIKEY_CLIENT_ID'] = '6ASziOpZKrpFS3SISzW5nEhFhGrd34FK'
os.environ['DIGIKEY_CLIENT_SECRET'] = 'GMDWotuxLzSmF8Pu'
os.environ['DIGIKEY_CLIENT_SANDBOX'] = 'True'
os.environ['DIGIKEY_STORAGE_PATH'] = 'C:\\Users\\sdamk\\digikey'

# Query product number
dkpn = '296-6501-1-ND'
api_limit = {}

part = digikey.product_details(dkpn,api_limits=api_limit)

print (part)
print (api_limit)

for item in part.parameters:
    if item.parameter=='Operating Temperature':
        print(item.value)