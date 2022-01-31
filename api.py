import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def decor_log(func):

    def wrapper(self, *args, **kwargs):
        set = func(self, *args, **kwargs)
        with open('log.txt', 'a', encoding='utf8') as file:
            file.write(f'\n--{func.__name__}--\n')
            try:
                if "headers" != False:
                    file.write(f'Headers - {str(self.headers)}\n')
            except AttributeError:
                headers = None
            try:
                if "params" != False:
                    file.write(f'Params - {str(self.params)}\n')
            except AttributeError:
                params = None
            try:
                if "data" != False:
                    file.write(f'Data - {str(self.data)}\n')
            except AttributeError:
                data = None
            try:
                if "result" != False:
                    file.write(f'Body requests - {str(self.result)}\n')
            except AttributeError:
                data = None
            file.write(str(f"Status - {self.status}\n"))
        return set

    return wrapper


class PetFriend:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    @decor_log
    def get_api_key(self, email: str, password: str) -> json:
        """Вызывает метод get для получения ключа авторизации"""
        headers = self.headers = {
            'email': email,
            'password': password
        }
        r = requests.get(self.base_url+'api/key', headers=headers)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result

    @decor_log
    def get_api_list_friends(self, auth_key: str, filter: str = ''):
        """Вызывает метод get для получения списка животных"""
        headers = self.headers = {'auth_key': auth_key['key']}
        params = self.params = {'filter': filter}
        r = requests.get(self.base_url+'api/pets', headers=headers, params=params)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result

    @decor_log
    def post_api_add_new_pet(self, name, animal_type, age, pet_photo, auth_key):
        """Вызывает метод post для добавления нового питомца на сайт"""
        data = self.data = MultipartEncoder(
            fields={
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
        headers = self.headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        r = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result

    @decor_log
    def delete_api_pet(self, auth_key, id_pet):
        """Вызывает метод delete для удаления питомца по его id"""
        headers = self.headers = {'auth_key': auth_key['key']}
        r = requests.delete(self.base_url+'api/pets/'+id_pet, headers=headers)
        status = self.status = r.status_code
        return status

    @decor_log
    def put_api_upd_pet(self, name, animal_type, age, id_pet, auth_key):
        """Вызывает метод put для изменения информации о питомце"""
        data = self.data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = self.headers = {'auth_key': auth_key['key']}
        r = requests.put(self.base_url + 'api/pets/' + id_pet, headers=headers, data=data)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result

    @decor_log
    def post_api_create_new_pet_with_out_photo(self, name, animal_type, age, auth_key):
        """Вызывает метод post для создания карточки питомца без фото"""
        data = self.data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = self.headers = {'auth_key': auth_key['key']}
        r = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result

    @decor_log
    def post_api_add_new_pet_simple(self, name, animal_type, age, auth_key):
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
   запроса и результат в формате JSON с данными добавленного питомца"""
        data = self.data = MultipartEncoder(fields={
            'name': name,
            'animal_type': animal_type,
            'age': age
        })
        headers = self.headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        r = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result


    @decor_log
    def post_api_add_photo_pet(self, pet_id, pet_photo, auth_key):
        """Вызывает метод post и добавляет к карточке питомца фотографию
         или заменяет ее если она существует"""
        data = self.data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = self.headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        r = requests.post(self.base_url+'api/pets/set_photo/'+pet_id, headers=headers, data=data)
        status = self.status = r.status_code
        result = None
        try:
            result = self.result = r.json()
        except:
            result = self.result = r.text
        return status, result


# pt = PetFriend()
# pt.get_api_key('kuznetsov_alex95@mail.ru', '1234')
