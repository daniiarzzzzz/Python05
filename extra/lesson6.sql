create table it_students (name TEXT, surname TEXT, level INTEGER, course TEXT, id INTEGER, school_name TEXT, address TEXT, floor INTEGER, student_amount INTEGER);

insert into it_students values ('Adil', 'Huseinov', 2, 'Python', 1, 'GeekTech', 'Ibraimova 103', 4, 276);
insert into it_students values ('Sultan', 'Kelsinbekov', 2, 'Python', 2, 'Makers', 'Ibraimova 104', 1, 240);
insert into it_students values ('Kairat', 'Israilov', 2, 'Python', 3, 'GeekTech', 'Ibraimova 103', 4, 276);

create table it_school (id INTEGER, name TEXT, address TEXT, floor INTEGER, student_amount INTEGER);

create table it_students2 (name TEXT, surname TEXT, level INTEGER, course TEXT, id INTEGER, school_id INTEGER, FOREIGN KEY(school_id) references it_school(id));

insert into it_school values (1, 'GeekTech', 'Ibraimova 103', 4, 276);
insert into it_school values (2, 'Makers', 'Ibraimova 104', 1, 240);

insert into it_students2 values ('Adil', 'Huseinov', 2, 'Python', 1, 1);
insert into it_students2 values ('Sultan', 'Kelsinbekov', 2, 'Python', 2, 2);
insert into it_students2 values ('Kairat', 'Israilov', 2, 'Python', 3, 1);

select name, surname, school_id from it_students2;

select * from it_school where id = 1;
select * from it_school where id = 2;
