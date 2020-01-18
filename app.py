import time
import asyncpg

from quart import Quart, jsonify, request, current_app, render_template
from db import search, DSN

app = Quart(__name__ , static_url_path='', static_folder='static/dist')

# TODO file based config
app.debug = True
if app.debug:
    # disable cache for static file when debugging
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
async def index():
    return await render_template('index.html')


@app.route('/api')
async def api():
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
    app.run(use_reloader=True)
