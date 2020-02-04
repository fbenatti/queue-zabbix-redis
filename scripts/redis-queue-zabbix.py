#!/usr/bin/python2.7
import redis
import json
import protobix
import socket
import sys

hostname = socket.gethostname()
redishost=hostname+'.tpn.terra.com'
redisport="6379"

r = redis.Redis(host=redishost,port=redisport)
listkeys=r.keys('*')

##Return discovery
print '{"data":['
fila = []
n=0
nome_fila = []
for key in listkeys:  
	print('{"{#FILA}":"%s"},' % (key))

print('{"{#FILA}":"TotalObjetos"}')	
print(']}')

##Update items.
data1 = {}
data2 = {}
totobjs=0

for key in listkeys:  
    totitens=(r.llen(key))
    kb = "fila.redis[" + key + "]"
    data2[kb] = totitens
    totobjs = totobjs + totitens

kb = 'fila.redis[TotalObjetos]'
data2[kb] = totobjs	
data1[hostname] = data2
DATA = json.loads(json.dumps(data1))
zbx = protobix.DataContainer()
zbx.data_type = 'items'
zbx.add(DATA)
zbx.send()

