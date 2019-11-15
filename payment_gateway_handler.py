from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse


class paymentGatewayHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        parsePath = urlparse.urlparse(self.path)
        query = parsePath.query
        self.wfile.write("***** From Payment Gateway *****\n")
        self.wfile.write("***** Calling to Bank *****\n")

        amount = urlparse.parse_qs(query)['amount']
        result = self.call_to_bank(int(amount[0]))

        paymentResultText = "***** The Payment is " + result + " *****\n"
        self.wfile.write(paymentResultText)
        return

    def call_to_bank(self, amount):                                                               
        if amount < 100:
            return "NOT OK"
        else:
            return "OK"

