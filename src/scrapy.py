import requests


class ScrapyData():
    def __init__(self):
        self.header = {
            'user-agente': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0\
                Safari/537.36'
        }

    def get_data(self, url):
        print(f'Conectando ao site {url}...')
        response = requests.get(url, self.header)
        while response.status_code != 200:
            response = requests.get(url, self.header)
        return response.content
