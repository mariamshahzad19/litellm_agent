import os
from litellm import completion
from dotenv import load_dotenv


# Load your Gemini API key from .env
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from your .env file.")

    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            { "role": "user","content" :  " Who is einstin?"}
        ],
        api_key=api_key


    )
    print(response['choices'][0]['message']['content'])

if __name__ =="__main__":
    main()