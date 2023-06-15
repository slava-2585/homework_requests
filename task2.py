import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, save_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={save_file}&overwrite=True'
        
        response = requests.get(url, headers=headers)
        if 200 <= response.status_code < 300:
            with open(file_path, 'rb') as f:
                try:
                    res = requests.put(response.json().get('href', ''), files={'file':f})
                    if 200 <= res.status_code < 300:
                        print(f'Картинка {path_to_file} загружена в {save_file}')
                except KeyError:
                    print(response)
        


if __name__ == '__main__':
    path_to_file = 'cats.jpeg'
    save_file = 'img/cats.jpeg'
    token = "y0_AgAAAAANf0P9AADLWwAAAADk5grpfuq0wLlRQHqNpacM5gL7bQWVMrk"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, save_file)