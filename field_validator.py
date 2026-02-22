from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: str
    linkedin_url: AnyUrl
    age: int 
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]





    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # extracting text after @
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    
    @field_validator('name', mode = 'after') # if set before, the value in this functin gets the value of the variable before type coersion by smart Pydantic. (int, str, etc.)
    @classmethod
    def transform_name(cls, value):
        return value.upper()



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



patient_info1 = {'name':'Nikhil', 'age':30,'email':'ab1@icici.com','linkedin_url':'https://linkedin.com/123', 'weight': 90.2, 
                 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':"abc@gmail.com", 'phone':'9090909090'}}


patient1 = Patient(**patient_info1)     # VALIDATION HAPPENS HERE -> Type Coercion


insert_data(patient1)
