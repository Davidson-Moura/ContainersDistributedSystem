import xmlrpc.client
import schedule
import asyncio
import random
import time

ports = [15741, 15742, 15743, 15744]

def get_host(p):
    if(p == 15741):
        return "container1"
    if(p == 15742):
        return "container2"
    if(p == 15743):
        return "container3"
    if(p == 15744):
        return "container4"

def addTest():
    try:
        requestPort = random.sample(ports, 1)[0]
        print(requestPort)
        url = 'http://'+ get_host(requestPort) + ':' + str(requestPort)
        s = xmlrpc.client.ServerProxy(url)
        print(requestPort, " - ", s.add(1))
    except Exception as e:
        print("Erro ao verificar contador")

addTest()
schedule.every(10).seconds.do(addTest)

while True:
    schedule.run_pending()
    time.sleep(1)