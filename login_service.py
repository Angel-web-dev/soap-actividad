from spyne import Application, rpc, ServiceBase, Unicode, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class LoginService(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Unicode)
    def login(ctx, username, password):
        # Simulación de verificación de usuario
        if username == "admin" and password == "1234":
            return "✅ Login exitoso. Bienvenido, admin."
        else:
            return "❌ Credenciales incorrectas."


application = Application(
    [LoginService],
    tns='spyne.login.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("🚀 Servicio SOAP de Login ejecutándose en http://localhost:8001/?wsdl")
    server = make_server('0.0.0.0', 8001, wsgi_app)
    server.serve_forever()
