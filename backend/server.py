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

# Get teacher name and surname by activity ID. It runs a function in the database. Multiple values can be returned!
@app.get("/teacher/activity/{activity_id}")
async def get_teacher_by_activityid(activity_id: str):
    resp = supabase.rpc("get_teacher_by_activityid", params={"activity_id": activity_id}).execute()
    
    if resp.data:
        return {"teacher": resp.data}
    return {"teacher": None}

# Get all activities for a specific teacher (many-to-many via teaches)
@app.get("/teacher/{teacher_id}/activities")
async def get_teacher_activities(teacher_id: str):
    # Prendi tutti gli idactivity dalla tabella teaches per questo teacher
    teaches_resp = supabase.table("teaches") \
        .select("idactivity") \
        .eq("idteacher", teacher_id) \
        .execute()
    
    activity_ids = [row["idactivity"] for row in teaches_resp.data] if teaches_resp.data else []
    if not activity_ids:
        return {"activities": []}
    
    # Prendi tutte le attività corrispondenti
    activities_resp = supabase.table("activity") \
        .select("*") \
        .in_("id", activity_ids) \
        .execute()
    
    return {"activities": activities_resp.data}

# ------------------- ACTIVITIES ------------------- #

# Get all activities information
@app.get("/activities")
async def get_activities():
    resp = supabase.table("activity")\
                   .select("*")\
                   .execute()
    return {"activities": resp.data}

# Get a specific activity by ID
@app.get("/activity/{activity_id}")
async def get_activity(activity_id: str):
    resp = supabase.table("activity")\
                   .select("*")\
                   .eq("id", activity_id)\
                   .execute()
    
    if len(resp.data) > 0:
        return {"activity": resp.data[0]}
    return {"activity": None}

# Get a specific activity by name
@app.get("/activity_by_name")
async def get_activity_by_name(name: str):
    # First try exact match
    resp = supabase.table("activity")\
                   .select("*")\
                   .eq("title", name)\
                   .execute()
    
    # If no exact match, try case-insensitive match with ILIKE
    if len(resp.data) == 0:
        resp = supabase.table("activity")\
                       .select("*")\
                       .ilike("title", f"%{name}%")\
                       .execute()
    
    if len(resp.data) > 0:
        return {"activity": resp.data[0], "activity_id": resp.data[0]["id"]}
    
    # If still no match, try matching with common activity name variations
    activity_mappings = {
        "mindful pottery": "Mindful Pottery",
        "mindful potter": "Mindful Pottery",
        "wellness workshop": "Wellness Workshop",
        "wellness workshops": "Wellness Workshop",
        "meditation": "Mindfulness Meditation",
        "mindfulness": "Mindfulness Meditation",
        "hatha yoga": "Hatha Yoga",
        "kundalini yoga": "Kundalini Yoga",
        "kundalini & hatha yoga": "Kundalini Yoga",
        "ashtanga yoga": "Ashtanga Yoga"
    }
    
    normalized_name = name.lower().strip()
    if normalized_name in activity_mappings:
        mapped_name = activity_mappings[normalized_name]
        resp = supabase.table("activity")\
                       .select("*")\
                       .eq("title", mapped_name)\
                       .execute()
        
        if len(resp.data) > 0:
            return {"activity": resp.data[0], "activity_id": resp.data[0]["id"]}
    
    return {"activity": None, "activity_id": None}

# Get activity ID from name
@app.get("/activity_id_from_name")
async def get_activity_id_from_name(name: str):
    # First try exact match
    resp = supabase.table("activity")\
                   .select("id, title")\
                   .eq("title", name)\
                   .execute()
    
    # If no exact match, try case-insensitive match with ILIKE
    if len(resp.data) == 0:
        resp = supabase.table("activity")\
                       .select("id, title")\
                       .ilike("title", f"%{name}%")\
                       .execute()
    
    if len(resp.data) > 0:
        return {"id": resp.data[0]["id"], "title": resp.data[0]["title"]}
    
    # If still no match, try matching with common activity name variations
    activity_mappings = {
        "mindful pottery": "Mindful Pottery",
        "mindful potter": "Mindful Pottery",
        "wellness workshop": "Wellness Workshop",
        "wellness workshops": "Wellness Workshop",
        "meditation": "Mindfulness Meditation",
        "mindfulness": "Mindfulness Meditation",
        "hatha yoga": "Hatha Yoga",
        "kundalini yoga": "Kundalini Yoga",
        "kundalini & hatha yoga": "Kundalini Yoga",
        "ashtanga yoga": "Ashtanga Yoga"
    }
    
    normalized_name = name.lower().strip()
    if normalized_name in activity_mappings:
        mapped_name = activity_mappings[normalized_name]
        resp = supabase.table("activity")\
                       .select("id, title")\
                       .eq("title", mapped_name)\
                       .execute()
        
        if len(resp.data) > 0:
            return {"id": resp.data[0]["id"], "title": resp.data[0]["title"]}
    
    return {"id": None, "title": None}

# ------------------- ROOMS ------------------- #

