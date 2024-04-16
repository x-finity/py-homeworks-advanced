import requests
from fake_headers import Headers


def create_headers(config_file='config.json'):
    def read_config(conf=config_file):
        with open(conf) as file:
            return dict(eval(file.read()))

    return Headers(browser="chrome", os="win").generate() | read_config(config_file)


def create_folder(folder_name, url, headers=None, params=None):
    if params is None:
        params = {"path": folder_name}
    response = requests.put(url, headers=headers, params=params)
    return response


def delete_folder(folder_name, url, headers=None):
    params = {"path": folder_name}
    response = requests.delete(url, headers=headers, params=params)
    return response


def get_folder_info(folder_name, url, headers=None):
    params = {"path": folder_name}
    response = requests.get(url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    # print(create_headers())
    # status = create_folder('test_folder', create_headers())
    # print(status)
    # status = delete_folder('test_folder', create_headers())
    # print(status)
    resp = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=create_headers(), params={
        'Content-Type': '123', 'path': 'test_folder'})
    print(resp.status_code)