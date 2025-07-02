from tinkoff.invest import Client, MoneyValue, OrderDirection, OrderType
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

TOKEN = 'Ваш API токен Т-Инвест песочницы'
acc_name = "Имя счета"
acc_id = "Айди счета"

with Client(TOKEN, target=INVEST_GRPC_API_SANDBOX) as client:
    #Открытие аккаунта
    #client.sandbox.open_sandbox_account(name = acc_name)
    #Закрытие аккаунта
    #client.sandbox.close_sandbox_account(account_id = acc_id)
    #Пополнение
    #client.sandbox.sandbox_pay_in(account_id = acc_id, amount = MoneyValue(units = 10000, nano = 990000000, currency = 'rub'))
    #Покупка
    #client.orders.post_order(figi = "BBG004730N88", quantity = 1, account_id = acc_id, direction= OrderDirection.ORDER_DIRECTION_BUY, order_type = OrderType.ORDER_TYPE_MARKET)
    #Продажа
    #client.orders.post_order(figi = "BBG004730N88", quantity = 1, account_id = acc_id, direction = OrderDirection.ORDER_DIRECTION_SELL, order_type = OrderType.ORDER_TYPE_MARKET)
