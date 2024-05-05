import xmlrpc.client
import schedule
import time
import random

host = "localhost"
lista = [15741,15742,15743,15744]

port = 15741 #random.sample(lista, 1)[0]

url = 'http://'+ host +':' + str(port)
print(url)

s = xmlrpc.client.ServerProxy(url)

def add():
    try:
        print(s.add(2))
    except Exception as e:
        print("Erro:", e)

def getCounter():
    try:
        print(s.add(2))
    except Exception as e:
        print("Erro:", e)

schedule.every(5).seconds.do(add)
schedule.every(10).seconds.do(getCounter)

add()
#getCounter()

while True:
    schedule.run_pending()
    time.sleep(1)

#print(s.pow(2,3))

#print(s.mul(5,2))

#print(s.system.listMethods())