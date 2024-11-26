from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.app.shared_state import game_sessions  # Import shared game_sessions

router = APIRouter()


class RoomRequest(BaseModel):
    room_id: str


@router.post("/create_room")
def create_room(request: RoomRequest):
    room_id = request.room_id
    if room_id in game_sessions:
        raise HTTPException(status_code=400, detail="Room already exists")
    game_sessions[room_id] = {"players": [], "state": {}}
    print(f"Room created: {room_id}, Current game_sessions: {game_sessions}")
    return {"success": True, "message": f"Room {room_id} created"}


@router.get("/get_rooms")
def get_rooms():
    return {"success": True, "rooms": list(game_sessions.keys())}
