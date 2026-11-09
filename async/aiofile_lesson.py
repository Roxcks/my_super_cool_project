import asyncio
import aiofiles

async def save_complaint(username: str, text: str):
    # менеджер контекстов, создает файл, если его нет и записывает в конец
    async with aiofiles.open('complaints.txt', 'a', encoding='utf-8') as doc:
        await doc.write(f'{username}: {text}\n') # обязательно await, надо дождаться результата
    
    # теперь открыть в режиме чтения
    async with aiofiles.open('complaints.txt', 'r', encoding='utf-8') as doc:
        content = await doc.read() # не забываем await
    
    print("--- Содержимое файла ---")
    print(content)

async def main():
    for i in range(3):
        await save_complaint(f'User_{i}', "Website doesn't work")

asyncio.run(main())