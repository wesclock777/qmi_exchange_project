import socket
import falcon
import json

class OrderSubmit:
    # POST request for submitting orders
    # tested using curl

    def __init__(self, exchange):
        self.exchange = exchange
    def on_post(self, request, response):

        body = request.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',\
            'A valid JSON document is required.')

        d = json.loads(body.decode('utf-8'))
        id = d['data']['traderId']
        orders = d['data']['orders']


        for order in orders:
            self.exchange.add_order(id, order)

        response.status = falcon.HTTP_200

class TraderCheck:
    # GET request for getting information on traders
    def __init__(self, exchange):
        self.exchange = exchange
    def on_get(self, request, response, id):

        orders = {
            "data": self.exchange.ret_orders(id)
        }

        response.media = orders
        response.status = falcon.HTTP_200
