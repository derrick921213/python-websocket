'''from websocket_server import WebsocketServer
import sys
def new_client(client,server):
    print("Client(%d) has joined."% client['id'])
def client_left(client,server):
    print("Client(%d) disconnected."% client['id'])
def message_back(client,server,message):
    print("Client(%d) said: %s"%(client['id'],message))
    result = "伺服器以收到訊息..." + message
    server.send_message(client,result)
server = WebsocketServer(4200,host='')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_back)
server.run_forever()'''
from websocket_server import WebsocketServer
import sys
print(sys.getdefaultencoding())
# Called for every client connecting (after handshake)
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
    type = sys.getfilesystemencoding()    
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message_to_all("Client(%d) said: %s" % (client['id'], message))
    


PORT=4200
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()