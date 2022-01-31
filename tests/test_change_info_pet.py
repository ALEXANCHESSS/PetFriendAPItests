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



    def test_post_api_add_photo_pet(self):
        """Тестирование функции добавления фотографии или ее замены к существующей карточки питомца"""
        _, list_my_pet = self.pf.get_api_list_friends(self.key, 'my_pets')
        if len(list_my_pet['pets']) == 0:
            _, id_pet = self.pf.post_api_create_new_pet_with_out_photo(name_pet, type_pet, age_pet, self.key)
            self.status, result = self.pf.post_api_add_photo_pet(id_pet['id'], pets_photo, self.key)
            assert id_pet['id'] == result['id']
        else:
            self.status, result = self.pf.post_api_add_photo_pet(list_my_pet['pets'][0]['id'], pets_photo, self.key)
            assert list_my_pet['pets'][0]['id'] == result['id']


