import psycopg2

def execute(statement, params=tuple()):
    conn = get_conn()
    cur = conn.cursor()
    res = cur.execute(statement, params)
    conn.commit()
    cur.close()
    conn.close()
    return cur

def get_conn():
    return psycopg2.connect(dbname='datagouvfr', user='postgres', password='postgres', host='localhost')

async def search(query, connection):
    q = '''
SELECT _id, title, description, organization
FROM (SELECT remote_id as _id,
             title, SUBSTRING(description, 0, 255) as description, organization,
             setweight(to_tsvector('french', title), 'A') ||
             setweight(to_tsvector('french', description), 'B') ||
             setweight(to_tsvector('simple', organization), 'C') as document
      FROM datasets) p_search
WHERE p_search.document @@ to_tsquery('french', $1)
ORDER BY ts_rank(p_search.document, to_tsquery('french', $1)) DESC LIMIT 10;
'''
    return await connection.fetch(q, query)
