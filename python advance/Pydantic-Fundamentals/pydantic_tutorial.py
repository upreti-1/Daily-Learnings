from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title = 'Name of the patient', 
                               description= 'Give the name of the patient in less then 50 words: ', examples = ['Nitish', 'Amit'])]
    #name: str = Field(max_length= 50)
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0, lt = 120)
    #weight: float = Field(gt = 0)
    weight: Annotated[float, Field(gt = 0, strict = True)]
    married: Annotated[bool, Field(default= None, description= 'Is the patient married or not ?')]
    allergies: Optional[List[str]] = Field(default = None, max_length=10)
    contact_details: Dict[str, str]

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info1 = {'name':'Nikhil', 'age':30,'email':'ab1@gmail.com','linkedin_url':'https://linkedin.com/123', 'weight': 90.2, 'married': True, #'allergies':['pollen', 'dust'], aba allergies chai optonal hunxa and default value is None
                 'contact_details':{'email':"abc@gmail.com", 'phone':'9090909090'}}
#patient_info2 = {'name':'Biraj', 'age':31}

patient1 = Patient(**patient_info1)
#patient2 = Patient(**patient_info2)

insert_data(patient1)
#update_data(patient2)