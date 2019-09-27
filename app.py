import falcon
from health_check import HealthCheck
from system import Exchange
from trading import OrderSubmit, TraderCheck



# create an api with these endpoints

exchange = Exchange()

APP = falcon.API()

health_check_resource = HealthCheck()
APP.add_route('/health', health_check_resource)

orders_resource = OrderSubmit(exchange)
APP.add_route('/orders', orders_resource)

orders_resource = TraderCheck(exchange)
APP.add_route('/orders/{id}', orders_resource)
