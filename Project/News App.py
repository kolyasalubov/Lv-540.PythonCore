from flask import Flask
from flask import render_template
from flask import request
import requests 

url = 'https://newsapi.org/v2/everything?'

class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)

app = Flask(__name__)

@app.route ('/', methods=['GET', 'POST'])
def show_results():
    topic = ''
    if request.method == 'POST':
        topic = request.form['tag']
        
    list_result = create_list(topic)

    return render_template('page.html', context = list_result)

def create_list(topic):
    
    title = []
    description = []
    img = []
    source = []
    link = []
    
    parameters = {
        'qInTitle': topic,
        'pageSize': 10,
        'from': '2020-11-12',
        'language': 'en',
        'sortby': 'publishedAt',
        'apiKey': '81ec34d373c746f5b03ec1745410ee60'
    }

    number_of_errors = None
    try:
        response = requests.get(url, params=parameters)
        response_json = response.json()
        if response_json['status'] == 'error':
            raise CustomError('The scope of your search is too broad, select more specific topic. Or you have made too many requests recently. Developer accounts are limited to 100 requests over a 24 hour period.')
        if response_json['totalResults'] == 0:
            raise CustomError('There are no results for the selected topic')
    except CustomError as e:
        print("We obtain error:", e.data)
    except ValueError:
        print('There is an JSONDecodeError. Decoding JSON has failed.')
    except requests.exceptions.ConnectionError:
        print('There is an Connection error. Connection refused, please check url.')
    else:
        number_of_errors = 0


    if number_of_errors == 0:

        numer_news_will_appear = min (parameters["pageSize"], response_json['totalResults'])
        for i in range(numer_news_will_appear):

            article = response_json['articles'][i]

            title.append(article['title'])
            description.append(article['description'])
            img.append(article['urlToImage'])
            source.append(article['source']['name'])
            link.append(article['url'])
            
        list_result = zip(title, description, img, source, link)
        return list_result

    else:
        return []

if __name__ == "__main__":
    app.run()

    
