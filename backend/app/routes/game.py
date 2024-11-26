from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Pydantic model for request body
class RoomRequest(BaseModel):
    room_id: str

# In-memory game session storage
game_sessions = {}

@router.post("/create_room")
def create_room(request: RoomRequest):
    room_id = request.room_id
    if room_id in game_sessions:
        return {"error": "Room already exists"}
    game_sessions[room_id] = {"players": [], "state": {}}
    return {"message": f"Room {room_id} created"}
    
@router.get("/get_rooms")
def get_rooms():
    return {"rooms": list(game_sessions.keys())}


