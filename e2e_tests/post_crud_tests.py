import pytest
import allure
from actions import pet_actions
from faker import Faker

fake = Faker()


@allure.description("User should be able to get available pets")
def test_get_all_pets():
    status="available"
    result = pet_actions.get_pets(status)
    assert result.status_code == 200



@allure.description("User should be able to create and delete pet")
def test_create_and_delete_pets():
    name="Doggie"
    photoUrls="Test url"
    status="available"

    # Create a new pet
    result = pet_actions.create_pet(name, photoUrls, status)
    assert result.status_code == 200
    # pet_id = result.json()["id"]
    # assert pet_id is not None

    # Delete the created pet
    # result = pet_actions.delete_pet(pet_id)
    # assert result.status_code == 200
