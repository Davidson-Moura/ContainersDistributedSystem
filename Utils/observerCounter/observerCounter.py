import xmlrpc.client
import schedule
import asyncio
import random
import time

#host = "localhost"

def getCounter(host, p):
    try:
        url = 'http://'+ host + ':' + str(p)
        s = xmlrpc.client.ServerProxy(url)
        print(url)
        print(s.counter())
        s = None
    except Exception as e:
        print("Erro ao verificar contador")

def getCounters():
    getCounter("container1", 15741)
    getCounter("container2", 15742)
    getCounter("container3", 15743)
    getCounter("container4", 15744)
    print("-----------------------------")

async def addTest():
    try:
        url = 'http://'+ "container1" + ':' + str(15741)
        s = xmlrpc.client.ServerProxy(url)
        print(s.add(1))
        s = None
    except Exception as e:
        print("Erro ao verificar contador")

#asyncio.run(addTest())

schedule.every(3).seconds.do(getCounters)

while True:
    schedule.run_pending()
    time.sleep(1)

#print(s.pow(2,3))

#print(s.mul(5,2))

#print(s.system.listMethods())