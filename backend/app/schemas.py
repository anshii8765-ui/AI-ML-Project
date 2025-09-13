from typing import Optional, List
from pydantic import BaseModel, EmailStr

# -------- Users --------
class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    class Config:
        from_attributes = True

# -------- Medicines --------
class MedicineCreate(BaseModel):
    name: str
    details: Optional[str] = None

class MedicineOut(BaseModel):
    id: int
    name: str
    details: Optional[str]
    class Config:
        from_attributes = True

# -------- Prescriptions --------
class PrescriptionItemIn(BaseModel):
    medicine_id: int
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    duration: Optional[str] = None

class PrescriptionCreate(BaseModel):
    user_id: int
    title: str
    notes: Optional[str] = None
    items: List[PrescriptionItemIn] = []

class PrescriptionItemOut(BaseModel):
    id: int
    medicine: MedicineOut
    dosage: Optional[str]
    frequency: Optional[str]
    duration: Optional[str]
    class Config:
        from_attributes = True

class PrescriptionOut(BaseModel):
    id: int
    user_id: int
    title: str
    notes: Optional[str]
    items: List[PrescriptionItemOut] = []
    class Config:
        from_attributes = True

