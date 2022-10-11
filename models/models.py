from framework.models import Model

class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @classmethod
    def get_by_id(cls, id):
        plant_dict = super().get_by_id(id)
        cls.print_object([plant_dict])
        get_employees_plant = Employee.get_data()
        print('The following workers work at this plant: ')
        for worker in get_employees_plant:
            for el in worker:
                if worker['type_of_work'] == 'plant' and worker['object_id'] == str(plant_dict['id']):
                    print(worker['name'])
                    break

    def _protected_example(self):
        return 'protected'

    def __private_example(self):
        return 'private'

class Employee(Model):

    file = "employees.json"

    def __init__(self, name, object_id, type_of_work):
        self.name = name
        self.object_id = object_id
        self.type_of_work = type_of_work
    def get_work(self):
        # Витягуєм данні про роботу
        if self.type_of_work == 'plant':
            return Plant.get_by_id(self.object_id)
        elif self.type_of_work == 'salon':
            return Salon.get_by_id(self.object_id)
        else:
            return {}

    @classmethod
    def get_by_id(cls, id):
        # Викликаєм батьківський метод get_by_id (get_by_id з класу Model)
        employee_dict = super().get_by_id(id)
        employee = Employee(employee_dict['name'], int(employee_dict['object_id']), employee_dict['type_of_work'])
        work_of_employee_plant = Plant.get_data()
        work_of_employee_salon = Salon.get_data()
        cls.print_object([employee_dict])
        print('Employee work in this: ')
        if employee_dict['type_of_work'] == 'plant':
            for el in work_of_employee_plant:
                for el_2 in el:
                    if str(el['id']) == str(employee_dict['object_id']):
                        print(el['name'])
                        break
        elif employee_dict['type_of_work'] == 'salon':
            for el in work_of_employee_salon:
                for el_2 in el:
                    if str(el['id']) == str(employee_dict['object_id']):
                        print(el['name'])
                        break


class Salon(Model):
    file = 'salon.json'

    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size

    @classmethod
    def get_by_id(cls, id):
        salon_dict = super().get_by_id(id)
        cls.print_object([salon_dict])
        get_employees = Employee.get_data()
        print('This workers work at this salon: ')
        for worker in get_employees:
            for el in worker:
                if worker['type_of_work'] == 'salon' and worker['object_id'] == str(salon_dict['id']):
                    print(worker['name'])
                    break