import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.db.database import Base
from src.models.db.medicine import Medicine
from src.models.db.alert import StockAlert
from langchain_community.utilities import SQLDatabase
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_DIR = os.path.join(BASE_DIR, "../db")
DB_PATH = os.path.join(BASE_DIR, "../db/pharmacy.db")  
DATABASE_URL = f"sqlite:///{DB_PATH}"

os.makedirs(DB_DIR, exist_ok=True)

engine = create_engine(DATABASE_URL)    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SQLDatabase.from_uri(DATABASE_URL)

def initialize_db():
    Base.metadata.create_all(bind=engine)   
    print("✅ Database tables created successfully!")

    db_session = SessionLocal()
    try:
        if db_session.query(Medicine).count() == 0:
            mock_medicines = [
                Medicine(name="Aspirin", dosage="500mg", quantity=50, price=5.99, expiry_date=date.fromisoformat("2025-12-31")),
                Medicine(name="Paracetamol", dosage="325mg", quantity=5, price=3.49, expiry_date=date.fromisoformat("2024-06-30")),
                Medicine(name="Ibuprofen", dosage="200mg", quantity=20, price=4.99, expiry_date=date.fromisoformat("2025-03-15")),
                Medicine(name="Amoxicillin", dosage="250mg", quantity=100, price=8.50, expiry_date=date.fromisoformat("2026-01-20")),
                Medicine(name="Cetirizine", dosage="10mg", quantity=75, price=2.99, expiry_date=date.fromisoformat("2025-09-10")),
                Medicine(name="Metformin", dosage="500mg", quantity=30, price=6.75, expiry_date=date.fromisoformat("2024-12-15")),
                Medicine(name="Omeprazole", dosage="20mg", quantity=15, price=4.25, expiry_date=date.fromisoformat("2025-06-01")),
                Medicine(name="Lisinopril", dosage="10mg", quantity=60, price=7.80, expiry_date=date.fromisoformat("2026-03-30")),
                Medicine(name="Atorvastatin", dosage="40mg", quantity=25, price=9.99, expiry_date=date.fromisoformat("2025-11-22")),
                Medicine(name="Salbutamol", dosage="100mcg", quantity=200, price=12.50, expiry_date=date.fromisoformat("2025-08-05")),
                Medicine(name="Diazepam", dosage="5mg", quantity=10, price=3.20, expiry_date=date.fromisoformat("2024-09-15")),
                Medicine(name="Ciprofloxacin", dosage="500mg", quantity=45, price=10.00, expiry_date=date.fromisoformat("2026-02-28")),
                Medicine(name="Loratadine", dosage="10mg", quantity=80, price=3.75, expiry_date=date.fromisoformat("2025-07-19")),
                Medicine(name="Prednisolone", dosage="5mg", quantity=35, price=5.60, expiry_date=date.fromisoformat("2024-11-30")),
                Medicine(name="Levothyroxine", dosage="50mcg", quantity=90, price=6.40, expiry_date=date.fromisoformat("2026-04-10")),
                Medicine(name="Tramadol", dosage="50mg", quantity=40, price=7.25, expiry_date=date.fromisoformat("2025-10-10")),
                Medicine(name="Amlodipine", dosage="5mg", quantity=120, price=5.50, expiry_date=date.fromisoformat("2026-05-15")),
                Medicine(name="Clopidogrel", dosage="75mg", quantity=60, price=8.25, expiry_date=date.fromisoformat("2025-10-15")),
                Medicine(name="Hydrochlorothiazide", dosage="25mg", quantity=90, price=4.80, expiry_date=date.fromisoformat("2026-02-10")),
                Medicine(name="Sertraline", dosage="50mg", quantity=30, price=6.95, expiry_date=date.fromisoformat("2024-12-01")),
                Medicine(name="Montelukast", dosage="10mg", quantity=45, price=7.50, expiry_date=date.fromisoformat("2025-08-20")),
                Medicine(name="Ranitidine", dosage="150mg", quantity=15, price=3.99, expiry_date=date.fromisoformat("2024-11-15")),
           
           
            ]
            db_session.add_all(mock_medicines)
            db_session.flush()  # Assign IDs
            mock_alerts = [
                StockAlert(medicine_id=m.id, alert_quantity=20) for m in mock_medicines  # Increased threshold for variety
            ]
            db_session.add_all(mock_alerts)
            db_session.commit()
            print("✅ Mock medicines and alerts added to pharmacy.db!")
        else:
            print(f"ℹ️ Database already has {db_session.query(Medicine).count()} medicines.")
    except Exception as e:
        print(f"❌ Error adding mock data: {e}")
        db_session.rollback()
    finally:
        db_session.close()
    print("✅ Database initialized successfully!")