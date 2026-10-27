import asyncio
# криптокошелек, где используется lock для того, чтобы все транзакции выполнялись по очереди
# если все будут выполняться одновременно, то изменения будут хаотичнымиё
class CryptoWallet:
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.__balance = initial_balance
        self.lock = asyncio.Lock() # создаем замок 

    @property # ограничиваем доступ к балансу извне
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            raise ValueError('Баланс не может быть отрицательным')

    async def process_transaction(self, amount, delay):
        async with self.lock:
            current = self.__balance
            print('Проводим транзакцию...')
            await asyncio.sleep(delay)
            self.__balance = current + amount
            print(f'Транзакция завершена, баланс пополнен: {self.__balance}р.')

async def main(): # запускаем коритину на 10 циклов
    account = CryptoWallet('Роксана', 3000.0)
    tasks = [account.process_transaction(200, 0.1) for _ in range(10)]
    await asyncio.gather(*tasks)

    print(f"✨ Итоговый баланс через класс: {account.balance}")


asyncio.run(main())



