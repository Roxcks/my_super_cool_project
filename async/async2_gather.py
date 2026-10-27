import asyncio

async def check_server(server_name, delay, is_down=False):
      print(f'Делаем запрос на сервер: {server_name}...')
      await asyncio.sleep(delay)
      if is_down == True:
            raise ConnectionError(f'Сервер {server_name} недоступен!')
      return {"server": server_name, "status": "online", "response_time": delay}

async def check_server_with_timeout(server_name, delay, timeout_sec, is_down=False):
      try:
        # Пытаемся выполнить проверку сервера, но не дольше timeout_sec
        result = await asyncio.wait_for(
            check_server(server_name, delay, is_down), 
            timeout=timeout_sec
        )
        return result
      except asyncio.TimeoutError:
        # Если сработал таймаут, мы выбрасываем TimeoutError, 
        # который gather поймает благодаря return_exceptions=True!
        raise TimeoutError(f"⏰ Сервер {server_name} превысил лимит времени ({timeout_sec}с)!")

async def main():
      print('Проверяем работу серверов...')
      servers = await asyncio.gather(check_server('Яндекс', 5, is_down=True), 
                                     check_server('Google', 2, is_down=False),
                                     check_server_with_timeout('Amazon', 6, timeout_sec=2.0, is_down=False),
                                     check_server('OpenAI', 3, is_down=False),
                                     return_exceptions=True
                                    )
      for res in servers:
            if isinstance(res, Exception):
                  print(f'ОШИБКА: {res}')
            else:
                  print(f'Успех! Сервер {res} ответил!')

asyncio.run(main())
