# VideoHelp-AI
Transform any product page URL into stunning video advertisements with the power of AI. Create professional marketing videos in seconds.
Here’s a README.md file you can place in your backend project root directory (/BE) to help users run and test the FastAPI backend that takes a product URL and returns an AI-generated video ad.

⸻

# 🎬 VideoHelp Backend

AI-powered backend to convert product URLs into engaging video ads using FastAPI, OpenAI, and FFmpeg.

---

## 📂 Project Structure
creatify-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   ├── config.py
│   │   └── utils.py
│   ├── services/
│   │   ├── generator.py
│   │   ├── scraper.py
│   │   └── video_maker.py
│   └── models/
│       └── request.py
│
├── videos/
│
├── .env.example
├── requirements.txt
└── README.md


---

## 🛠️ Setup Instructions

### 1. Clone the Repo
gh repo clone surenaman9/VideoHelp-AI
cd VideoHelp-AI```

###2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

###3. Install Dependencies
pip install -r requirements.txt

##4. Configure Environment Variables
Rename .env.example to .env and fill in your keys:
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
