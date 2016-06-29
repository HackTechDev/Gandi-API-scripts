#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys
import time 
from time import gmtime, strftime

pp = pprint.PrettyPrinter(indent=4)

api = xmlrpc.client.ServerProxy('https://rpc.gandi.net/xmlrpc/')
apikey = '<API KEY>'


logVMFile = "VM.log"
logFile = "deletedVM.log"

vmCount = 0

print("*****************************************************")
print("List of Virtual Machine")

vmList = api.hosting.vm.list(apikey)
#pp.pprint(vmList)


for vm in vmList:
    # Get the vm
    print("*****************************************************")
    vm_id = vm['id']
    vm_hostname = vm['hostname']
    pp.pprint(str(vmCount) + ":" + str(vm_id) + " " + vm_hostname)

    vmInfo =  api.hosting.vm.info(apikey, vm_id)
    #pp.pprint(vmInfo)

    # Delete the vm
    print("  vm deletetion in progress")


    print("  vm stop:" + vm_hostname)
    vmStop = api.hosting.vm.stop(apikey, vm_id)
    pp.pprint("    ope:" + str(vmStop['id']) + ":" + vmStop['step'])
    

    # TODO: Replace by 'step' checker
    time.sleep(60)

 
    # Get operation information
    opeInfo = api.operation.info(apikey, vmStop['id'])
    pp.pprint("    ope:" + str(opeInfo['id']) + ":" + opeInfo['step'])
   

    # When 'Stop' operation step if done/finished
    if opeInfo['step'] == "DONE":
        print("  vm delete:" + vm_hostname)
        vmDelete = api.hosting.vm.delete(apikey, vm_id)

        pp.pprint("    ope:" + str(vmDelete['id']) + ":" + vmDelete['step'])

        # TODO: Replace by 'step' checker
        time.sleep(60)

        # Get operation information
        opeInfo = api.operation.info(apikey, vmDelete['id'])
    
        # When 'Delete' operation step if done/finished
        if opeInfo['step'] == "DONE":
            pp.pprint("    ope:" + str(opeInfo['id']) + ":" + opeInfo['step'])

            # Write to a log file
            with open(logFile, 'a') as file:
                dateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                file.write(dateTime + ":" + str(vmCount) + ":" + str(vm_id) + ":" + vm_hostname + "\n")

    vmCount +=1
   
print("*****************************************************")
sys.exit(0)
