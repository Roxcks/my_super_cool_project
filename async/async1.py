# задача на использование asyncio.create_task
import asyncio
import time
# пишем 3 корутины
async def coffee():
    print('[кофе]: ставим чайник')
    await asyncio.sleep(3) # говорим event loop вернуться через 3 сек, пока другие дела сделать
    print('Кофе готов!')
async def make_sandwich():
    print('[бутерброд]: делаем бутерброд')
    await asyncio.sleep(4)
    print('бутерброд готов!')
async def iron_shirt():
    print('[рубашка]: гладим рубашку')
    await asyncio.sleep(4)
    print('рубашка поглажена!')
async def main():
    start_time = time.time()
    print('Выполняем утреннюю рутину...')

    task1 = asyncio.create_task(coffee()) # превращаем в таск
    task2 = asyncio.create_task(make_sandwich())
    task3 = asyncio.create_task(iron_shirt())

    await task1 # запускаем
    await task2
    await task3

    end_time = time.time()
    print(f'Задача завершена за {end_time - start_time}с')

asyncio.run(main()) # запуск основной корутины (обязательно!!!)
