use web;
create table images(
    id varchar(32) unique,
    name varchar(255),
    path varchar(255),
    ctime timestamp,
    primary key (id)
);
