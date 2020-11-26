from flask import request, Flask, render_template
from services.weather_service import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html')

@app.route('/city')
def city():
    return render_template('city.html')

@app.route('/forecast/<name>')
def forecast(name):
    song = 'sunny'
    background = 'https://i.pinimg.com/originals/d1/b4/a5/d1b4a5f4125f5351197f271ba45c3954.gif'

    temp, press, humid, description = get_weather(name)
    if humid > 50 and temp <= 0:
        song = 'let_it_snow'
        background = 'https://thumbs.gfycat.com/GrandioseSameKatydid-size_restricted.gif'

    elif humid <= 50 and temp > 0:
        song = 'sunny'
        background = 'https://i.pinimg.com/originals/d1/b4/a5/d1b4a5f4125f5351197f271ba45c3954.gif'
    elif humid > 70 and temp > 0:
        song = 'its_raining_men'
        background = 'https://i.imgur.com/UhWJLex.gif'

    return render_template('forec.html', temp=temp, press=press, humid=humid, description=description, song=song, background = background)



