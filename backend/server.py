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
      "https://hypermedia-applications-rho.vercel.app",  # Frontend su Vercel
      "http://localhost:5173",
      "http://localhost:8080",
      "http://localhost:3000",
      "http://localhost:3001"
    ],
    allow_credentials=True,
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
async def get_teachers(lang: str = "en"):
    try:
        base_resp = supabase.table("teacher_base").select("*").execute()
        base_teachers = base_resp.data if base_resp.data else []
        if not base_teachers:
            return {"teachers": []}
        teachers = []
        missing_translations = []
        for base in base_teachers:
            trans_resp = supabase.table("teacher_translations")\
                .select("*")\
                .eq("teacher_id", base["id"])\
                .eq("language_code", lang)\
                .execute()
            trans_data = trans_resp.data[0] if trans_resp.data else None
            if not trans_data:
                missing_translations.append(base["id"])
                continue
            teacher = {**base, **trans_data}
            if "teacher_id" in teacher:
                del teacher["teacher_id"]
            if "language_code" in teacher:
                del teacher["language_code"]
            teachers.append(teacher)
        if missing_translations:
            return {"error": f"Missing translations for teachers: {missing_translations}", "teachers": []}
        return {"teachers": teachers}
    except Exception as e:
        print(f"Error fetching teachers: {str(e)}")
        return {"teachers": [], "error": str(e)}

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

# Get all activities information with translations for a specific language (NO fallback)
@app.get("/activities")
async def get_activities(lang: str = "en"):
    """
    Restituisce tutte le attività con le traduzioni nella lingua richiesta.
    Se una traduzione non esiste per una attività, ritorna errore.
    """
    try:
        # Prendi tutte le attività base
        base_resp = supabase.table("activity_base").select("*").execute()
        base_activities = base_resp.data if base_resp.data else []

        if not base_activities:
            return {"activities": []}

        activities = []
        missing_translations = []
        for base in base_activities:
            # Prendi la traduzione nella lingua richiesta
            trans_resp = supabase.table("activity_translations")\
                .select("*")\
                .eq("activity_id", base["id"])\
                .eq("language_code", lang)\
                .execute()
            trans_data = trans_resp.data[0] if trans_resp.data else None

            # Se non trovi la traduzione, aggiungi a missing_translations
            if not trans_data:
                missing_translations.append(base["id"])
                continue

            # Unisci i dati base e tradotti
            activity = {**base, **trans_data}
            # Rimuovi campi duplicati
            if "activity_id" in activity:
                del activity["activity_id"]
            if "language_code" in activity:
                del activity["language_code"]

            activities.append(activity)

        if missing_translations:
            return {"error": f"Missing translations for activities: {missing_translations}", "activities": []}

        return {"activities": activities}
    except Exception as e:
        print(f"Error fetching activities: {str(e)}")
        return {"activities": [], "error": str(e)}

