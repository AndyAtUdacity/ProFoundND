drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title text not null,
	description text not null
);

drop table if exists lessons;
create table lessons (
	id integer primary key autoincrement,
	title text not null
);

create table entries_in_lesons (
	id integer primary key autoincrement,
	entry
)