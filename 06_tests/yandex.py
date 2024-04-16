import requests
from fake_headers import Headers


def create_headers():
    def read_config(config_file):
        with open(config_file) as file:
            return dict(eval(file.read()))

    return Headers(browser="chrome", os="win").generate() | read_config('config.json')


def create_folder(folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = create_headers()
    params = {"path": folder_name}
    req = requests.put(url, headers=headers, params=params)
    return req.status_code


def delete_folder(folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = create_headers()
    params = {"path": folder_name}
    req = requests.delete(url, headers=headers, params=params)
    return req.status_code


if __name__ == '__main__':
    print(create_headers())
    status = create_folder('test_folder')
    print(status)
    status = delete_folder('test_folder')
    print(status)