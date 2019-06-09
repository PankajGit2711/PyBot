from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from pybot import startchat

class ChatServer(WebSocket):

    def handleMessage(self):
        message = self.data
        response = startchat(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
