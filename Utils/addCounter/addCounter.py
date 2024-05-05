import xmlrpc.client
import schedule
import asyncio
import random
import time

def addTest():
    try:
        url = 'http://'+ "container1" + ':' + str(15741)
        s = xmlrpc.client.ServerProxy(url)
        print(s.add(1))
    except Exception as e:
        print("Erro ao verificar contador")

addTest()
schedule.every(10).seconds.do(addTest)

while True:
    schedule.run_pending()
    time.sleep(1)