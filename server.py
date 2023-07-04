from http.server import BaseHTTPRequestHandler, HTTPServer

# Definizione della classe del gestore delle richieste
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Imposta il codice di risposta a 200 (OK)
        self.send_response(200)
        
        # Imposta l'intestazione della risposta
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Contenuto della risposta
        response_content = "<h1>Benvenuto nel server Python!</h1>"
        response_content = "<h2>Questa pagina funziona traminte un file server.py</h2>"
        
        # Invia la risposta al client
        self.wfile.write(response_content.encode())

# Definizione dell'indirizzo IP e della porta del server
server_address = ('', 8000)

# Creazione dell'istanza del server HTTP
print('Server in avviamento')
httpd = HTTPServer(server_address, RequestHandler)
print('Server in esecuzione...')

# Avvio del server
httpd.serve_forever()