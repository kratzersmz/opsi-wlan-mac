#!/bin/python
from __future__ import print_function
import os
import sys
import pprint
import time
from OPSI.Backend.BackendManager import BackendManager

backend = BackendManager()
clients = backend.host_getObjects(type="OpsiClient")
# future plan maybe executing on server and access jsonrpcbackend remotely
#from OPSI.Backend.JSONRPC import JSONRPCBackend
#b = JSONRPCBackend(address="https://backup.paedml-linux.lokal:4447/rpc", username="administrator", password="xxxx")
#clients = b.host_getObjects(type="OpsiClient")

print('You need to have the opsi product hwaudit installed on the client to make this work!')
print('Please check if \'ssh root@server.paedml-linux.lokal\' is working from backup without errors!')
print('Starting with getting macs an filling server entries.....')

for client in clients:
  # checking 1
  test_list = ['w10adminvm','admin-pc','adminvm']
  res = [ele for ele in test_list if(ele in client.id)] 
  if res:
    continue
  ak =  backend.getHardwareInformation_hash(client.id)
  for networkcontroller in ak[u'NETWORK_CONTROLLER']:
      if 'wireless' in networkcontroller[u'description'].lower():
          print("Adding MAC and DNS of  " + client.id + ": " + networkcontroller[u'macAddress'])
          hashClient = backend.host_getHashes(id=client.id)
          clientName = client.id.split('.')
          sshCommandFirst = 'ssh root@server.paedml-linux.lokal \'udm computers/windows modify --dn=cn=' + clientName[0] + ',cn=computers,ou=schule,dc=paedml-linux,dc=lokal --append mac='+  networkcontroller[u'macAddress'] + ' --append "dhcpEntryZone=cn=schule,cn=dhcp,ou=schule,dc=paedml-linux,dc=lokal '+ hashClient[0]['ipAddress'] +' ' + networkcontroller[u'macAddress'] +'"\''
          os.command(sshCommandFirst)
          time.sleep(2)

print('End of filling wlan macs on server...')
