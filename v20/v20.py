from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import json

accountID = "101-001-12974810-001"
access_token = '4ee72f8854218b0e532c9f5379c53034-a39bfbf0e25e946cb82059e920fa51e4'

api = API(access_token=access_token, environment="practice")

params = { "instruments": "EUR_USD,EUR_JPY,USD_JPY" }
import oandapyV20.endpoints.accounts as accounts
r = accounts.AccountInstruments(accountID=accountID, params=params)
req = api.request(r)
print(json.dumps(req,indent=2))