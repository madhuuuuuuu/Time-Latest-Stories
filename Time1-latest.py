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
