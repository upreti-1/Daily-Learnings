from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient (BaseModel):
    name: str
    gender: str = 'male'
    age: int
    address: Address


address_dict = {'city': 'gurgaon', 'state':'haryana','pin':'12345'}

address1 = Address(**address_dict)

patient_dict = {'name':'Nikhil', 'age':12, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()       # it will convert an existing pydantic model to a python dictionary
temp1 = patient1.model_dump(include=['name', 'address'])
temp2 = patient1.model_dump(exclude=['name', 'address'])
temp3 = patient1.model_dump(exclude = {'address':['state']})

temp5 = patient1.model_dump(exclude_unset= True)    # will not show the things that are not set while entering data in the pydantic model



print(temp)
print(temp1)
print(temp2)
print(temp3)
print('Temp 5',temp5)
print(type(temp))