# Single Level Inheritance
class Company:
    def company_details(self):
        print("Company Details")


class Person(Company):
    def person_details(self):
        print("Person Details")

if __name__=="__main__":
    person = Person()
    person.company_details()
