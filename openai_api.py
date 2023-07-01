import openai
import os
import getpass
from PIL import Image




class ChatGPT:
    def __init__(self):
        openai.api_key = open(os.environ["OPENAI_API_KEY_FILE"], "r").read()
        if openai.api_key is None:
            print("OpenAI API key is not set. Exiting...")
            exit(1)

    def __call__(self, model: str, messages: list):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages, 
            
        )
        print(messages, response, flush=True)
        return response["choices"][0]["message"]['content']
    

class DALLE:
    def __init__(self) -> None:
        openai.api_key = open(os.environ["OPENAI_API_KEY_FILE"], "r").read()
        if openai.api_key is None:
            print("OpenAI API key is not set. Exiting...")
            exit(1)

    def generate(self, prompt: str):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024",
            )
            image_url = response['data'][0]['url']
        except Exception as e:
            if isinstance(e, openai.error.InvalidRequestError):
                image_url = "https://cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg"
        print(image_url, flush=True)
        return image_url
    
    def variate(self, image):
        response = openai.Image.create_variation(
            image=image,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url