import sqlite3

with sqlite3.connect("netflix.db")  as connection:
     cursor = connection.cursor()
     query = """SELECT *(director, duration, country)
                FROM netflix
                WHERE director = 'Christopher Nolan" 
                AND duration > 110
                AND country in ("Russia","Romania")
                AND country LIKE 'R%'
                AND release_year BETWEEN 1945 AND 1950
                AND director = ''(хотим найти пустую строку) AND IS NOT NULL(когда вся строка не заполнена)
                LIMIT 10
                
                ORDER BY release_year DESC(ASC)
                LIMIT 10
                
                GROUP BY type(будет только "tv show" "series" без пвторениий)
                
                OFFSET 10"""

     cursor.execute(query)

     for row in cursor.fetchall():
          print(row)

