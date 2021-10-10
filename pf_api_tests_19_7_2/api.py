import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Апи библиотека к приложению Pet Friends"""

    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str):
        """метод, который делает запрос к api сервера и возвращает статус запроса и ответ в формате json
        с ключом пользователя, полученным по указанным значениям email и password"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = ""):
        """метод, который делает запрос к api сервера и возвращает статус запроса и ответ в формате json
        со списком питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_add_information_about_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str):
        """метод, который отправляет POST запрос на сервер с данными нового питомца и возвращает статус запроса
        и результат в формате json с информацией о добавленном питомце"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str):
        """метод отправляет запрос на сервер на удаление питомца по указанному id и возвращает статус запроса
        и результат в формате json с уведомлением об успешном удалении"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url+'api/pets/'+pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_update_information_about_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str):
        """метод отправляет запрос PUT на сервер для обновления данных питомца с указанным id и возвращает статус запроса
        и результат в формате json с измененными данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }

        res = requests.put(self.base_url+'api/pets/'+pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_add_information_about_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str):
        """метод отправляет POST запрос на сервер с данными нового питомца без фотографии и возвращает статус запроса и
        результат в формате json c информацией о новом питомце"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def post_add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str):
        """метод направляет POST запрос на добавление фотографии с указанным id питомца и возвращает статус запроса и
        результат в формате json c информацией о новом питомце"""

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
