# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)

import uuid
import requests

class randomuser:
    id = []
    username = []

    def __init__(self, id):
        self.username = self.get_firstname_and_lastname()
        self.id = uuid.uuid1()

    def get_firstname_and_lastname(self):
        users = requests.get("https://randomuser.me/api/")
        datausers = users.json()
        firstname = datausers['results'][0]['name']['first']
        lastname = datausers['results'][0]['name']['last']
        return firstname, lastname

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id

class randomusers:
    users = []
    ids = []

    def __init__(self, loops = 100):
        for i in range(loops):
            self.users.append(randomuser(i))
            self.ids.append(randomuser(i))

    def list_of_users(self):
        for user in self.users:
            print(user.get_id(), user.get_username()[0].capitalize()+' '+user.get_username()[1].capitalize())

x = randomusers(100)

x.list_of_users()
