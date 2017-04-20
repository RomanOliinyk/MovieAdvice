import psycopg2

def count_insert():
    conn = psycopg2.connect("dbname=Movie_Advice user=RomanOliinyk")
    cur = conn.cursor()

    keywords = []
    SQL = """ SELECT keyword_id
        FROM "Movie_Advice_schema".recommendation_keyword """
    cur.execute(SQL)
    rows = cur.fetchall()
    for row in rows:
        keywords.append(row[0])

    print (len(keywords))
    keywords_count = []
    for keyword in keywords:
        SQL = """SELECT COUNT(*)
            FROM "Movie_Advice_schema".recommendation_moviekeyword
            WHERE keyword_id = {};""".format(keyword)
        cur.execute(SQL)
        rows = cur.fetchall()
        keywords_count.append(rows[0][0])

    print (len(keywords_count))
    #print (keywords_count)
    id = 0
    for keyword in keywords:
        count = keywords_count[id]
        id += 1
        print (id)
        SQL = """INSERT INTO
            "Movie_Advice_schema".recommendation_moviekeywordcount
            (id, count, keyword_id)
            VALUES (%s, %s, %s);"""
        data = (id, count, keyword)
        cur.execute(SQL, data)
        conn.commit()

    conn.commit()
    cur.close()
    conn.close()


count_insert()
