#!usr/bin/env python
import psycopg2


# Establishes a Connection to the database
def connect_db(db_name="news"):
    try:
        con = psycopg2.connect("dbname={}".format(db_name))
        curr = con.cursor()
        return con, curr
    except Exception:
        print("Failed to connect to the database")


# Gets Disconnected from the database
def disconnect_db(curr, con):
    curr.close()
    con.close()

# Query1
heading1 = ("The most popular 3 articles of all the time")
# Solution for the Query1
query1 = ("select * from newslog1_view limit 3")

# Query2
heading2 = ("The most popular article authors of all the time")
# Solution for the Query2
query2 = ("select * from newslog2_view order by total desc")
# Query3
heading3 = ("Errors On which days more than 1% of requests lead to errors?")
# Solution for the Query3
query3 = ("select error_date, error from newslog3_view where error >1")
'''
connects with database...
Executes queries and displays the results.......
'''


def execute_query(query):
    con, curr = connect_db()
    curr.execute(query)
    result = curr.fetchall()
    disconnect_db(con, curr)
    return result


# Prints the query result to the console...
def display_result(results, heading):
    style(heading)
    for index, result in enumerate(results):
        print(str(index+1)+"."+str(result[0])+"\t--"+str(result[1])+" views")


# Prints the query result for the third Query to the console
def display_error_result(results, heading):
    style(heading)
    for index, result in enumerate(results):
        print(str(index+1)+"."+str(result[0])+"\t--"+str(result[1])+"%errors")


# Formats the title/Query(capitalizes and add styles)
def style(heading):
    h = heading.upper()
    top = "~" * 80
    print("\n\n"+top+"\n"+h+"\n"+top)
    return top


if __name__ == '__main__':
    # Get query results
    sol1 = execute_query(query1)
    sol2 = execute_query(query2)
    sol3 = execute_query(query3)
    # Print query results
    display_result(sol1, heading1)
    display_result(sol2, heading2)
    display_error_result(sol3, heading3)
