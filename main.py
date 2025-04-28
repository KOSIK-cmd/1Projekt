import sqlite3
from http_serwer import SimpleHandler
from warnings import catch_warnings
import sql_connector
from http.server import BaseHTTPRequestHandler, HTTPServer


# sql_connector.addCustomer(input("podaj imię: "),input("podaj nazwisko: "),input("podaj email: "),input("podaj numer telefonu: "))
#
# sql_connector.selectCustomerByID(input("podaj ID customera: "))
#
# sql_connector.selectCustomerByEmail(input("podaj email customera: "))
#
# sql_connector.selectCustomerByPhone(input("podaj telefon customera: "))
#
# sql_connector.selcetCustomerByFirstName(input("podaj imię customera: "))
#
# sql_connector.selectCustomerByLastName(input("podaj nazwisko customera: "))
# try:
#     sql_connector.deleteCustomer(int(input("podaj ID do usnięcia: ")))
# except: pass

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serwer raczej działa na porcie {port}...')
    httpd.serve_forever()
run()


                   



