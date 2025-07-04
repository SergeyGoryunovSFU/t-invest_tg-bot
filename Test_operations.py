from tinkoff.invest import Client, MoneyValue, OrderDirection, OrderType, InstrumentStatus
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

TOKEN = 'Ваш API токен Т-Инвест песочницы'
acc_name = "Имя счета"
acc_id = "Айди счета"

#Примеры figi-идентификаторов для инструментов разных типов (они рабочие)
figi_share = "BBG004730N88"
figi_bond = "TCS99A106J04"
figi_currency = "BBG0013J7Y00"
figi_etf = "TCS10A106G80"
figi_futures = "FUTMIX092500"

with Client(TOKEN, target=INVEST_GRPC_API_SANDBOX) as client:
    #Открытие аккаунта
    #client.sandbox.open_sandbox_account(name = acc_name)
    #Закрытие аккаунта
    #client.sandbox.close_sandbox_account(account_id = acc_id)
    #Пополнение счета
    #client.sandbox.sandbox_pay_in(account_id = acc_id, amount = MoneyValue(units = 10000, nano = 990000000, currency = 'rub'))
    #Покупка акции
    #client.orders.post_order(figi = figi_share, quantity = 1, account_id = acc_id, direction= OrderDirection.ORDER_DIRECTION_BUY, order_type = OrderType.ORDER_TYPE_MARKET)
    #Продажа акции
    #client.orders.post_order(figi = figi_share, quantity = 1, account_id = acc_id, direction = OrderDirection.ORDER_DIRECTION_SELL, order_type = OrderType.ORDER_TYPE_MARKET)

    #Методы для просмотра всех возможных инструментов разных типов: акции, облигации, валюты, фонды и фьючерсы. Переменной assets присвоить соответствующий тип инструмента
    #shares = client.instruments.shares(instrument_status = InstrumentStatus(1)).instruments
    #bonds = client.instruments.bonds(instrument_status = InstrumentStatus(1)).instruments
    #currency = client.instruments.currencies(instrument_status = InstrumentStatus(1)).instruments
    #etf = client.instruments.etfs(instrument_status = InstrumentStatus(1)).instruments
    #futures = client.instruments.futures(instrument_status = InstrumentStatus(1)).instruments
    #assets = shares/bonds/currency/etf/furutes
    #for asset in assets:
    #    print(f"{asset}\n")
