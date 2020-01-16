import asyncpg

DSN = 'postgres://postgres:postgres@localhost:5432/datagouvfr'


async def get_conn():
    return await asyncpg.connect(DSN)


async def execute(query):
    conn = await get_conn()
    await conn.execute(query)


async def search(query, connection):
    q = '''
SELECT _id, title, description, organization, nb_hits
FROM (SELECT remote_id as _id,
             title, SUBSTRING(description, 0, 255) as description, organization, nb_hits,
             setweight(to_tsvector('french', title), 'A') ||
             setweight(to_tsvector('french', description), 'B') ||
             setweight(to_tsvector('simple', organization), 'C') as document
      FROM datasets) p_search
WHERE p_search.document @@ to_tsquery('french', $1)
ORDER BY nb_hits DESC, ts_rank(p_search.document, to_tsquery('french', $1)) DESC LIMIT 10;
'''
    return await connection.fetch(q, query)
