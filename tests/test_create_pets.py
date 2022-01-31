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


    def test_post_api_create_new_pet_with_out_photo_correct(self):
        """Тестирование корректной работы функции создания нового питомца без изображения"""
        self.status, self.result = self.pf.post_api_create_new_pet_with_out_photo(name_pet, type_pet, age_pet, self.key)
        assert 'id' in self.result

    @pytest.mark.parametrize('name', [generate_string(255), generate_string(1001), russian_chars(),
                                      russian_chars().upper(), chinese_chars(), special_chars(), '123'],
                             ids=['255 symbols', 'more than 1000 symbols',
                                  'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("animal_type"
        , [generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(),
           special_chars(), '123']
        , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("age"
        , ['1']
        , ids=['min'])
    def test_add_new_pet_simple(self, name, animal_type, age):
        """Проверяем, что можно добавить питомца с различными данными"""
        self.status, self.result = self.pf.post_api_add_new_pet_simple(name, animal_type, age, self.key)
        assert self.status == 200
        assert self.result['name'] == name
        assert self.result['age'] == age
        assert self.result['animal_type'] == animal_type



    @pytest.mark.parametrize('name', [''],
                             ids=['empty'])
    @pytest.mark.parametrize("animal_type"
        , ['']
        , ids=['empty'])
    @pytest.mark.parametrize("age"
        , ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(),
           russian_chars().upper(), chinese_chars()]
        , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials',
               'russian', 'RUSSIAN', 'chinese'])
    def test_add_new_pet_simple(self, name, animal_type, age):
        """Проверяем, что можно добавить питомца с различными данными"""
        self.status, self.result = self.pf.post_api_add_new_pet_simple(name, animal_type, age, self.key)
        assert self.status == 400


    def test_post_api_add_new_pet_photo_pdf(self, name=name_pet, animal_type=type_pet,
                                          age=age_pet, pet_photo=pets_photo_pdf):
        """Тестирование возможности добавить нового питомца с использованием изображения в формате .pdf"""

        status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, self.key)
        assert status == 500

    @pytest.mark.xfail(reason='Сервер должен выдавать ошибку, но приходит 200 ОК')
    def test_post_api_add_new_pet_age_str(self, name=name_pet, animal_type=type_pet,
                                          age='age_pet', pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, используя в качестве значения возраста строку"""

        self.status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, self.key)
        assert result['age'] == age

    @pytest.mark.parametrize('name, animal_type, age', [('', '', '')], ids=['empty'])
    def test_post_api_add_new_pet_noname(self, name, animal_type,
                                          age, pet_photo=pets_photo):
        """Тестирование возможности добавить нового питомца, оставив значение 'имя' пустым"""

        self.status, result = self.pf.post_api_add_new_pet(name, animal_type, age, pet_photo, self.key)
        assert result['name'] == name

