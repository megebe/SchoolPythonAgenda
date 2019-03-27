import json
data_path = './db/data/contacts.json'

def read():
    with open(data_path) as file:
        data = json.load(file)
        file.close()
        return data

def save(contacts):
    with open(data_path, 'w') as file:
        json.dump(contacts, file, indent=4)
        file.close()
