from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud, models

router = APIRouter(prefix="/prescriptions", tags=["prescriptions"])

@router.post("", response_model=schemas.PrescriptionOut)
def create_prescription(data: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    if not db.query(models.User).get(data.user_id):
        raise HTTPException(status_code=400, detail="Invalid user_id")
    med_ids = [i.medicine_id for i in data.items]
    if med_ids:
        existing = {m.id for m in db.query(models.Medicine).filter(models.Medicine.id.in_(med_ids)).all()}
        missing = set(med_ids) - existing
        if missing:
            raise HTTPException(status_code=400, detail=f"Invalid medicine ids: {sorted(missing)}")
    return crud.create_prescription(db, data)

@router.get("", response_model=list[schemas.PrescriptionOut])
def list_prescriptions(user_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_prescriptions(db, user_id)

@router.get("/{rx_id}", response_model=schemas.PrescriptionOut)
def get_prescription(rx_id: int, db: Session = Depends(get_db)):
    rx = crud.get_prescription(db, rx_id)
    if not rx:
        raise HTTPException(status_code=404, detail="Not found")
    return rx

