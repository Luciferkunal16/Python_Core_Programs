class DomesticAnimal:
    def Dogs(self):
        print("I am Dog")
class WildAnimal:
    def Tiger(self):
        print("I am Tiger")
class Animal(DomesticAnimal,WildAnimal):
    def Animal(self):
        print("I am Animal")
if __name__=="__main__":
    animal_object=Animal()
    animal_object.Dogs()
    animal_object.Animal()
    animal_object.Tiger()
