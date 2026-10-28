import asyncio
# класс проверки пинов серверов
class ServerMonitor:
    def __init__(self, num_workers=2):
        self.queue = asyncio.Queue()  # создаем очередь
        self.num_workers = num_workers

    async def check_server(self, worker_id):  
    # метод воркер, стоит у очереди и берет оттуда задачи
        while True:
            try: # нужно использовать try, иначе если произойдет ошибка, программа ляжет
                # 1. Забираем конкретный сервер из очереди
                server_name = await self.queue.get()

                print(
                    f" Воркер {worker_id} проверяет сервер:"
                    f" {server_name}..."
                )
                await asyncio.sleep(0.5)
                print(f"Сервер {server_name} работает!")
            finally:
                self.queue.task_done()

    async def add_servers(self, servers_list):  
    # производитель, берет список серверов и по одному закидывает в очередь
        for server in servers_list:
            await self.queue.put(server)  # поставили сервер на конвейер
            print(f"📥 Добавили в очередь: {server}")
            await asyncio.sleep(0.2)

    async def run(self, servers_list):
    # главный диспетчер, запускает процесс
    # 1 - нанимает рабочих и расставляет у конвейера
        workers = [
            asyncio.create_task(self.check_server(i))
            for i in range(1, self.num_workers + 1)
        ]

        # 2 - запускает закидывание задач на конвейер
        await self.add_servers(servers_list)

        # 3 - ждет, пока абсолютно все задачи не будут выполнены
        await self.queue.join()

        # 4 - когда всё готово, убирает рабочих
        for w in workers:
            w.cancel()


async def main():
    # пуск, создает объект класса ServerMonitor
    # 1 - создает саму фабрику
    monitor = ServerMonitor(num_workers=2)
    # 2 - задает список серверов
    my_servers = [
        "api.server.com",
        "auth.server.com",
        "db.server.com",
        "cache.server.com",
    ]
    # 3 - запускает главный метод run и ждет, когда закончится
    await monitor.run(my_servers)

    print("Все серверы успешно проверены!")


asyncio.run(main())
    