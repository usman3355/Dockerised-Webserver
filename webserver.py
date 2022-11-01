from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector import Error
from db import create_db_connection,read_query

hostName = "localhost"
serverPort = 8080
query = "SELECT name FROM users WHERE id = 1;"

class webser(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            db_co = create_db_connection()
            data = read_query(db_co,query)
            current_user = data[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title> Web server developed by : %s</title></head>" % current_user, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p> it is a containarised App mysql and webserver</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        
        except Error as err:
            print(f"Error: '{err}'")



    


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), webser)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped.")
