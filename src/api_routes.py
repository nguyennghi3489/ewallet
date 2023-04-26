from config.api import BASE_PATH
from routes import Mapper
import controllers.merchant
import controllers.account

route_mapper = Mapper()
route_mapper.prefix = BASE_PATH

route_mapper.connect(
    None,
    '/merchant/signup',
    controller=controllers.merchant.signup)


route_mapper.connect(
    None,
    '/account',
    controller=controllers.account.create)


route_mapper.connect(
    None,
    '/account/{accountId}/token',
    controller=controllers.account.token)

route_mapper.connect(
    None,
    '/account/topup',
    controller=controllers.account.topup)
  