from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from backend.app.routes import game
from backend.app.game_logic import handle_player_action
from backend.app.shared_state import game_sessions  # Import the shared state

# Initialize FastAPI app
app = FastAPI(
    title="D&D AI Game Master",
    description="A backend API for managing game rooms and facilitating interactions with an AI-powered Game Master",
    version="1.0.0"
)

# Include routes for game room management
app.include_router(game.router)

# Root endpoint for health check or basic information
@app.get("/")
def read_root():
    """
    Health check endpoint.
    """
    return {"message": "Welcome to the D&D AI Game Master!"}

# WebSocket endpoint for player interactions
@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    print(f"WebSocket connection request for room_id: {room_id}")
    await websocket.accept()

    # Check if the room exists
    print(f"Current game_sessions: {game_sessions}")  # Debugging: show current state
    if room_id not in game_sessions:
        print(f"Room {room_id} not found in game_sessions.")
        await websocket.send_text("Room not found.")
        await websocket.close(code=403)
        return

    # Add the WebSocket connection to the room
    print(f"Room {room_id} found. Adding WebSocket connection.")
    game_sessions[room_id]["players"].append(websocket)

    try:
        while True:
            # Receive player input
            data = await websocket.receive_text()
            print(f"Received: {data}")

            # Handle player action and get AI response
            response = handle_player_action(data, game_sessions[room_id])

            # Debugging: print the AI response
            print(f"AI Response: {response}")

            # Send response back to all players in the room
            for player in game_sessions[room_id]["players"]:
                await player.send_text(response)
    except WebSocketDisconnect:
        # Remove the WebSocket connection when the client disconnects
        game_sessions[room_id]["players"].remove(websocket)
        print(f"Client disconnected from room {room_id}")

        # Cleanup: Remove the room if it is empty
        if not game_sessions[room_id]["players"]:
            del game_sessions[room_id]
            print(f"Room {room_id} has been removed as it is now empty.")

