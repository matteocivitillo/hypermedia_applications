from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:5173",
      "http://localhost:8080",
      "http://localhost:3000"
    ],            # o metti solo quello che serve
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/messaggi")
async def get_messaggi():
    # Seleziono *tutte* le colonne di tutti i record
    resp = supabase.table("messaggi")\
                   .select("*")\
                   .order("id", desc=False)\
    .execute()
    return {"messaggi": resp.data}

# ------------------- TEACHERS ------------------- #

# Get all teachers information
@app.get("/teachers")
async def get_teachers():
    resp = supabase.table("teacher")\
                   .select("*")\
                   .execute()
    return {"teachers": resp.data}

# Get a specific teacher by ID
@app.get("/teacher/{teacher_id}")
async def get_teacher(teacher_id: str):
    resp = supabase.table("teacher")\
                   .select("*")\
                   .eq("id", teacher_id)\
                   .execute()
    
    if len(resp.data) > 0:
        return {"teacher": resp.data[0]}
    return {"teacher": None}
