from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional, Pattern, List
import re

from models import Band, Bank, Robbery
from schemas import BandCreate, BandResponse, BankCreate, BankResponse, RobberyCreate, RobberyResponse 

DATABASE_URL = "postgresql://arusyak:pass123@localhost:5432/my_project"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

# Create FastAPI app
app = FastAPI(debug=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания нового бандита
@app.post("/bandits/", response_model=BandResponse)
def create_bandit(bandit: BandCreate, db: Session = Depends(get_db)):
    db_band = Band (**bandit.dict())
    db.add(db_band)
    db.commit()
    db.refresh(db_band)

    return db_band

# Эндпоинт для получения информации о бандите по ID
@app.get("/bandits/{bandit_id}", response_model=BandResponse)
def read_bandit(bandit_id: int, db: Session = Depends(get_db)):
    bandit = db.query(Band).filter(Band.band_id == bandit_id).first()
    if bandit is None:
        raise HTTPException(status_code=404, detail="Bandit not found")
    return bandit

@app.get("/bandits/", response_model=List[BandResponse])
def list_bandits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bandits = db.query(Band).offset(skip).limit(limit).all()
    return bandits

# Эндпоинт для создания нового банка
@app.post("/banks/", response_model=BankResponse)
def create_bank(bank: BankCreate, db: Session = Depends(get_db)):
    db_bank = Bank(**bank.dict())
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)

    return db_bank

# Эндпоинт для получения информации о банке по ID
@app.get("/banks/{bank_id}", response_model=BankResponse)
def read_bank(bank_id: int, db: Session = Depends(get_db)):
    bank = db.query(Bank).filter(Bank.bank_id == bank_id).first()
    if bank is None:
        raise HTTPException(status_code=404, detail="Bank not found")
    return bank

@app.get("/banks/", response_model=List[BankResponse])
def list_banks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    banks = db.query(Bank).offset(skip).limit(limit).all()
    return banks

# Эндпоинт для создания нового ограбления
@app.post("/robberies/", response_model=RobberyResponse)
def create_robbery(robbery: RobberyCreate, db: Session = Depends(get_db)):
    db_robbery = Robbery(**robbery.dict())
    db.add(db_robbery)
    db.commit()
    db.refresh(db_robbery)
    return db_robbery

# Эндпоинт для получения информации об ограблении по ID
@app.get("/robberies/{robbery_id}", response_model=RobberyResponse)
def read_robbery(robbery_id: int, db: Session = Depends(get_db)):
    robbery = db.query(Robbery).filter(Robbery.robbery_id == robbery_id).first()
    if robbery is None:
        raise HTTPException(status_code=404, detail="Robbery not found")
    return robbery

@app.get("/robberies/", response_model=List[RobberyResponse])
def list_robberies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    robberies = db.query(Robbery).offset(skip).limit(limit).all()
    return robberies
