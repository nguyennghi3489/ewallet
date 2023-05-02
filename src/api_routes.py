from config.api import BASE_PATH
from routes import Mapper
import controllers.merchant
import controllers.account
import controllers.transaction

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


route_mapper.connect(
    None,
    '/transaction/create',
    controller=controllers.transaction.create)

route_mapper.connect(
    None,
    '/transaction/confirm',
    controller=controllers.transaction.confirm)

route_mapper.connect(
    None,
    '/transaction/verify',
    controller=controllers.transaction.verify)
  