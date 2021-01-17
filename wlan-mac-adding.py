#!/bin/python
#from __future__ import print_function
import os
import sys
import pprint
import time
#from OPSI.Backend.BackendManager import BackendManager

#backend = BackendManager()
#clients = backend.host_getObjects(type="OpsiClient")
# future plan maybe executing on server and access jsonrpcbackend remotely
#from OPSI.Backend.JSONRPC import JSONRPCBackend
#b = JSONRPCBackend(address="https://backup.paedml-linux.lokal:4447/rpc", username="administrator", password="xxxx")
#clients = b.host_getObjects(type="OpsiClient")

print('You need to have the opsi product hwaudit installed on the client to make this work!')
print('Please check if \'ssh root@server.paedml-linux.lokal\' is working from backup without errors!')
#raw_input('Press enter if you read info above and start the script.....')

# get all hosts and macs(if already added)
#allHosts = os.popen('ssh root@server.paedml-linux.lokal \'udm computers/windows list\'').read()
with open('testi.txt', "r") as file_object:
    data = file_object.read()
    file_object.close()

allHosts = data.split('DN:')
dictHosts = {}

for host in allHosts:
  # get hosts name
  start = 'cn='
  end = ','
  hosti = host[host.find(start)+len(start):host.find(end)]
  # check if 2 dhcpentryzones, if so, 2 macs....if len = 3, 2 dpchpentries...
  calcMacs = host.split('dhcpEntryZone:')
  dictHosts[hosti] = calcMacs
sys.exit()

for client in clients:
  # checking 1
  test_list = ['w10adminvm','admin-pc','adminvm']
  res = [ele for ele in test_list if(ele in client.id)] 
  if res:
    continue
  ak =  backend.getHardwareInformation_hash(client.id)
  for networkcontroller in ak[u'NETWORK_CONTROLLER']:
      if 'wireless' in networkcontroller[u'description'].lower():
          print("Checking MAC and DNS of  " + client.id + ": " + networkcontroller[u'macAddress'] + "...")#,end="")
          # check if second mac is already in allHosts
          clientName = client.id.split('.')
          if not dictHosts[clientName[0] = str('3'): 
            hashClient = backend.host_getHashes(id=client.id)
            sshCommandFirst = 'ssh root@server.paedml-linux.lokal \'udm computers/windows modify --dn=cn=' + clientName[0] + ',cn=computers,ou=schule,dc=paedml-linux,dc=lokal --append mac='+  networkcontroller[u'macAddress'] + ' --append "dhcpEntryZone=cn=schule,cn=dhcp,ou=schule,dc=paedml-linux,dc=lokal '+ hashClient[0]['ipAddress'] +' ' + networkcontroller[u'macAddress'] +'"\''
            os.command(sshCommandFirst)
            time.sleep(2)

print('End of filling wlan macs on server...')
