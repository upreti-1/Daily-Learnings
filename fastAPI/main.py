from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (restrict this to your frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)

class Patient(BaseModel):
    id: Annotated[str, Field(..., description = 'Id of the patient', examples= ['P001'])]
    name: Annotated[str, Field(..., description= 'Name of the patient')]
    city: Annotated[str, Field(..., description= 'city in which the patient is living')]
    age: Annotated[int, Field(..., gt = 0, lt = 120, description= 'age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description= 'choose between male, female and others')]
    height: Annotated[float, Field(..., gt = 0, description= 'Height of the patient in meters')]
    weight: Annotated[float, Field(..., gt = 1, description= 'weight of the patient in KGs')]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight / (self.height)**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None,gt = 0)]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt = 0)]
    weight: Annotated[Optional[float], Field(default=None, gt = 0)]


def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)



@app.get('/')
def hello():
    return {'message': 'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': "Fully functional API to manage your patient records"}

"""@app.get('/view')
def view():
    data = load_data()
    return list(data.values())"""

@app.get('/view')
def view():
    data = load_data()
    
    # Inject the ID back into the patient data before sending to frontend
    patient_list = []
    for patient_id, patient_info in data.items():
        patient_info['id'] = patient_id
        patient_list.append(patient_info)
        
    return patient_list

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description= "ID of the patient in the DB", example = 'P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail= "Patient Not Found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = "Sort on the basis of height, weight or bmi"),
                   order: str = Query('asc',description = 'Sort in ascending or descending order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid feild. Select from {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Select between ascending and descending")
    
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x:x.get(sort_by, 0), reverse = sort_order)

    return sorted_data




@app.post('/create')
def create_patient(patient_info : Patient):
    
    # load existing data
    data = load_data()

    # checking if the patient already exists in the database
    if patient_info.id in data:
        raise HTTPException(status_code= 400, detail= 'patient already exists')

    # new patient add to database
    # converting pydantic object into dictionary
    data[patient_info.id] = patient_info.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    # sending response that the records is created to the client
    return JSONResponse(status_code= 201, content={'message' : 'Patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException (status_code= 404, detail= 'Patient Not Found')
    
    existing_data_info = data[patient_id]

    # converting patient_update to dictionary
    updated_patient_info = patient_update.model_dump(exclude_unset= True) 

    for key, value in updated_patient_info.items():
        existing_data_info[key] = value

    # now we need to change the existing_data_info to pydantic format to get the bmi and verdict calculations auto.
    # existing_data_info -> pydantic object -> updated bmi & verdict -> pydantic object -> dictionary -> save
    existing_data_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_data_info)

    patient_pydantic_object = patient_pydantic_object.model_dump(exclude=['id'])
    # add this dict to data
    data[patient_id] = patient_pydantic_object

    # save data
    save_data(data)

    return JSONResponse (status_code=200, content= {'message':'Patient Updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        return HTTPException(status_code= 404, detail="patient not found")
    
    del data[patient_id]
    
    save_data(data)

    return JSONResponse(status_code= 200, content = {'message':'Deletion Successfull'})