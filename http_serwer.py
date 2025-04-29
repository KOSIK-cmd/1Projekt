from http.server import BaseHTTPRequestHandler
import sql_connector
class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/users":
            response = self.getUsers()
        elif self.path == "/deleteUser":
            response = self.deleteUser()
            response += "udało się"
        elif self.path == "/addUser":
            response = self.addUser()

        else:
            response = self.getDefaultPage()
        self.wfile.write(response.encode('utf-8'))
        # Strona domyślna

    def getUsers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = "<h1>Lista użytkowników</h1><ul>"
        users = sql_connector.selectAll()
        for user in users:
            print(user)
            response += f"""
            <li>ID: {user[0]}, Imię: {user[1]}, Nazwisko:{user[2]}  </li>"""
        response += "</ul>"
        # Generowanie HTML z wynikami

    def getDefaultPage(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        response = f"""
        <h1>Witaj na moim serwerze!</h1>
        <p>Ścieżka: </p> {self.path}</p>
        <p><a href="/users">→ Zobacz użytkowników</a></p>"""
        # Generowanie HTML z wynikami

    def deleteUser(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        sql_connector.deleteCustomer()

    def addUser(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = sql_connector.addCustomer()





