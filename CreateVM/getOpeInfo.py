#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys 
import time 
from time import gmtime, strftime

pp = pprint.PrettyPrinter(indent=4)

api = xmlrpc.client.ServerProxy('https://rpc.gandi.net/xmlrpc/')
apikey = '<API KEY>'



opeInfo = api.operation.info(apikey, 61890670)

if opeInfo['step'] == "DONE":
    print("VM create : " +  opeInfo['step'])
else: 
    print("VM create : In progress...")
