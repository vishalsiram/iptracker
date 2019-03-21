import os
import urllib.request as urllib2
import json
import sys

def Credit():
    print ("#############################################")
    print ("#+++++++++++++++IP TRACKER++++++++++++++++++#")
    print ("#        Script By Vishal Siram             #")
    print ("#------------Happy Hacking------------------#")
    print ("#############################################")
Credit()

while True:
    ip=input("What is your target IP: ")
    url= "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print(" IP: " + values['query'])
    print(" City: " + values['city'])
    print("ISP: "+ values['isp'])
    print("country: " + values['country'])
    print("Region: " + values['region'])
    print("Time zone: " + values['timezone'])

    break
