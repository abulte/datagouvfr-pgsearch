import asyncpg
import httpx

from minicli import cli, run
from progressist import ProgressBar

from db import execute, get_conn

IFILE = '/data/export.csv'


@cli
async def load():
    await execute('DROP TABLE IF EXISTS datasets;')
    await execute('''
    CREATE TABLE datasets (
        id serial PRIMARY KEY,
        remote_id varchar,
        title varchar,
        description varchar,
        organization varchar,
        nb_hits int default 0,
        url varchar
    );''')
    await execute(f'''
    COPY datasets (remote_id, title, url, description, organization)
    FROM '{IFILE}' WITH (DELIMITER ',', HEADER, FORMAT CSV);
    ''')
    await create_index()


@cli
async def create_index():
    await execute('''
CREATE INDEX idx_fts_datasets ON datasets
USING gin((setweight(to_tsvector('french', title), 'A') ||
             setweight(to_tsvector('french', description), 'B') ||
             setweight(to_tsvector('simple', organization), 'C')));
''')


async def fetch_stats_for(url):
    async with httpx.AsyncClient(base_url='https://stats.data.gouv.fr') as client:
        params = {
            'idSite': 109,
            'module': 'API',
            'method': 'Actions.getPageUrl',
            'pageUrl': url,
            'format': 'json',
            'period': 'year',
            'date': 'last1',
        }
        try:
            response = await client.get('/', params=params, timeout=10)
        except httpx.exceptions.ReadTimeout:
            print(f'Timeout from {client.base_url}{url}')
            return {}
        return response.json()


@cli
async def fetch_stats():
    conn = await get_conn()
    rows = await conn.fetch('SELECT id, url FROM datasets;')
    bar = ProgressBar(total=len(rows))
    for row in bar.iter(rows):
        stats = await fetch_stats_for(row['url'])
        if stats.get('2020'):
            await conn.execute(
                'UPDATE datasets SET nb_hits = $1 WHERE id = $2',
                stats['2020'][0]['nb_hits'],
                row['id']
            )


if __name__ == '__main__':
    run()
