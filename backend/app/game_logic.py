from backend.app.ai_master import get_game_master_response

def handle_player_action(action: str, session_state: dict) -> str:
    """
    Handle the player's action, update the game state, and return a response.
    """
    if not action.strip():
        return "Invalid action. Please provide a valid action."

    # Use AI Game Master to generate a response
    ai_response = get_game_master_response(action)
    
    # Update the session state (can be expanded later)
    session_state["last_action"] = action

    return ai_response

