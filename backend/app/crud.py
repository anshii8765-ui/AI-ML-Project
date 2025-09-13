from sqlalchemy.orm import Session
from . import models, schemas

# ---------- Users ----------
def create_user(db: Session, user: schemas.UserCreate):
    obj = models.User(email=user.email, name=user.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_user(db: Session, user_id: int):
    return db.query(models.User).get(user_id)

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def list_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# ---------- Medicines ----------
def create_medicine(db: Session, med: schemas.MedicineCreate):
    obj = models.Medicine(name=med.name, details=med.details)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_medicines(db: Session, q: str | None = None):
    query = db.query(models.Medicine)
    if q:
        query = query.filter(models.Medicine.name.ilike(f"%{q}%"))
    return query.order_by(models.Medicine.name.asc()).all()

# ---------- Prescriptions ----------
def create_prescription(db: Session, data: schemas.PrescriptionCreate):
    rx = models.Prescription(user_id=data.user_id, title=data.title, notes=data.notes)
    db.add(rx)
    db.flush()
    for item in data.items:
        db.add(models.PrescriptionItem(
            prescription_id=rx.id,
            medicine_id=item.medicine_id,
            dosage=item.dosage,
            frequency=item.frequency,
            duration=item.duration
        ))
    db.commit()
    db.refresh(rx)
    return rx

def get_prescription(db: Session, rx_id: int):
    return db.query(models.Prescription).filter(models.Prescription.id == rx_id).first()

def list_prescriptions(db: Session, user_id: int | None = None):
    query = db.query(models.Prescription)
    if user_id:
        query = query.filter(models.Prescription.user_id == user_id)
    return query.order_by(models.Prescription.id.desc()).all()
nano app/crud.py

