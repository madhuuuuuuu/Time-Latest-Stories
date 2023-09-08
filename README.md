# Time-Latest-Stories
To create a custom API that scrapes the latest 6 stories from Time.com and to print them will involve a few steps. This code is in python script.

STEP 1 : Install Dependencies

To install necessary dependencies.

>>pip install requests beautifulsoup4 Flask

STEP 2 : Create the python script with the code.
```
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get_latest_stories', methods=['GET'])
def get_latest_stories():
    try:
        url = 'https://time.com/'
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            story_elements = soup.find_all('li', class_='latest-stories__item')
            
            stories = []
            
            for story in story_elements[:6]:
                title = story.text.strip()
                link = story.find('a')['href']
                stories.append({'Title': title, 'Link': link})
    
            return jsonify({'stories': stories})
        else:
            return jsonify({'error': 'Failed to fetch data from Time.com'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
STEP 3 : Save the script and run it

API will be available at http://localhost:5000/get_latest_stories. We can deploy it to a server.

STEP 4 : Access the API

We can make a GET request to http://localhost:5000/get_latest_stories, and it will return the latest 6 stories from Time.com in JSON format.



![Time-Latest-Stories](https://github.com/madhuuuuuuu/Time-Latest-Stories/assets/95408668/0fa0e126-0377-4bda-bc49-b3d7c3384d9f)
