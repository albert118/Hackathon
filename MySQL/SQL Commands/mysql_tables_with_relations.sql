
create table yearly_aggregate_users (
	line_id smallint(5) not null primary key auto_increment,
	line_val varchar(30) not null,
	cardtype varchar(50) not null,
	year_aggregate_vals int,
	year_val int
);

create table population_predictions (
	district_id smallint(5) not null primary key auto_increment,
	district varchar(20) not null,
	year_val int not null,
	pop_prediction int
);

create table station_yearly_aggregates ( 
	station_id smallint(5) not null primary key auto_increment,
	station varchar(35) not null,
	year_val float,
	entries_1 float,
	entries_2 float,
	entries_3 float,
	entries_4 float,
	exits_1 float,
	exits_2 float,
	exits_3 float,
	exits_4 float,
	entries_daily_avg float,
	exits_daily_avg float
);

create table station_line (
	line_id smallint(5) primary key not null auto_increment,
	station_id smallint(5) not null,
	foreign key fk_yearly(line_id)
	references yearly_aggregate_users(line_id)
	on update cascade
	on delete restrict
);

create table station_district (
	station_id smallint(5) primary key not null auto_increment,
	district_id smallint(5)  not null,
	foreign key fk_pop(district_id)
	references population_predictions(district_id)
	on update cascade
	on delete restrict
);

