import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="The prompt to send to the LLM")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
prompt = args.prompt
messages = types.Content(role="user", parts=[types.Part(text=prompt)])

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")


client = genai.Client(api_key=api_key)
prompt_token_count = 0
candidiate_token_count = 0

llm_response = client.models.generate_content(model='gemini-2.5-flash',contents=messages)

if llm_response.usage_metadata is None:
    raise RuntimeError("No usage metadata returned from the API.")
else:
    prompt_token_count = llm_response.usage_metadata.prompt_token_count
    candidiate_token_count = llm_response.usage_metadata.candidates_token_count

if args.verbose:
    print(f'User prompt: {prompt}')
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidiate_token_count}") 

print(f'Response:\n{llm_response.text}')


