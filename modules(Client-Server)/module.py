from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import schedule
import asyncio
import random
import json
import time
import os

host = "0.0.0.0"

realPort = int(os.environ.get('MY_PORT'))
jsonPorts = os.environ.get('PORTS')

ports = json.loads(jsonPorts) #[15741,15742,15743,15744]
#ports.remove(realPort)

receivedMessages = []

class MyModule:
    realPort = realPort
    requestHost = "localhost"
    requestPorts = ports
    counter = 0

class IntrospectionHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class MeuServidorXMLRPC(SimpleXMLRPCServer):
    def __init__(self, endereco, funcao_a_cada_loop, *args, **kwargs):
        self.funcao_a_cada_loop = funcao_a_cada_loop
        super().__init__(endereco, requestHandler=IntrospectionHandler, *args, **kwargs)

    def handle_request(self):
        print("Aqui")
        self.funcao_a_cada_loop()
        super().handle_request() 

#class RequestHandler(SimpleXMLRPCRequestHandler):
#    rpc_paths = ('/RPC2',)

#with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler) as server:

def get_host(p):
    if(p == 15741):
        return "container1"
    if(p == 15742):
        return "container2"
    if(p == 15743):
        return "container3"
    if(p == 15744):
        return "container4"

def get_msgKey():
    return str(MyModule.realPort) + "-" + str(MyModule.counter)

with MeuServidorXMLRPC((host, realPort), schedule.run_pending) as server:
    print(host + ":" + str(realPort))

    # Functions
    def adder_function(x):
        MyModule.counter += x

        print(get_msgKey())
        receivedMessages.append(get_msgKey())

        propagate_the_change(x, MyModule.realPort, 0, get_msgKey()) #asyncio.run(propagate_the_change(x))
        return MyModule.counter

    def counter_function(): 
        return MyModule.counter

    def get_url(p):
        return 'http://'+ get_host(p) + ':' + str(p)
    
    def propagate_the_change(value, originPort, itSendPort, msgKey): #async def propagate_the_change(value):
        for p in MyModule.requestPorts:
            if(originPort != p and p != itSendPort):
                try:
                    requestUrl = get_url(p)
                    s = xmlrpc.client.ServerProxy(requestUrl)
                    s.changedCounter(value, originPort, MyModule.realPort, msgKey)
                except Exception as e:
                    print("Erro request:", e)
        return 1
    
    def changed_counter(valueAdded, originPort, itSendPort, msgKey):
        print("mensagem repassada", msgKey)
        if msgKey in receivedMessages:
            return 0
        receivedMessages.append(msgKey)

        if(originPort != MyModule.realPort):
            MyModule.counter += valueAdded
            propagate_the_change(valueAdded, originPort, itSendPort, msgKey)# asyncio.run(propagate_the_change(valueAdded))

        return 1

    # Requests
    def requestAdd():
        try:
            requestPort = random.sample(MyModule.requestPorts, 1)[0]
            requestUrl = get_url(requestPort)
            s = xmlrpc.client.ServerProxy(requestUrl)
            s.add(1)
        except Exception as e:
            print("Erro request:", e)
    
    # Register functions
    server.register_function(adder_function, 'add')
    server.register_function(counter_function, 'counter')
    server.register_function(changed_counter, 'changedCounter')

    # Init Requests
    # schedule.every(10).seconds.do(requestAdd)

    # Init Server
    server.register_introspection_functions()
    server.register_multicall_functions()
    server.serve_forever()

    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)