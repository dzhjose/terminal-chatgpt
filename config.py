import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY", "")
