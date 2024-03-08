class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        if owner:
            owner.add_pet(self)
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        if not all(isinstance(pet, Pet) for pet in self.pets_list):
            raise Exception("Invalid pet type")

        sorted_pets = sorted(self.pets_list, key=lambda p: p.name)
        return sorted_pets
