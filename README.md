#Log Analysis
##DESCRIPTION
For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?

##RUNNING THE PROGRAM
1.To get started, the user must use a virtual machine  on your computer. You can download **Vagrant** and **VirtualBox** to install and manage your virtual machine. Use* vagrant up* to bring the **virtual machine** online and *vagrant ssh* to **login**.

2.Download the data and Unzip the file in order to extract _newsdata.sql_. This file should be inside the Vagrant folder.

3.Load the database by using the command:* psql -d news -f newsdata.sql*.

4.Connect to the database by using the command: *psql -d news*.

5.Create the Views given below. Then exit psql.

6.Now execute the Python file - `python logs_analysis.py`


##Create The Following Views:

##View for query1:

create view newslog1_view as select title, count(*) as total from articles, log where log.path like concat('%', articles.slug, '%')  and log.status like '%200%' group by  title order by total desc;

##View for query2:


create or replace view newslog2_view as select authors.name, count(*) as total from articles inner join authors on articles.author = authors.id inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by authors.name;


##View for quer3:

create or replace view newslog3_view as select date(time) as error_date,round(100.0*sum(case log.status when'404 NOT FOUND' then 1 else 0 end)/count(log.status), 2) as error from log group by error_date;



