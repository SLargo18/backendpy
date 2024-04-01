from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.config import SessionLocal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/events", response_model=list[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    events = services.get_events(db)
    return JSONResponse(content=jsonable_encoder([event.to_dict() for event in events]))

@router.get("/events/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = services.get_event(db, event_id)
    if not event:
        return JSONResponse(status_code=404, content={"message": "Event not found"})
    return JSONResponse(content=jsonable_encoder(event.to_dict()))

@router.post("/events", response_model=schemas.Event, status_code=201)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    new_event = services.create_event(db, event)
    return JSONResponse(status_code=201, content=jsonable_encoder(new_event.to_dict()))

@router.put("/events/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = services.update_event(db, event_id, event)
    if not db_event:
        return JSONResponse(status_code=404, content={"message": "Event not found"})
    return JSONResponse(content=jsonable_encoder(db_event.to_dict()))

@router.delete("/events/{event_id}", status_code=204)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = services.delete_event(db, event_id)
    if not db_event:
        return JSONResponse(status_code=404, content={"message": "Event not found"})
    return JSONResponse(status_code=204, content={"message": "Event deleted successfully"})