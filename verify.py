import models
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# API_KEY = ''  # Anyway I will delete this API-Key later on.

# llm = ChatGoogleGenerativeAI(model = 'gemini-flash-1.5' ,google_api_key = API_KEY)


def fetch_details(number_plate):
    db = get_db()
    user = db.query(models.Traffic_Database).filter(models.Traffic_Database.plate_no==number_plate).first()

    if user:
        name = user.owner_name
        pending_fines = user.pending_fines
        active_charges = user.active_charges
        criminal_history = user.criminal_history

        if pending_fines > 0 or active_charges == True or criminal_history == True:
            return f"Flagged Records", 1

        else:
             return f"Safe to go", 0
    
    return None, None