from http.server import BaseHTTPRequestHandler


import sql_connector
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

 # Generowanie HTML z wynikami
            response = "<h1>Lista użytkowników</h1><ul>"
            users = sql_connector.selectAll()
            for user in users:
                print(user)
                response  += f"""
                <li>ID: {user[0]}, Imię: {user[1]}, Nazwisko:{user[2]}  </li>"""
            response += "</ul>"

        else:
        # Strona domyślna
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            response = f"""
            <h1>Witaj na moim serwerze!</h1>
            <p>Ścieżka: </p> {self.path}</p>
            <p><a href="/users">→ Zobacz użytkowników</a></p>"""
        # Wysłanie odpowiedzi
        self.wfile.write(response.encode('utf-8'))






