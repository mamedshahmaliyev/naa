
-- SQLite DDL
create table authors (
    id INTEGER,
    name TEXT,
    surname TEXT
);
create table books (
    id INTEGER,
    title TEXT,
    author_id INTEGER
);
create table publishers (
    id INTEGER,
    title TEXT
);




-- SQLite DML

insert into authors(id, name, surname)
values (2, 'Nizami', 'Ganjavi');

select books.title,
       authors.name,
       authors.surname 
from books
left join authors on books.author_id = authors.id
;

delete from authors where id = 2;

update authors set name = 'Ahmad'
where id = 1;


insert into books(id, title, author_id)
values (1, '7 Gozel', 2);

delete from books where id = 1;



