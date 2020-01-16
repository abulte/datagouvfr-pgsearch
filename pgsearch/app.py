import time
import asyncpg

from roll import Roll

from db import search, DSN

app = Roll()


@app.route('/')
async def index(request, response):
    query = request.query.get('q')
    if not query:
        response.json = {}
        return
    start = time.time()
    async with app.pool.acquire() as connection:
        res = await search(query, connection)
    response.json = {
        'time': time.time() - start,
        'data': [{k: v for (k,v) in r.items()} for r in res]
    }


@app.listen('startup')
async def create_db():
    app.pool = await asyncpg.create_pool(DSN, max_size=20)