# Get a specific activity by ID
@app.get("/activity/{activity_id}")
async def get_activity(activity_id: str, lang: str = "en"):
    try:
        # Fetch base activity data
        base_resp = supabase.table("activity_base").select("*").eq("id", activity_id).execute()
        
        if not base_resp.data or len(base_resp.data) == 0:
            return {"activity": None}
            
        base_activity = base_resp.data[0]
        
        # Fetch translation for the requested language
        trans_resp = supabase.table("activity_translations")\
            .select("*")\
            .eq("activity_id", activity_id)\
            .eq("language_code", lang)\
            .execute()
            
        # If translation not found in requested language, try English as fallback
        if not trans_resp.data or len(trans_resp.data) == 0:
            if lang != "en":
                trans_resp = supabase.table("activity_translations")\
                    .select("*")\
                    .eq("activity_id", activity_id)\
                    .eq("language_code", "en")\
                    .execute()
        
        if not trans_resp.data or len(trans_resp.data) == 0:
            # If still no translation, return just the base data
            return {"activity": base_activity}
            
        # Merge base and translation data
        trans_data = trans_resp.data[0]
        activity = {**base_activity, **trans_data}
        
        # Remove duplicate fields
        if "activity_id" in activity:
            del activity["activity_id"]
        if "language_code" in activity:
            del activity["language_code"]
            
        return {"activity": activity}
    except Exception as e:
        print(f"Error fetching activity {activity_id}: {str(e)}")
        return {"activity": None, "error": str(e)}

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
async def get_rooms(lang: str = "en"):
    try:
        base_resp = supabase.table("room_base").select("*").execute()
        base_rooms = base_resp.data if base_resp.data else []
        if not base_rooms:
            return {"rooms": []}
        rooms = []
        missing_translations = []
        for base in base_rooms:
            trans_resp = supabase.table("room_translations")\
                .select("*")\
                .eq("room_id", base["id"])\
                .eq("language_code", lang)\
                .execute()
            trans_data = trans_resp.data[0] if trans_resp.data else None
            if not trans_data:
                missing_translations.append(base["id"])
                continue
            room = {**base, **trans_data}
            if "room_id" in room:
                del room["room_id"]
            if "language_code" in room:
                del room["language_code"]
            rooms.append(room)
        if missing_translations:
            return {"error": f"Missing translations for rooms: {missing_translations}", "rooms": []}
        return {"rooms": rooms}
    except Exception as e:
        print(f"Error fetching rooms: {str(e)}")
        return {"rooms": [], "error": str(e)}

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

# ------------------- REVIEWS ------------------- #

@app.get("/reviews")
async def get_reviews(lang: str = "en"):
    try:
        # Recupera le review di base
        base_resp = supabase.table("reviews_base").select("*").order("date", desc=True).execute()
        base_reviews = base_resp.data if base_resp.data else []
        if not base_reviews:
            return {"reviews": []}
            
        reviews = []
        missing_translations = []
        
        for base in base_reviews:
            # Recupera le traduzioni per questa lingua
            trans_resp = supabase.table("review_translations")\
                .select("*")\
                .eq("review_id", base["id"])\
                .eq("language_code", lang)\
                .execute()
            trans_data = trans_resp.data[0] if trans_resp.data else None
            
            if not trans_data:
                missing_translations.append(base["id"])
                continue
                
            # Recupera le informazioni del partecipante
            participant_resp = supabase.table("participant")\
                .select("*")\
                .eq("id", base["idparticipant"])\
                .execute()
            participant_data = participant_resp.data[0] if participant_resp.data else {}
            
            # Recupera le informazioni dell'attività
            activity_resp = supabase.table("activity_base")\
                .select("id")\
                .eq("id", base["idactivity"])\
                .execute()
                
            activity_id = None
            if activity_resp.data and len(activity_resp.data) > 0:
                activity_id = activity_resp.data[0].get("id")
                
                # Recupera il titolo dell'attività nella lingua specifica
                activity_trans_resp = supabase.table("activity_translations")\
                    .select("title")\
                    .eq("activity_id", activity_id)\
                    .eq("language_code", lang)\
                    .execute()
                    
                activity_title = None
                if activity_trans_resp.data and len(activity_trans_resp.data) > 0:
                    activity_title = activity_trans_resp.data[0].get("title")
            
            # Unisci tutti i dati
            review = {**base, **trans_data}
            if "review_id" in review:
                del review["review_id"]
            if "language_code" in review:
                del review["language_code"]
                
            # Aggiungi le informazioni del partecipante
            review["participant"] = participant_data
            
            # Aggiungi le informazioni dell'attività
            review["activity"] = {
                "id": activity_id,
                "title": activity_title
            }
            
            reviews.append(review)
            
        if missing_translations:
            return {"error": f"Missing translations for reviews: {missing_translations}", "reviews": []}
            
        return {"reviews": reviews}
    except Exception as e:
        print(f"Error fetching reviews: {str(e)}")
        return {"reviews": [], "error": str(e)}
