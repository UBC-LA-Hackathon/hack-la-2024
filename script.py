# open banksy.json: https://www.w3schools.com/python/python_json.asp
# read
# add info to Discussion object

import json

banksy = open("bonus-hackathon-data/bonus-hackathon-data/hack-la-24-banksy-discussions.json",'r')
data = json.load(banksy)

class Discussion:
    def __init__(self):
        self.title = None
        self.user1 = None
        self.user2 = None
        self.messages = []

    def add_title(self, title):
        self.title = title

    def add_message(self, message):
        self.messages.append(message)

    def add_user(self, user):
        if self.user1 is None:
            self.user1 = user
        elif self.user2 is None and user != self.user1:
            self.user2 = user

    def print_messages(self):
        for msg in self.messages:
            print(msg)

    def get_user1(self):
        return self.user1

    def get_user2(self):
        return self.user2

    def get_title(self):
        return self.title

    def get_messages(self):
        return self.messages


discussion_array = []

for discussions in data:
    discussion_data = discussions['discussion_topic']

    discussion = Discussion()

    discussion.add_title(discussion_data['title'])
    discussion.add_user(discussion_data['user_name'])
    discussion.add_message(discussion_data['message'])

    for reply in discussion_data['replies']:
        discussion.add_user(reply['user_name'])
        discussion.add_message(reply['message'])

    discussion_array.append(discussion)

for i in discussion_array:
    print(f"User 1: {i.user1}")
    print(f"User 2: {i.user2}")
    i.print_messages()