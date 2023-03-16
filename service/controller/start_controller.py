from flask import Response
from flask_restplus import Resource

from service.restplus import api

start = api.namespace("")


@start.route('/', methods=['GET'])
class StartController(Resource):
    @api.response(200, 'Enviado com sucesso.')
    def get(self) -> dict:
        """Método para verificar se a rota está funcionando."""
        return Response('Welcome to Timezone Flask API.')