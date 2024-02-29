import os
import urllib2
import json
while True:
    ip=raw_input("input ip")
    url="https://ip-api.com/json/"
    responce=urllib2.urlopen(url+ip)
    data=responce.read()
    values=json.loads(data)

    print("IP:"+values['query'])
    print("city:"+values['city'])
    print("ISB:"+values['isb'])
    print("Country:"+values['country'])
    print("Region:"+values['region'])
    print("Time-Zone:"+values['timezone'])

    break
