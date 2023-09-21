import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['your_login'], 'password': data['your_password']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def post_title():
    return 'Мои мечты'


# Фикстура для создания нового поста
@pytest.fixture()
def new_post_data():
    return data['new_post']
