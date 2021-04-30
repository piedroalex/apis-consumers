# CONSUMINDO UMA API SOAP
from zeep import Client

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1('Joao', 'Maria')
print(result)