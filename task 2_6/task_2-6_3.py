donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor == "I" or donor == patient or \
   (donor == "II" and (patient == "II" or patient == "IV")) or \
   (donor == "III" and (patient == "III" or patient == "IV")) or \
   (donor == "IV" and patient == "IV"):
    print(f"Переливание крови {donor} группы пациенту с {patient} группой ВОЗМОЖНО")
else:
    print(f"Переливание крови {donor} группы пациенту с {patient} группой НЕВОЗМОЖНО")