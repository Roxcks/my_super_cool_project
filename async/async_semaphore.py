import asyncio
class FileDownloader:
    def __init__(self, max_concurrent=2):
        self.sem = asyncio.Semaphore(max_concurrent) # создали семафор (пропускает 2 запроса серверу)
    async def download_file(self, file_name, delay): # сама корутина
        async with self.sem: # обозначаем, что функция выполняется как разрешает семафор
            print(f'Начинаем загрузку файла {file_name}...')
            await asyncio.sleep(delay)
            print(f'{file_name} успешно скачан!')

async def main():
    downloader = FileDownloader()
    downloads = [downloader.download_file('file1.txt', 1), downloader.download_file('file2.txt', 1),
                 downloader.download_file('file3.txt', 1), downloader.download_file('file4.txt', 1),
                 downloader.download_file('file5.txt', 1), downloader.download_file('file6.txt', 1),
                 downloader.download_file('file7.txt', 1), downloader.download_file('file8.txt', 1)]
    await asyncio.gather(*downloads) # просит запустить все задачи одновременно и отдать результат, когда закончит

asyncio.run(main())