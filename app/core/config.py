import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VIDEO_DIR = os.path.join(os.getcwd(), "videos")