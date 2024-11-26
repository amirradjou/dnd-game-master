# D&D AI Game Master

Welcome to the **D&D AI Game Master**, a Python-based backend API for running Dungeons & Dragons-inspired games using an AI-powered Game Master. This project leverages OpenAI's GPT-based models to create an immersive, interactive, and engaging storytelling experience for players.

## Features

- **AI-Powered Game Master**: The AI serves as a Game Master, responding to player inputs with detailed and engaging narratives following D&D principles.
- **Multi-Player Support**: Allows multiple players to interact in shared game rooms using WebSocket connections.
- **Dynamic Room Management**: Create and manage game rooms through REST API endpoints.
- **Shared Game State**: Maintains game sessions and state using shared in-memory storage.

## Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)**: Web framework for building the API.
- **[OpenAI's GPT Models](https://platform.openai.com/docs/)**: Used for AI-based responses.
- **WebSockets**: Enables real-time communication between players and the Game Master.
- **Python `dotenv`**: For managing environment variables.
- **Pydantic**: Data validation and settings management.

## Project Structure

```plaintext
app/
├── ai_master.py       # Handles AI Game Master interactions using OpenAI GPT models.
├── game_logic.py      # Manages game logic and updates session state.
├── main.py            # Initializes the FastAPI app and WebSocket routes.
├── shared_state.py    # Shared in-memory storage for game sessions.
├── routes/
│   └── game.py        # API endpoints for creating and managing game rooms.
```

Installation
------------

1.  **Clone this repository**:

    `git clone https://github.com/yourusername/llm-dnd.git
    cd llm-dnd`

2.  **Create and activate a Python virtual environment**:

    `python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate``

3.  **Install dependencies**:

    `pip install -r requirements.txt`

4.  **Set up your `.env` file**:

    Copy the provided `.env.example` file and configure it with your OpenAI API key:

    `OPENAI_API_KEY=your_openai_api_key`

Usage
-----

1.  **Start the FastAPI server**:

    `uvicorn app.main:app --reload`

2.  **Interact with the API**:

    -   **Create a room**: `POST /create_room`
    -   **List rooms**: `GET /get_rooms`
    -   **Connect via WebSocket**: `ws://127.0.0.1:8000/ws/{room_id}`

    Players can connect to a game room via WebSocket and interact with the AI-powered Game Master.

API Endpoints
-------------

### REST Endpoints

-   **`POST /create_room`**: Create a new game room.

    -   **Request body**:

        `{
          "room_id": "room_name"
        }`

    -   **Response**:

        `{
          "message": "Room created successfully",
          "room_id": "room_name"
        }`

-   **`GET /get_rooms`**: Retrieve a list of all active game rooms.

    -   **Response**:

        `{
          "rooms": ["room1", "room2"]
        }`

### WebSocket Endpoint

-   **`/ws/{room_id}`**: Connect to a game room for real-time interactions with the AI Game Master.

Development
-----------

### Adding New Features

-   **`ai_master.py`**: Modify the Game Master's behavior, such as adjusting the initial system message or implementing more sophisticated handling of player inputs.
-   **`game_logic.py`**: Add new rules, mechanics, or state updates based on player actions.
-   **`routes/game.py`**: Add new REST API endpoints for managing game rooms or additional features.


Future Improvements
-------------------

-   **Persistence**: Add database support to persist game state across sessions.
-   **AI Customization**: Introduce fine-tuned models or allow users to configure AI responses.
-   **Authentication**: Implement player authentication and authorization for room access.
-   **UI**: Build a frontend interface for easier player interaction.
