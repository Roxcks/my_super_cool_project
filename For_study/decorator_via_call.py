import functools
from time import perf_counter, sleep
class FunctionAudit:
    def __init__(self, func,):
        self.func = func
        functools.update_wrapper(self, func)
        # для того, чтобы, когда функция превратится в экземпляр класса,
        # не теряла своё имя и документацию
        self.call_count = 0
        self.inner_stats = {"operation_time": [], 
                        "imported_args": [], 
                        "result": [],
                        "errors": []}
        
    def __call__(self, *args):
        self.call_count += 1 
        start_time = perf_counter()
        try:
            result = self.func(*args)
            end_time = perf_counter()
            duration = end_time - start_time

            self.inner_stats['operation_time'].append(duration)
            self.inner_stats['imported_args'].append(args)
            self.inner_stats['result'].append(result)
            self.inner_stats['errors'].append(None)
            return result
        
        except Exception as e:
            end_time = perf_counter()
            # фиксируем время работы программы до поломки
            duration = end_time - start_time
            self.inner_stats["operation_time"].append(duration)
            self.inner_stats["imported_args"].append((args))
            self.inner_stats["result"].append(None)
            self.inner_stats["errors"].append(str(e))
            # пишем всё то же самое, только для ошибки и добавляем текст ошибки
            raise e
    def get_stats(self):
        errors_list = self.inner_stats['errors']   
        success_count = sum(1 for err in errors_list if err is None) 
        errors_count = sum(1 for err in errors_list if err is not None)
        total_time = sum(self.inner_stats["operation_time"])
        avg_time = total_time / self.call_count if self.call_count > 0 else 0

        return {
            "total_calls": self.call_count,
            "successful_calls": success_count,
            "failed_calls": errors_count,
            "average_time_sec": round(avg_time, 5)
        }
    
    def print_report(self): # функция для красивого вывода статистики
        stats = self.get_stats()
        print("=" * 40)
        print(f"📊 ОТЧЕТ АУДИТА ФУНКЦИИ: {self.func.__name__}")
        print("=" * 40)
        print(f"📞 Всего вызовов:       {stats['total_calls']}")
        print(f"✅ Успешных вызовов:   {stats['successful_calls']}")
        print(f"❌ Ошибок:             {stats['failed_calls']}")
        print(f"⏱️ Среднее время:      {stats['average_time_sec']} сек.")
        print("=" * 40)

    def clear_history(self):
        self.call_count = 0
        self.inner_stats = {
            "operation_time": [], 
            "imported_args": [], 
            "result": [],
            "errors": []
        }

@FunctionAudit
def heavy_calculation(x, y):
    sleep(0.05)
    if x < 0:
        raise ValueError("Число не может быть отрицательным!")
    return x ** y

# 1. Успешные вызовы
print(heavy_calculation(2, 3))  # 8
print(heavy_calculation(3, 2))  # 9
print(heavy_calculation(5, 8))

# 2. Вызов с ошибкой
try:
    heavy_calculation(-1, 5)
except ValueError as e:
    print(f"Поймали ошибку: {e}")

# 3. Смотрим собранную статистику
print(heavy_calculation.print_report())    