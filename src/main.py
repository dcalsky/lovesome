import os
import re
from sanic import Sanic
from sanic.response import json, html
from draw import draw
from sanic_jinja2 import SanicJinja2

static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')
templates_path = os.path.join(os.path.join(os.path.dirname(__file__), 'templates'))

app = Sanic()
jinja = SanicJinja2(app) # Use jinja2 for template engine
app.static('/static', static_path) # Images
app.static('/', templates_path)

@app.route('/')
async def test(request):
  return jinja.render('index.html')


@app.route('/draw')
async def handle(request):
  if not 'word2' in request.args or not 'word3' in request.args:
    return json({"message": "word2 and word3 must be provided!"})
  pattern = re.compile(r'^[A-Z0-9]{1}$')

  word1 = 'I' # request.args['word1'][0]
  word2 = request.args['word2'][0]
  word3 = request.args['word3'][0]
  if not pattern.match(word2) or not pattern.match(word3):
    return json({"message": "word must be an uppercase english character!"})
    
  file_path = os.path.join(static_path, word1 + word2 + word3 + '.jpg')
  if not os.path.isfile(file_path):
    draw(word1, word2, word3)
  return json({"message": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4400, workers=4)