
from api import PetFriends
from settings import valid_password, valid_email, not_valid_email, not_valid_password
import os


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """проверяем что запрос ключа возвращает статус 200 и в результате присутствует слово key"""

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_not_valid_email_user(email=not_valid_email, password=valid_password):
    """проверяем что запрос ключа с невалидным email возвращает статус 403"""

    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_not_valid_password_user(email=valid_email, password=not_valid_password):
    """проверяем что запрос ключа с невалидным password возвращает статус 403"""

    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_all_pets_with_valid_key(filter=''):
    """проверяем что запрос возвращает не пустой список"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_information_about_new_pet_with_valid_data(name='Дори', animal_type='золотая рыбка',
                                                       age='2', pet_photo='images/01.JPG'):
    """проверяем можно ли добавить питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_delete_self_pet_successfully():
    """проверяем возможность удаления питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.post_add_information_about_new_pet(auth_key, "Немо", "Рыба клоун", "3", "images/02.JPG")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_update_information_self_pet_successfully(name='Хьюго', animal_type='карась', age='5'):
    """проверяем возможность обновлять информацию о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_add_information_about_new_pet_without_photo_and_with_valid_data(name='Рони', animal_type='акула', age='10'):
    """проверяем можно ли добавить питомца без фотографии с корректными данными"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_photo_self_pet_with_valid_data():
    """проверяем возможность добавления фотографии питомцу с указанным id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.post_add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo='images/02.JPG')
        assert status == 200
    else:
        raise Exception("There is no my pets")


def test_add_information_about_new_pet_with_not_valid_name(name='', animal_type='золотая рыбка', age='3',
                                                           pet_photo='images/01.JPG'):
    """проверяем можно ли добавить питомца с пустой строкой в поле name"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_information_about_new_pet_with_not_valid_name_long(name='a1a2a3a4a5a6a7a8a9a10a11a12a13a'
                                                                     '14a15a16a17a18a19a20a21a22a23a24'
                                                                     'a25a26a27a28a29a30a31a32a33a34a3'
                                                                     '5a36a', animal_type='золотая рыбка',
                                                                age='3', pet_photo='images/01.JPG'):
    """проверяем можно ли добавить питомца с параметром для поля name в 100 символов"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_information_about_new_pet_with_not_valid_animal_type(name='', animal_type='', age='3',
                                                                  pet_photo='images/01.JPG'):
    """проверяем можно ли добавить питомца с пустой строкой в поле animal_type"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == animal_type
