import SocketServer
import payment_gateway_handler

PORT = 8002
Handler = payment_gateway_handler.paymentGatewayHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

try:
    print "serving at port", PORT
    httpd.serve_forever()

except KeyboardInterrupt:
    print "shutting down the web server"
    httpd.socket.close()

