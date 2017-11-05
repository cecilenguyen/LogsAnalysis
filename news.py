import psycopg2

# set name of database to connect to
DBNAME = "news"


# connects to database and queries db
def get_query(query):
    # return all items from the database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    items = c.fetchall()
    db.close()
    return items


# format printing of queries 1 and 2
def print_query(result):
    for col in result:
        print(str(col[0]) + ' - ' + str(col[1]) + ' views')


# format printing of query 3
def print_err_query(result):
    for col in result:
        print(str(col[0]) + ' - ' + str(col[1]) + '%')


# SQL query for most popular three articles of all time
query1 = '''select articles.title, count(*) as num
    from articles join log on log.path like concat('%',articles.slug)
    group by articles.title, log.path
    order by num desc
    limit 3;'''

# SQL query for most popular article authors of all time
query2 = '''select authors.name, count(*) as num
    from articles join authors
    on articles.author = authors.id
    join log on log.path like concat('%', articles.slug)
    group by authors.name
    order by num desc;'''

# SQL query for which days more than 1% of requests lead to errors
query3 = '''select day,
    cast(round(error/cast(total as decimal)*100, 2) as decimal(10,2))
    from (select cast(time as date) as day,
    count(*) as total,
    count(case when status like '404%' then 1 end) as error
    from log
    group by day) as errorRatio
    where error/cast(total as decimal)*100 > 1;'''

# call functions for each query and prints to console
query1result = get_query(query1)
print('What are the most popular three articles of all time?')
print_query(query1result)
print()

query2result = get_query(query2)
print('Who are the most popular article authors of all time?')
print_query(query2result)
print()

query3result = get_query(query3)
print('On which days did more than 1% of requests lead to errors?')
print_err_query(query3result)
print()
