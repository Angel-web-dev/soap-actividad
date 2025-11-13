from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class TemperatureService(ServiceBase):

    @rpc(Float, _returns=Float)
    def c_to_f(ctx, celsius):
        return (celsius * 9/5) + 32

    @rpc(Float, _returns=Float)
    def f_to_c(ctx, fahrenheit):
        return (fahrenheit - 32) * 5/9

    @rpc(Float, _returns=Float)
    def f_to_k(ctx, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15


# Configuración de la app SOAP
application = Application(
    [TemperatureService],
    tns='spyne.temperature.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("🚀 Servicio SOAP de Temperatura ejecutándose en http://localhost:8000/?wsdl")
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()