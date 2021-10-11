use journal;

INSERT INTO teachers(id, first_name, last_name, father_name, gender, experience)
VALUES (1, 'Məmməd', 'Şahmalıyev', 'Oqtay', 'male', 10) as new
ON DUPLICATE KEY UPDATE first_name=new.first_name, last_name=new.last_name, 
father_name=new.father_name, gender=new.gender, experience=new.experience;

INSERT INTO subjects(id, name, code, hours)
VALUES (1, 'Object Oriented Programming', 'OOP', 90) as new
ON DUPLICATE KEY UPDATE name=new.name, code=new.code, hours=new.hours;

INSERT INTO student_groups(id, name)
VALUES (1, '2451i') as new
ON DUPLICATE KEY UPDATE name=new.name;

INSERT INTO students(id, last_name, first_name, father_name, gender) VALUES 
(1, "HƏŞİMOV", "MUHƏMMƏD", "XƏZƏR", "male"),
(2, "HƏSƏNOVA", "ŞÜKÜFƏ", "ELÇİN", "female"),
(3, "ABASQULİZADƏ", "ƏLİ", "ELŞAD", "male"),
(4, "MƏMMƏDOV", "CAVİD", "RƏHMAN", "male"),
(5, "QURBANOV", "RÜSTƏM", "ELŞAD", "male"),
(6, "MƏMMƏDOV", "CƏLAL", "ƏHMƏD", "male"),
(7, "SADIQOV", "MURAD", "YAŞAR", "male"),
(8, "KƏRİMİ", "NİHAT", "RİZVAN", "male"),
(9, "ALLAHVERDİYEVA", "RƏKSANƏ", "MƏMMƏD", "female"),
(10, "QƏDİRLİ", "ƏZİMƏXANIM", "NƏSİMİ", "female"),
(11, "KƏRİMZADƏ", "ÇİNARƏ", "NATİQ", "male"),
(12, "BABAYEV", "MURAD", "NAMİQ", "male"),
(13, "ƏLİZADƏ", "XƏDİCƏ", "ELÇİN", "female"),
(14, "POLADZADƏ", "ƏDHƏM", "FUAD", "male"),
(15, "HƏMİDOV", "HƏMİD", "ŞAHİN", "male"),
(16, "YARMƏMMƏDOV", "RAUL", "ELÇİN", "male"),
(17, "NOVRUZLU", "YUSİF", "QURBAN", "male"),
(18, "QƏMBƏROV", "NURLAN", "RÖVŞƏN", "male"),
(19, "MƏMMƏDOV", "CAVİD", "EMİL", "male"),
(20, "MƏMMƏDOV", "DAVUD", "FUAD", "male"),
(21, "HÜSEYNOV", "ELNUR", "ELMAN", "male"),
(21, "HÜSEYNOV", "ELNUR", "ELMAN", "male"),
(22, "MİRZƏYEV", "AMAL", "AYDIN", "male"),
(23, "MAHMUDOV", "NURLAN", "XƏQANİ", "male")
as new
ON DUPLICATE KEY UPDATE first_name=new.first_name, last_name=new.last_name, 
father_name=new.father_name, gender=new.gender;


insert into students_groups(student_id, group_id)
values(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1) as new
ON DUPLICATE KEY UPDATE student_id=new.student_id;


insert into journal(id, kafedra, faculty, group_id, start_date, end_date)
values (1, 'Computer Systems and Programming', 'Aerokosmik', 1, '2024-02-15', '2024-05-31') as new
ON DUPLICATE KEY UPDATE kafedra=new.kafedra, faculty=new.faculty, group_id=new.group_id, 
start_date=new.start_date, end_date=new.end_date;
