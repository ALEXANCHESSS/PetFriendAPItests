from api import PetFriend
from setting import *


class TestPetFriends:
    def setup(self):
        self.pf = PetFriend()

    def test_post_api_create_new_pet_with_out_photo_correct(self):
        """Тестирование корректной работы функции создания нового питомца без изображения"""
        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_create_new_pet_with_out_photo(name_pet, type_pet, age_pet, auth_key)
        assert status == 200
        assert 'id' in result

    def test_post_api_add_photo_pet(self):
        """Тестирование функции добавления фотографии или ее замены к существующей карточки питомца"""
        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        _, list_my_pet = self.pf.get_api_list_friends(auth_key, 'my_pets')
        if len(list_my_pet['pets']) == 0:
            _, id_pet = self.pf.post_api_create_new_pet_with_out_photo(name_pet, type_pet, age_pet, auth_key)
            status, result = self.pf.post_api_add_photo_pet(id_pet['id'], pets_photo, auth_key)
            assert status == 200
            assert id_pet['id'] == result['id']
        else:
            status, result = self.pf.post_api_add_photo_pet(list_my_pet['pets'][0]['id'], pets_photo, auth_key)
            assert status == 200
            assert list_my_pet['pets'][0]['id'] == result['id']

    def test_get_api_key_for_not_valid_user(self, email=email_correct):
        """Тест на вход в систему с помощью невалидных данных"""
        status, result = self.pf.get_api_key(email, '0000')
        with open('log.txt', 'w') as file:
            file.write(str(result))
        assert status == 200
        assert 'key' in result

    def test_get_api_list_pets_not_valid_user(self, filter='my_pets'):
        """Тестирование возможности просмотреть список 'мои питомцы' использовав невалидные данные для входа"""
        _, auth_key = self.pf.get_api_key(email_correct, '0000')
        if auth_key == dict:
            status, result = self.pf.get_api_list_friends(auth_key, filter)
            with open('log.txt', 'w', encoding='utf8') as file:
                file.write(str(result))
            assert status == 200
            assert len(result['pets']) > 0
        else:
            raise Exception("API key not found")

    def test_post_api_add_new_pet_photo_pdf(self, name=name_pet, animal_type=type_pet,
                                          age=age_pet, pet_photo=pets_photo_pdf):
        """Тестирование возможности добавить нового питомца с использованием изображения в формате .pdf"""

        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
        with open('log.txt', 'w', encoding='utf8') as file:
            file.write(str(result))
        assert status == 200
        assert result['age'] == age

    def test_post_api_add_new_pet_age_str(self, name=name_pet, animal_type=type_pet,
                                          age='age_pet', pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, используя в качестве значения возраста строку"""

        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
        with open('log.txt', 'w', encoding='utf8') as file:
            file.write(str(result))
        assert status == 200
        assert result['age'] == age

    def test_post_api_add_new_pet_noname(self, name='', animal_type=type_pet,
                                          age=age_pet, pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, оставив значение 'имя' пустым"""

        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
        with open('log.txt', 'w', encoding='utf8') as file:
            file.write(str(result))
        assert status == 200
        assert result['name'] == name

    def test_post_api_add_new_pet_no_animal_type(self, name=name_pet, animal_type='',
                                          age=age_pet, pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, оставив значение 'порода' пустым"""

        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
        with open('log.txt', 'w', encoding='utf8') as file:
            file.write(str(result))
        assert status == 200
        assert result['animal_type'] == animal_type

    def test_post_api_add_new_pet_no_age(self, name=name_pet, animal_type=type_pet,
                                          age='', pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, оставив значение 'возраст' пустым"""

        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
        with open('log.txt', 'w', encoding='utf8') as file:
            file.write(str(result))
        assert status == 200
        assert result['age'] == age

    def test_delete_pets_correct(self):
        """Тестирование возможности удалить карточку питомца без API key"""
        _, auth_key = self.pf.get_api_key(email_correct, password_correct)
        _, list_my_pet = self.pf.get_api_list_friends(auth_key, '')
        status = self.pf.delete_api_pet({"key": ''}, list_my_pet['pets'][0]['id'])
        assert status == 200




    # def test_get_api_key_for_valid_user(self, email=email_correct, password=password_correct):
    #     status, result = self.pf.get_api_key(email, password)
    #     assert status == 200
    #     assert 'key' in result
    #
    # def test_get_api_list_pets_correct(self, filter=''):
    #     _, auth_key = self.pf.get_api_key(email_correct, password_correct)
    #     status, result = self.pf.get_api_list_friends(auth_key, filter)
    #     assert status == 200
    #     assert len(result['pets']) > 0
    # #
    # def test_post_api_add_new_pet_correct(self, name=name_pet, animal_type=type_pet, age=age_pet, pet_photo=pets_photo):
    #     _, auth_key = self.pf.get_api_key(email_correct, password_correct)
    #     status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
    #     assert status == 200
    #     assert result['age'] == age
    #
    # def test_delete_pets_correct(self):
    #     _, auth_key = self.pf.get_api_key(email_correct, password_correct)
    #     _, result = self.pf.post_api_add_new_pet(name_pet, type_pet, age_pet, pets_photo, auth_key)
    #     id_pet = result['id']
    #     status = self.pf.delete_api_pet(auth_key, id_pet)
    #     assert status == 200
    #
    # def test_put_upd_pet_correct(self, name=name_pet, animal_type=type_pet, age=age_pet, pet_photo=pets_photo):
    #     _, auth_key = self.pf.get_api_key(email_correct, password_correct)
    #     _, result_post = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, auth_key)
    #     status, result_put = self.pf.put_api_upd_pet(dict_for_put['name_pet'],
    #                                                  dict_for_put['type_pet'], dict_for_put['age_pet'],
    #                                                  result_post['id'], auth_key)
    #     assert status == 200
    #     assert result_put['name'] == dict_for_put['name_pet']
    #     assert result_put['animal_type'] == dict_for_put['type_pet']
    #     assert result_put['age'] == dict_for_put['age_pet']


