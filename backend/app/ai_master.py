from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Load the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set. Set OPENAI_API_KEY in a .env file or as an environment variable.")

# Initialize OpenAI Chat LLM
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    model="gpt-3.5-turbo",  # Specify the desired model (e.g., gpt-4 or gpt-3.5-turbo)
)

def get_game_master_response(player_input: str) -> str:
    """
    Generate a response from the AI Game Master based on the player's input.
    """
    if not player_input.strip():
        return "Please provide a valid input for the Game Master."

    # Define the system message and user input
    system_message = (
        "You are an expert Dungeons & Dragons Game Master. Respond to the player's input in a detailed, "
        "immersive, and engaging manner, following D&D rules and storytelling principles."
    )
    user_message = player_input

    # Attempt to get a response from the AI
    try:
        response = llm.predict_messages(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ]
        )
        return response["content"]  # Extract the content from the response
    except Exception as e:
        return f"An error occurred while generating a response: {str(e)}"