# Get all rooms information
@app.get("/rooms")
async def get_rooms():
    resp = supabase.table("room")\
                   .select("*")\
                   .execute()
    
    # Process room data to ensure proper formatting
    rooms_data = []
    for room in resp.data:
        # Process features - ensure it's a list
        features = room.get("features", "")
        if isinstance(features, str):
            # Split by hyphens if they exist
            if "-" in features:
                features_list = [f.strip() for f in features.split("-") if f.strip()]
            # Otherwise split by commas if they exist
            elif "," in features:
                features_list = [f.strip() for f in features.split(",") if f.strip()]
            else:
                # Single feature or empty
                features_list = [features] if features else []
        else:
            features_list = features if isinstance(features, list) else []
        
        # Ottieni le attività dalla tabella activity che hanno questa stanza come roomid
        room_id = room.get("id")
        
        # Cerca le attività che hanno questa stanza come roomid
        activities_resp = supabase.table("activity")\
                                 .select("title")\
                                 .eq("roomid", room_id)\
                                 .execute()
        
        # Estrai i titoli delle attività dai risultati
        activities = [a["title"] for a in activities_resp.data] if activities_resp.data else []
        
        # Format the processed room data
        processed_room = {
            "id": room.get("id"),
            "title": room.get("title", ""),
            "description": room.get("description", ""),
            "features": features_list,
            "activities": activities,
            "image": room.get("image", ""),
            "quote": room.get("quote", "Experience the transformative power of our specially designed spaces.")
        }
        
        rooms_data.append(processed_room)
    
    return {"rooms": rooms_data}

# Get a specific room by ID
@app.get("/room/{room_id}")
async def get_room(room_id: str):
    resp = supabase.table("room")\
                   .select("*")\
                   .eq("id", room_id)\
                   .execute()
    
    if len(resp.data) > 0:
        room = resp.data[0]
        
        # Process features - ensure it's a list
        features = room.get("features", "")
        if isinstance(features, str):
            # Split by hyphens if they exist
            if "-" in features:
                features_list = [f.strip() for f in features.split("-") if f.strip()]
            # Otherwise split by commas if they exist
            elif "," in features:
                features_list = [f.strip() for f in features.split(",") if f.strip()]
            else:
                # Single feature or empty
                features_list = [features] if features else []
        else:
            features_list = features if isinstance(features, list) else []
        
        # Process activities - combine activity1 and activity2
        activities = []
        activity1 = room.get("activity1")
        activity2 = room.get("activity2")
        
        if activity1:
            activities.append(activity1)
        if activity2:
            activities.append(activity2)
            
        # If no activities were found in activity1/2, check activities field
        if not activities and room.get("activities"):
            activities_text = room.get("activities")
            if isinstance(activities_text, str):
                # Split by hyphens if they exist
                if "-" in activities_text:
                    activities = [a.strip() for a in activities_text.split("-") if a.strip()]
                # Otherwise split by commas if they exist
                elif "," in activities_text:
                    activities = [a.strip() for a in activities_text.split(",") if a.strip()]
                else:
                    # Single activity
                    activities = [activities_text]
            elif isinstance(activities_text, list):
                activities = activities_text
        
        # Format the processed room data
        processed_room = {
            "id": room.get("id"),
            "title": room.get("title", ""),
            "description": room.get("description", ""),
            "features": features_list,
            "activities": activities,
            "image": room.get("image", ""),
            "quote": room.get("quote", "Experience the transformative power of our specially designed spaces.")
        }
        
        return {"room": processed_room}
    return {"room": None}

# ------------------- AREAS ------------------- #

# Get all areas information
@app.get("/areas")
async def get_areas():
    resp = supabase.table("areas")\
                   .select("*")\
                   .execute()
    
    # Process the areas to ensure complete image URLs
    areas_data = []
    for area in resp.data:
        # Create a complete URL if it's partial
        image_url = area.get("image", "")
        if image_url and "dcrgvkmnnavjahkprnkem.supabase" in image_url:
            # Check if it's a partial URL
            if not "/storage/v1/object/public/yoga/" in image_url:
                # Complete the URL based on area title
                area_title = area.get("title", "").lower()
                if area_title == "bar":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg"
                elif area_title == "play area":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg"
                elif area_title == "spa":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg"
        
        # Update the area with the complete image URL
        area["image"] = image_url
        areas_data.append(area)
    
    return {"areas": areas_data}

# Get a specific area by ID
@app.get("/area/{area_id}")
async def get_area(area_id: str):
    resp = supabase.table("areas")\
                   .select("*")\
                   .eq("id", area_id)\
                   .execute()
    
    if len(resp.data) > 0:
        area = resp.data[0]
        
        # Create a complete URL if it's partial
        image_url = area.get("image", "")
        if image_url and "dcrgvkmnnavjahkprnkem.supabase" in image_url:
            # Check if it's a partial URL
            if not "/storage/v1/object/public/yoga/" in image_url:
                # Complete the URL based on area title
                area_title = area.get("title", "").lower()
                if area_title == "bar":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg"
                elif area_title == "play area":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg"
                elif area_title == "spa":
                    image_url = "https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg"
                
                area["image"] = image_url
        
        return {"area": area}
    return {"area": None}
