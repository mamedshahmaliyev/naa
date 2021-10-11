
import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(host="localhost", user="root", password="", database="population")
crs = conn.cursor(dictionary=True)

persons = []


fake = Faker()

for i in range(10**7):
    first_name = fake.first_name()
    last_name = fake.last_name()
    father_name = fake.first_name_male()
    
    start_datetime = datetime.strptime('1950-01-01', '%Y-%m-%d')
    end_datetime = datetime.strptime('2024-12-31', '%Y-%m-%d')
    delta = end_datetime - start_datetime
    random_days = random.randint(0, delta.days)
    birthdate = start_datetime + timedelta(days=random_days)
    
    current_date = datetime.now()
    age = current_date.year - birthdate.year
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    gender = random.choice(['male', 'female'])
    
    persons.append((first_name, last_name, father_name, birthdate, age, gender))
    
    if len(persons) == 10000:
        print('inserting record', i)
        sql = '''insert into population (first_name, last_name, father_name, birthdate, age, gender) 
                values  (%s, %s, %s, %s, %s, %s)'''
        crs.executemany(sql, persons)
        persons = []
        conn.commit()

sql = 'select * from population order by rand() limit 10'
crs.execute(sql)
rows = crs.fetchall()

for row in rows:
    print(row['first_name'], row['id'])
    
sql = 'select count(*) from population'
crs.execute(sql)
print(crs.fetchall())
    

    