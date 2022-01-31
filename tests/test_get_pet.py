from api import PetFriend
from setting import *
import pytest


# def is_age_valid(age):
#    # Проверяем, что возраст - это число от 1 до 49 и целое
#    return age.isdigit() and 0 < int(age) < 50 and float(age) == int(age)


@pytest.mark.api
class TestPetFriends:
    def setup(self):
        self.pf = PetFriend()

    @pytest.fixture(autouse=True)
    def get_key(self):
        self.pf = PetFriend()
        self.status, self.key = self.pf.get_api_key(email_correct, password_correct)
        assert 'key' in self.key
        yield
        assert self.status == 200


    def test_get_api_key_for_not_valid_user(self, email=email_correct):
        """Тест на вход в систему с помощью невалидных данных"""
        status, result = self.pf.get_api_key(email, '0000')

        assert status == 403

    def test_get_api_list_pets_not_valid_user(self, filter='my_pets'):
        """Тестирование возможности просмотреть список 'мои питомцы' использовав невалидные данные для входа"""
        status, auth_key = self.pf.get_api_key(email_correct, '0000')
        if type(auth_key) == dict:
            self.status, result = self.pf.get_api_list_friends(auth_key, filter)
            assert len(result['pets']) > 0
        else:
            assert status == 403


    @pytest.mark.skip(reason='Без API key невозможно провести никакую операцию')
    def test_delete_pets_correct(self):
        """Тестирование возможности удалить карточку питомца без API key"""
        _, list_my_pet = self.pf.get_api_list_friends(self.key, '')
        status = self.pf.delete_api_pet({"key": ''}, list_my_pet['pets'][0]['id'])
        assert status == 403




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


