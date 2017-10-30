use web;
create table captcha(
    id char(4) unique,
    code char(6),
    count integer,
    primary key (id)
);
