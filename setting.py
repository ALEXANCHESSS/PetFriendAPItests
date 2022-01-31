
email_correct = 'kuznetsov_alex95@mail.ru'
password_correct = '1234'
name_pet = 'Вафля'
type_pet = 'Котофей'
age_pet = '5'
pets_photo = 'images/Cat_sam.jpg'
pets_photo_pdf = 'images/Cat_sam.pdf'

dict_for_put = {
    'name_pet': 'Пряник',
    'type_pet': 'Бывший котофей',
    'age_pet': '4'
}

def generate_string(n):
    return 'x' * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'