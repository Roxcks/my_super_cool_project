import asyncio
class ReportGenerator: # создаем класс, который генерирует отчеты в заданных форматах
    def __init__(self, num_workers=2):
        self.num_workers = num_workers
        self.queue = asyncio.Queue() # создаем очередь

    async def worker(self, worker_id): # создаем воркера, в качестве аргумента передается номер воркера
        while True: # запускаем цикл выполнения задач в очереди
            report_type = await self.queue.get() # берем задачу из очереди, называем ее report_type
            # выносим get из блока try, чтобы функция не отчитывалась при отсутствии задач
            try: 
                print(f'worker{worker_id}: Создаем файл отчета в формате {report_type}')
                print(f'worker{worker_id}: Отчет в формате {report_type} готов!')
            finally:
                self.queue.task_done() # сообщаем очереди, что задача выполнена и можно делать следующую
                

    async def add_requests(self, report_types): #производитель, берет аргументом список
        for report_type in report_types:
            await self.queue.put(report_type) # кладет элемент списка на конвейер
            print(f'Запрос на отчет в формате {report_type} добавлен в очередь')
            await asyncio.sleep(0.5)

    async def run(self, report_types): # главный исполнитель
        # передает в функцию worker i - номер воркера и генерирует кол-во воркеров
        workers = [asyncio.create_task(self.worker(i)) for i in range (1, self.num_workers + 1)]
        await self.add_requests(report_types) # запускает производитель
        await self.queue.join() # ждет, пока все задачи будут выполнены
        for w in workers: # отменяет воркеров, когда всё выполнено
            w.cancel()

async def main():
    generator = ReportGenerator(3) # создает объект класса
    my_file_types = ['PNG', 'PDF', 'WORD', 'EXCEL', 'TXT', 'JSON'] # список форматов
    await generator.run(my_file_types) # запускает run и передает список

    print('Все отчеты готовы!')

asyncio.run(main())







            

