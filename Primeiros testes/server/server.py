from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

host = "localhost"
host = "0.0.0.0"
port = 15740
print(host + ":" + str(port))

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler) as server:    
    #server.register_introspection_functions()

    #server.register_function(pow)

    def adder_function(x):
        return x

    server.register_function(adder_function, 'add')

    class MyFuncs:
        def mul(self, x, y):
            return x * y

    #server.register_instance(MyFuncs())

    server.register_multicall_functions()
    server.serve_forever()