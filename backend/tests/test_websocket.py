import asyncio
import websockets
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def ensure_room_exists(room_id):

    response = requests.post(f"{BASE_URL}/create_room", json={"room_id": room_id})
    if response.status_code == 200:
        print(f"Room {room_id} created: {response.json()}")
    elif response.status_code == 400 and "Room already exists" in response.text:
        print(f"Room {room_id} already exists.")
    else:
        raise Exception(f"Failed to ensure room existence: {response.text}")

async def test_websocket():

    uri = "ws://127.0.0.1:8000/ws/room1"  # Ensure the 'room1' exists on the server
    try:
        # Connect to the WebSocket
        async with websockets.connect(uri) as websocket:
            print("Connected to WebSocket")

            # Prepare a test message
            message = "I want to attack the goblin with my sword."
            print(f"Sending: {message}")

            # Send the message
            await websocket.send(message)

            # Receive the response
            response = await websocket.recv()
            print(f"Received: {response}")

            # Optional: Validate the response format
            try:
                response_data = json.loads(response)
                print(f"Response is valid JSON: {response_data}")
            except json.JSONDecodeError:
                print("Response is not in JSON format.")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection was closed unexpectedly: {e}")
    except Exception as e:
        print(f"An error occurred during WebSocket communication: {e}")

if __name__ == "__main__":
    # Ensure room exists before running the WebSocket test
    ensure_room_exists("room1")
    asyncio.run(test_websocket())

