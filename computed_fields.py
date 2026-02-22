# Computed feild calculates the information that are not provided explicitly by the user.
# In this example, we will calculate BMI dynamically using computed field.

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float  #kg
    height: float  #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height)**2 ,2)
        return bmi
  

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.calculate_bmi)
    print('Inserted')



def update_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')



patient_info1 = {'name':'Nikhil', 'age':770,'email':'ab1@icici.com','linkedin_url':'https://linkedin.com/123', 'weight': 20.2, 'height': 1.72,
                 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':"abc@gmail.com", 'phone':'9090909090', 'emergency': '0202020202'}}


patient1 = Patient(**patient_info1)     # VALIDATION HAPPENS HERE -> Type Coercion


insert_data(patient1)
