import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriend:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email: str, password: str) -> json:
        """Вызывает метод get для получения ключа авторизации"""
        headers = {
            'email': email,
            'password': password
        }
        r = requests.get(self.base_url+'api/key', headers=headers)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result

    def get_api_list_friends(self, auth_key: str, filter: str = ''):
        """Вызывает метод get для получения списка животных"""
        headers = {'auth_key': auth_key['key']}
        params = {'filter': filter}
        r = requests.get(self.base_url+'api/pets', headers=headers, params=params)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result

    def post_api_add_new_pet(self, name, animal_type, age, pet_photo, auth_key):
        """Вызывает метод post для добавления нового питомца на сайт"""
        data = MultipartEncoder(
            fields={
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        r = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result

    def delete_api_pet(self, auth_key, id_pet):
        """Вызывает метод delete для удаления питомца по его id"""
        headers = {'auth_key': auth_key['key']}
        r = requests.delete(self.base_url+'api/pets/'+id_pet, headers=headers)
        status = r.status_code
        return status

    def put_api_upd_pet(self, name, animal_type, age, id_pet, auth_key):
        """Вызывает метод put для изменения информации о питомце"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        r = requests.put(self.base_url + 'api/pets/' + id_pet, headers=headers, data=data)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result

    def post_api_create_new_pet_with_out_photo(self, name, animal_type, age, auth_key):
        """Вызывает метод post для создания карточки питомца без фото"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        r = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result

    def post_api_add_photo_pet(self, pet_id, pet_photo, auth_key):
        """Вызывает метод post и добавляет к карточке питомца фотографию
         или заменяет ее если она существует"""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        r = requests.post(self.base_url+'api/pets/set_photo/'+pet_id, headers=headers, data=data)
        status = r.status_code
        result = None
        try:
            result = r.json()
        except:
            result = r.text
        return status, result


