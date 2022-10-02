import json
from abc import ABC

class Model(ABC):
    def generate_dict(self): # Генеруєм словник з полів які є в нашому класі
        return self.__dict__

    @classmethod
    def get_data(cls):
        file = open('database/' + cls.file, 'r')
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @staticmethod
    def save_to_file(path_to_file, data):
        file = open(path_to_file, 'w')
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def get_all(cls):
        data = cls.get_data()
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                for field in fields:
                    if field == 'id':
                        continue
                    print(el[field])

    @classmethod
    def print_object(cls, objects: list):
        if len(objects) > 0:
            fields = objects[0].keys()
            for ob in objects:
                for field in fields:
                    if field == 'id':
                        continue
                    print(ob[field])

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        count = 0
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                if id == el['id']:
                    return el
                # Каунтер на випадок якшо елемент не знайшло
                count += 1
                if count == len(el):
                    print('Not found element with this Id')

    def save(self):
        data = self.get_data()
        new_el = self.generate_dict()
        if len(data) > 0:
            new_el['id'] = data[-1]['id'] + 1
        else:
            new_el['id'] = 1
        data.append(new_el)
        self.save_to_file('database/' + self.file, data)
