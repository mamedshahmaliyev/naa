import random

# List of students and topics
students_name = ["HƏŞİMOV MUHƏMMƏD XƏZƏR OĞLU",
                 "HƏSƏNOVA ŞÜKÜFƏ ELÇİN QIZI",
                 "ABASQULİZADƏ ƏLİ ELŞAD OĞLU",
                 "MƏMMƏDOV CAVİD RƏHMAN",
                 "QURBANOV RÜSTƏM ELŞAD OĞLU",
                 "MƏMMƏDOV CƏLAL ƏHMƏD",
                 "SADIQOV MURAD YAŞAR OĞLU",
                 "KƏRİMİ NİHAT RİZVAN OĞLU",
                 "ALLAHVERDİYEVA RƏKSANƏ MƏMMƏD QIZI",
                 "QƏDİRLİ ƏZİMƏXANIM NƏSİMİ QIZI",
                 "KƏRİMZADƏ ÇİNARƏ NATİQ QIZI",
                 "BABAYEV MURAD NAMİQ OĞLU",
                 "ƏLİZADƏ XƏDİCƏ ELÇİN QIZI",
                 "POLADZADƏ ƏDHƏM FUAD OĞLU",
                 "HƏMİDOV HƏMİD ŞAHİN OĞLU",
                 "YARMƏMMƏDOV RAUL ELÇİN OĞLU",
                 "NOVRUZLU YUSİF QURBAN OĞLU",
                 "QƏMBƏROV NURLAN RÖVŞƏN OĞLU",
                 "MƏMMƏDOV CAVİD EMİL OĞLU",
                 "MƏMMƏDOV DAVUD FUAD OĞLU",
                 "HÜSEYNOV ELNUR ELMAN OĞLU",
                 "MİRZƏYEV AMAL AYDIN OĞLU",
                 "MAHMUDOV NURLAN XƏQANİ OĞLU"]

topics_name = ["1.Object Oriented Design – Implement Simple ATM",
               "2. Object Oriented Design – Implement Simple Library Automation System",
               "3. Object Oriented Design – Implement Simple Quiz System",
               "4. Object Oriented Design – Implement Simple Car Rental System",
               "5. Object Oriented Design – Implement Simple Hotel Booking System",
               "6. Object Oriented Design – Implement Simple Courier Delivery Management System",
               "7. Object Oriented Design – Implement Chess Game",
               "8. Object Oriented Design – Implement Event Management System",
               "9. Object Oriented Design – Implement Tic-Tac-Toe Game",
               "10. Object Oriented Design – Implement Address Book",
               "11. Object Oriented Design – Implement Medical Appointment System",
               "12. Object Oriented Design – Implement Simple Inventory Management System",
               "13. Object Oriented Design – Implement Calendar Application",
               "14. Object Oriented Design – Implement Forum Application",
               "15. Object Oriented Design – Implement Polling System",
               "16. Object Oriented Design – Implement Voting System",
               "17. Object Oriented Design – Implement Expense Tracking Application",
               "18. Object Oriented Design – Implement Recipe Organizer System",
               "19. Object Oriented Design – Implement Personal Blog Management System",
               "20. Object Oriented Design – Implement Task Management Application",
               "21. Object Oriented Design – Implement Restaurant Ordering System",
               "22. Object Oriented Design – Implement Online Auction System",
               "23. Object Oriented Design – Implement Simple Online Trading System"]

# Shuffle the list of topics to ensure randomness
random.shuffle(topics_name)

# Assign topics to students
assignments = {student: topic for student, topic in zip(students_name, topics_name)}

# Print assignments
for student, topic in assignments.items():
    print(f"{student} is assigned to {topic}")