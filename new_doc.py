def reception_triage(symptom):
   
    def surgeon(patient_name):
        return f"Хирург: экстренная операция по поводу острого живота у пациента {patient_name}"
        
    def psychiatrist(patient_name):
        return f"Психиатр: купирование острого психоза у пациента {patient_name}"
        
    def cardiologist(patient_name):
        return f"Кардиолог: экстренная терапия при инфаркте миокарда у пациента {patient_name}"
        
    def neurologist(patient_name):
        return f"Невролог: тромболизис при инсульте у пациента {patient_name}"
        
    def obstetrician(patient_name):
        return f"Акушер-гинеколог: принятие родов у пациентки {patient_name}"

    # 2. Возвращаем нужную функцию в зависимости от симптома
    if symptom == 'острый живот':
        return surgeon
    elif symptom == 'инфаркт':
        return cardiologist
    elif symptom == 'инсульт':
        return neurologist
    elif symptom == 'острый психоз':
        return psychiatrist
    elif symptom == 'роды':
        return obstetrician

symptoms_list = ['роды', 'инфаркт', 'инсульт', 'острый психоз', 'острый живот']

# Шаг А: С помощью map получаем список функций-врачей для каждого симптома
doctors_list = list(map(reception_triage, symptoms_list))

# Список имен пациентов, которые поступили вместе с симптомами
patients_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецова"]

results = []  

for i in range(len(patients_names)):
    doc = doctors_list[i]        # Берем врача по номеру i
    patient = patients_names[i]  # Берем пациента по тому же номеру i
    
    diagnosis = doc(patient)     # Врач осматривает пациента
    results.append(diagnosis)    # Записываем результат в журнал

for result in results:
    print(result)


