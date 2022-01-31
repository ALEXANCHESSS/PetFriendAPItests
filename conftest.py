import pytest

from setting import *
from api import PetFriend

class FicsturesTest:

        def setup(self):
                self.pf = PetFriend()

        @pytest.fixture()
        def get_key(self):
                pf = PetFriend()
                status, self.key = pf.get_api_key(email_correct, password_correct)
                assert status == 200
                assert 'key' in self.key
                return self.key

