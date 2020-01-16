import time
import asyncpg

from quart import Quart, jsonify, request, current_app
from db import search, DSN

app = Quart(__name__)
app.DEBUG = True


@app.route('/')
async def index():
    query = request.args.get('q')
    if not query:
        return jsonify({})
    start = time.time()
    async with current_app.pool.acquire() as connection:
        res = await search(query, connection)
    return jsonify({
        'time': time.time() - start,
        'data': [{k: v for (k,v) in r.items()} for r in res]
    })


@app.before_first_request
async def create_db():
    app.pool = await asyncpg.create_pool(DSN, max_size=20)


if __name__ == '__main__':
    app.run()
