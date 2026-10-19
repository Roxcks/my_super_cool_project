names = ["Анна", "Борис", "Влад", "Глеб", "Дарья"]
departments = ["IT", "HR", "IT", "Маркетинг", "HR"]
salaries = [45000, 65000, 80000, 40000, 52000]
d = [{department:{name: salary}} for department, name, salary in zip(departments, names, salaries) if salary > 50000]
print(d)