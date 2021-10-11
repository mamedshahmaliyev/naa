
-- CREATE UNIQUE INDEX idx_group_id_unique ON journals(group_id);
-- ALTER TABLE subjects ADD COLUMN credit INTEGER;

create table journals (
    id INTEGER PRIMARY KEY,
    group_id TEXT NOT NULL UNIQUE,
    faculty TEXT NOT NULL
);
create table subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hours INTEGER
    credit INTEGER
);
create table students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronym TEXT
);
create table journal_records (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    record_type TEXT NOT NULL,
    date TEXT NOT NULL,
    class_number INTEGER NOT NULL,
    mark INTEGER,
    present_hours INTEGER
);