from flask import *
import requests
app=Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/VxCrHkEZTv28bwZC4YD8_w"
    response = requests.get(api_url).json()
    image_url = "<img src=" + response['icon_url'] + ">"
    return "<strong>Random joke from chuck norris: </strong>" + response['value'] + image_url


if __name__=='__main__':
    app.run(debug=True)


