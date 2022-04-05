import allure
import json
from actions import base_actions
import requests
from faker import Faker

fake = Faker()


@allure.step("Get available pets")
def get_pets(status,client=requests, **kwargs):
    body = f"""{{"status": "{status}"}}"""
    return base_actions.get(client, "pet/findByStatus?", data=body)



@allure.step("Create pet")
def create_pet(name, photoUrls, status, client=requests, **kwargs):
    body = f"""{{"name": "{name}", "photoUrls": ["{photoUrls}"], "status":"{status}"}}"""
    return base_actions.post(client, "pet/", data=body)


@allure.step("Update pet")
def get_pet(pet_id, client=requests, **kwargs):
    return base_actions.get(client, "pet/" + str(pet_id))


@allure.step("Delete a pet")
def delete_pet(pet_id, client=requests, **kwargs):
    return base_actions.delete(client, "pet/" + str(pet_id))
