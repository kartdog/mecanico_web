
class Carro():
    def __init__(self, request):
        self.session = request.session

        # Obtener la key de la sesión si es que existe.
        carro = self.session.get('session_key')

        # Si el usuerio es nuevo, no hay sesión & se crea una.
        if 'session_key' not in request.session:
            carro = self.session['sesion_key'] = {}

        # Asegurar que carro este disponible en cualquier pág.
        self.carro = carro