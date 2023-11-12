from decor import log_dec
from exeptions import InvalidNameError, InvalidAgeError, InvalidIdError
import argparse


class Person:

    def __init__(self, last_name, first_name, middle_name, age):
        self._validate_name(last_name, 'Last Name')
        self._validate_name(first_name, 'First Name')
        self._validate_name(middle_name, 'Middle Name')
        self._validate_age(age)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    @log_dec
    def _validate_name(self, name, field_name):
        if not name or not isinstance(name, str):
            raise InvalidNameError(f'Invalid name: {name}. '
                                   f'Name should be a non-empty string.')

    @log_dec
    def _validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. '
                                  f'Age should be a positive integer.')

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}, ' \
               f'Age: {self.age}'


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id):
        super().__init__(last_name, first_name, middle_name, age)
        self._validate_id(id)
        self.id = id

    @log_dec
    def _validate_id(self, id):
        if not isinstance(id, int) or id < 100000 or id > 999999:
            raise InvalidIdError(
                f'Invalid id: {id}. Id should be a 6-digit positive '
                f'integer between 100000 and 999999.')

    def get_level(self):
        return sum(map(int, str(self.id))) % 7


def main():
    parser = argparse.ArgumentParser(description='Person and Employee info')
    parser.add_argument('--last_name', '-ln', type=str, help='Last Name')
    parser.add_argument('--first_name', '-fn', type=str, help='First Name')
    parser.add_argument('--middle_name', '-mn', type=str, help='Middle Name')
    parser.add_argument('--age', '-a', type=int, help='Age')
    parser.add_argument('--id', '-i', type=int, help='Employee ID')
    args = parser.parse_args()
    employee = Employee(args.last_name, args.first_name,
                        args.middle_name, args.age, args.id)
    return f'Employee information:\n{employee}' \
           f'\nEmployee Level:\n{employee.get_level()}'



if __name__ == "__main__":
    print(main())

# person = Person("", "John", "Doe", 30)
# print(person)
# employee = Employee(55, 55,55,-30,00)
# print(employee)