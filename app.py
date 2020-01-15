import time

from quart import Quart, jsonify, request
from db import search

app = Quart(__name__)
app.DEBUG = True

@app.route('/')
async def index():
    query = request.args.get('q')
    if not query:
        return jsonify({})
    start = time.time()
    res = search(query)
    return jsonify({
        'time': time.time() - start,
        'data': res
    })

app.run()
