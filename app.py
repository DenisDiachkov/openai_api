from flask import Flask, send_file, Response, request
from io import BytesIO
from PIL import Image
from openai_api import ChatGPT, DALLE
import os
import requests


app = Flask(__name__)
def openai_authentification():
    global chatgpt_api
    global dalle_api
    chatgpt_api = ChatGPT()
    dalle_api = DALLE()


@app.route('/chat', methods=['POST'])
def chatgpt():
    global chatgpt_api
    json = request.get_json()
    model = json['model']
    messages = json['messages']
    answer = chatgpt_api(
        model=model,
        messages=messages
    )
    return Response(
        answer,
        mimetype='text/html',
    )


@app.route('/dalle', methods=['POST'])
def dalle():
    global dalle_api
    json = request.get_json()
    action = json['action']
    if action == 'generate':
        prompt = json['prompt']
        response = dalle_api.generate(prompt=prompt)
    elif action == 'variate':
        image_url = json['image_url']
        
        img = BytesIO(requests.get(image_url).content)
        image = Image.open(img)
        png_image = BytesIO()
        image.save(png_image, "PNG")

        response = dalle_api.variate(image=png_image.getvalue())
    img = BytesIO(requests.get(response).content)
    print(response)
    return Response(
        img.getvalue(), 
        mimetype='image/png',
    )


@app.route('/', methods=['GET'])
def GUI():
    return open('./gui.html').read()



if __name__ == '__main__':
    openai_authentification()
    app.run(
        host="0.0.0.0",
        port=os.environ.get("FLASK_PORT", "5000"),
    )