from colorama import Fore, Back, Style, init

# Обязательная инициализация для корректной работы в Windows (в macOS/Linux тоже не помешает)
init(autoreset=True)

# Примеры использования
print(Fore.YELLOW + "Этот текст красный!")
print(Fore.GREEN + "А этот текст зеленый!")
print(Back.GREEN + Fore.BLACK + "Черный текст на желтом фоне!")
print(Style.BRIGHT + "Яркий текст.")

# Стили сбрасываются автоматически благодаря autoreset=True,
# но можно вернуть стандартный вид и вручную:
print(Style.RESET_ALL + "Обычный текст.")