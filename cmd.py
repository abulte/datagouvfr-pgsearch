import click

from db import execute

IFILE = '/data/export.csv'

@click.group()
def cli():
    pass

@cli.command()
def load():
    execute('DROP TABLE IF EXISTS datasets;')
    execute('CREATE TABLE datasets (id serial PRIMARY KEY, remote_id varchar, title varchar, description varchar, organization varchar);')
    execute(f"COPY datasets (remote_id, title, description, organization) FROM '{IFILE}' WITH (DELIMITER ',', HEADER, FORMAT CSV);")

@cli.command()
def create_index():
    execute('''
CREATE INDEX idx_fts_datasets ON datasets
USING gin((setweight(to_tsvector('french', title), 'A') ||
             setweight(to_tsvector('french', description), 'B') ||
             setweight(to_tsvector('simple', organization), 'C')));
''')

if __name__ == '__main__':
    cli()
