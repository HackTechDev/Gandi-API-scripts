#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys
import time 
from time import gmtime, strftime

pp = pprint.PrettyPrinter(indent=4)

# API production connection
api = xmlrpc.client.ServerProxy('https://rpc.gandi.net/xmlrpc/')

# API key
apikey = '<API KEY>'


# vm specifity
vm_spec = {'datacenter_id' : 1, 
           'cores' : 1, 
           'memory' : 1024,
           'hostname' : 'test01', 
           'login' : 'administrateur', 
           'password' : 'mot2passe' }


# disk specifity
disk_spec = {'datacenter_id' : 1,
             'name' : 'sysdisk', 
             'size' : 10240}

# Id image of "Debian 8 64 bits (HVM)"
image_id = 3315704


# Create the server
vmCreate = api.hosting.vm.create_from(apikey, vm_spec, disk_spec, image_id)

#pp.pprint(vmCreate)

# Operation list
diskCreateOpe = api.operation.info(apikey, vmCreate[0]['id'])
ifaceCreateOpe = api.operation.info(apikey, vmCreate[1]['id'])
vmCreateOpe = api.operation.info(apikey, vmCreate[2]['id'])


vm_id = vmCreateOpe['params']['vm_id']

# Get the vm creation ope id
pp.pprint("vmCreateOpe : " + str(vmCreateOpe['id']))

pp.pprint("vm_id : " + str(vm_id))


vmInfo = api.hosting.vm.info(apikey, vm_id)


# Get the 1st network interface
ifaces = vmInfo['ifaces']
#pp.pprint(ifaces[0])

# Get the 1st ip address
ips = ifaces[0]['ips']

#pp.pprint(ips)

# First ipv4 address
IpAd1 = ips[0]['ip']

pp.pprint(IpAd1) 


print("*****************************************************")
sys.exit(0)
