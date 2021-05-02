create table mother (id INTEGER, name TEXT);

create table children (name TEXT, surname TEXT, mother_id INTEGER, FOREIGN KEY(mother_id) references mother(id));

select * from children where mother_id = 1;

create table uni_students (id INTEGER, name TEXT, course INTEGER);

create table uni_professor (id INTEGER, name TEXT, subject TEXT);

create table proff_stud (student_id INTEGER, proff_id INTEGER,
FOREIGN KEY (student_id) references uni_students(id),
FOREIGN KEY (proff_id) references uni_professor(id));


insert into uni_students values (1, 'Daniiar', 3);
insert into uni_students values (2, 'Beki', 3);

insert into uni_professor values (1, 'Li Gan U', 'Vostokovedenya');
insert into uni_professor values (2, 'Kazybaev', 'Math');
insert into uni_professor values (3, 'Imtyaz Gurlbara', 'OS');

insert into proff_stud values (1, 3);
insert into proff_stud values (1, 2);


insert into proff_stud values (2, 3);
insert into proff_stud values (2, 2);
insert into proff_stud values (2, 1);

select * from proff_stud where student_id = 1;

select * from proff_stud where proff_id = 3;
