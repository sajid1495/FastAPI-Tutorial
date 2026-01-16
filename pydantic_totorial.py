from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int 
    height: float
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserting patient data...")

patient_info = {"name": "Sajid", "age": "thirty", "height": 5.9, "weight": 75.5, "married": "False",
                "allergies": ["pollen", "nuts"], "contact_details": {"phone": "123-456-7890", "email": "sajid@example.com"}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)