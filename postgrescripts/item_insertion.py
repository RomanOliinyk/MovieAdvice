import psycopg2
import csv

def load_file(filename):
    results = []
    with open(filename) as csvfile:
        inputfile = csv.reader(csvfile, delimiter=';')
        for row in inputfile:
            results.append(row)

    #results_new = []
    #for item in results:
        #new_item = list(map(int, item))
        #results_new.append(new_item)

    #print (results[0])
    return results

#load_file('movie_crew.csv')

def table_insert():
    data = load_file('movie_crew.csv')

    for item in data:
        conn = psycopg2.connect("dbname=Movie_Advice user=RomanOliinyk")
        cur = conn.cursor()

        row_id = int(item[4])
        department = item[2]
        job = item[3]
        movie_id = int(item[0])
        person_id = int(item[1])

        SQL = """INSERT INTO "Movie_Advice_schema".recommendation_moviecrew(
            id, department, job, movie_id, person_id)
            VALUES (%s, %s, %s, %s, %s);"""
        data1 = (row_id, department, job, movie_id, person_id)
        #print (data1)
        #break

        try:
            cur.execute(SQL, data1)
            conn.commit()
            print (row_id)
        except:
            print ('Error')

    conn.commit()
    cur.close()
    conn.close()

table_insert()
