import time
import telebot
from tinkoff.invest import Client, Operation


from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

TOKEN = 'Ваш API токен Т-Инвест песочницы'

BOT_TOKEN = 'Токен бота'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_messages(message):
    with (Client(TOKEN, target=INVEST_GRPC_API_SANDBOX) as client):
        def acc_selection():
            mas_acc = client.users.get_accounts().accounts
            if mas_acc:
                print("Выберите счет, по которому вы хотите получать уведомления обо всех операциях:")
                for index, acc in enumerate(mas_acc):
                    print(f"{index+1}. Имя: {acc.name}, ID: {acc.id}")
                return choice(mas_acc) - 1
            else:
                print("Счета не найдены")
                acc_creating()
                return 0

        def acc_creating():
            print("Создание счета:")
            acc_name = input("Введите имя счета: ")
            client.sandbox.open_sandbox_account(name = acc_name)

        def choice(mas_acc):
            while True:
                try:
                    c = int(input())
                    if 1 <= c <= len(mas_acc):
                        return c
                    else:
                        print("Указан неверный пункт меню!")
                except ValueError:
                    print("Ошибка: Введите целое число!")

        def operation_message(operation: Operation, id):
            if operation.operation_type.value == 1:
                return f"НОВАЯ ОПЕРАЦИЯ:\nID: {operation.id}\nТип операции: {operation.type}\nСумма: {operation.payment.units},{int(operation.payment.nano / pow(10, 7))} {operation.payment.currency}\nДата: {operation.date}" + portfolio_balance(id)
            if operation.operation_type.value == 15 or operation.operation_type.value == 22:
                n = 1
                if operation.operation_type.value == 15:
                    n *= -1
                instrument_type = operation.instrument_type
                if instrument_type == "share":
                    instrument_type = "акция"
                elif instrument_type == "bond":
                    instrument_type = "облигация"
                elif instrument_type == "currency":
                    instrument_type = "облигация"
                elif instrument_type == "etf":
                    instrument_type = "фонд"
                elif instrument_type == "futures":
                    instrument_type = "фьючерс"
                return f"НОВАЯ ОПЕРАЦИЯ:\nID: {operation.id}\nТип операции: {operation.type}\nТип инструмента: {instrument_type}\nFigi-идентификатор: {operation.figi}\nЦена(за 1 инструмент): {operation.price.units},{int(operation.price.nano / pow(10, 7))} {operation.price.currency}\nКол-во: {operation.quantity}\nСумма: {operation.payment.units},{int(n*operation.payment.nano / pow(10, 7))} {operation.payment.currency}\nДата: {operation.date}"
            if operation.operation_type.value == 19:
                return f"КОМИССИЯ ПО ПРЕДЫДУЩЕЙ ОПЕРАЦИИ:\nID: {operation.id}\nСумма: {operation.payment.units},{int(-1*operation.payment.nano / pow(10, 7))} {operation.payment.currency}\nДата: {operation.date}" + portfolio_balance(id)
            return "Операция не прошла"

        def portfolio_balance(id):
            current_portfolio = client.operations.get_portfolio(account_id = id)
            return f"\n----------------------\nБАЛАНС ПОРТФЕЛЯ:\nОбщая стоимость валют: {current_portfolio.total_amount_currencies.units},{int(current_portfolio.total_amount_currencies.nano / pow(10, 7))} {current_portfolio.total_amount_currencies.currency}\nОбщая стоимость акций: {current_portfolio.total_amount_shares.units},{int(current_portfolio.total_amount_shares.nano / pow(10, 7))} {current_portfolio.total_amount_shares.currency}\nОбщая стоимость облигаций: {current_portfolio.total_amount_bonds.units},{int(current_portfolio.total_amount_bonds.nano / pow(10, 7))} {current_portfolio.total_amount_bonds.currency}\nОбщая стоимость фондов: {current_portfolio.total_amount_etf.units},{int(current_portfolio.total_amount_etf.nano / pow(10, 7))} {current_portfolio.total_amount_etf.currency}\nОбщая стоимость фьючерсов: {current_portfolio.total_amount_futures.units},{int(current_portfolio.total_amount_futures.nano / pow(10, 7))} {current_portfolio.total_amount_futures.currency}"

        index_of_acc = acc_selection()
        current_acc = client.users.get_accounts().accounts[index_of_acc]
        id_of_acc = current_acc.id
        print(f"Выбран счёт {index_of_acc+1}. Имя: {current_acc.name}, ID: {id_of_acc}")

        flag_print = True
        flag_first_iteration = True

        while True:
            try:
                op = client.operations.get_operations(account_id=id_of_acc).operations

                if op:

                    flag_new_operation = False

                    if flag_first_iteration:
                        flag_first_iteration = False
                        last_operation = op[0]


                    for index, operation in enumerate(op):
                        if operation.id == last_operation.id:
                            k = index
                            break

                    if k != 0:
                        for i in range(k-1, -1, -1):
                            bot.send_message(message.chat.id, operation_message(op[i], id_of_acc))
                            flag_new_operation = True

                    if flag_new_operation:
                        last_operation = op[0]

                elif flag_print:
                    print("Нет операций!")
                    flag_print = False


            except Exception as e:
                print(f"Ошибка: {e}")

            time.sleep(5)

bot.infinity_polling()
