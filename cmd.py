from minicli import cli, run

from db import execute

IFILE = '/data/export.csv'


@cli
async def load():
    await execute('DROP TABLE IF EXISTS datasets;')
    await execute('CREATE TABLE datasets (id serial PRIMARY KEY, remote_id varchar, title varchar, description varchar, organization varchar);')
    await execute(f"COPY datasets (remote_id, title, description, organization) FROM '{IFILE}' WITH (DELIMITER ',', HEADER, FORMAT CSV);")
    await create_index()


@cli
async def create_index():
    await execute('''
CREATE INDEX idx_fts_datasets ON datasets
USING gin((setweight(to_tsvector('french', title), 'A') ||
             setweight(to_tsvector('french', description), 'B') ||
             setweight(to_tsvector('simple', organization), 'C')));
''')


if __name__ == '__main__':
    run()
