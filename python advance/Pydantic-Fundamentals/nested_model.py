from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient (BaseModel):
    name: str
    gender: str
    age: int
    address: Address

    # here address is a complex data ('house no, street, city, pincode)
    # so if we need only city or pincode, it becomes complex. To overcome this issue, we use nested_models

address_dict = {'city': 'gurgaon', 'state':'haryana','pin':'12345'}

address1 = Address(**address_dict)

patient_dict = {'name':'Nikhil', 'gender':'Male', 'age':12, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)


# Better Data Organization
# Code Reusability
# Enhanced Readibility
# Automatic Validation