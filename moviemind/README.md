# MovieMind

This README guides you through setting up the MovieMind project from scratch, including front-end and back-end scaffolding.

## Prerequisites

- Git  
- Node.js v18+  
- Python 3.10+  
- VS Code  
- (Optional) MongoDB Atlas account  
- (Optional) Firebase account & Web app  

## 1. Clone the Repository

```bash
git clone https://github.com/Poojith-Kotipalli/Movie_Mind.git
cd Movie_Mind

2. Front-End Setup (Next.js + Tailwind)

2.1 Create the moviemind folder

mkdir moviemind
cd moviemind

2.2 Initialize Next.js App

npx create-next-app@latest . \
  --typescript --eslint \
  --tailwind \
  --app \
  --turbopack

This will scaffold:
	•	React, Next.js, TypeScript, ESLint
	•	Tailwind CSS configuration (tailwind.config.js, postcss.config.js)
	•	app/ directory with page.tsx

2.3 Install Firebase SDK

npm install firebase

2.4 Start Development Server

npm run dev

Visit http://localhost:3000 to verify the Tailwind-powered Next.js starter page.

3. Back-End Setup (Flask)

3.1 Create the backend folder

cd ..
mkdir backend
cd backend

3.2 Set Up Python Virtual Environment

python3 -m venv venv
source venv/bin/activate        # (Windows: venv\Scripts\activate)

3.3 Install Dependencies

pip install Flask flask-pymongo dnspython flask-cors python-dotenv requests

3.4 Create app.py

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return "MovieMind API is running", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)

3.5 Run Flask Server

flask run --port=5000

Visit http://localhost:5000 to see MovieMind API is running.

4. Commit & Push

Back in the project root (Movie_Mind/):

git add .
git commit -m "chore: scaffold moviemind front-end and Flask back-end structure"
git push origin master

5. Next Steps
	•	Inside moviemind/, wire up Tailwind (if needed), Firebase Auth, and build your landing page (app/page.tsx).
	•	In backend/, add routes for /search and /quiz and connect to MongoDB Atlas.
	•	Create .env.local in moviemind/ for Firebase config, and .env in backend/ for MongoDB & TMDb keys.
	•	Open your workspace in VS Code, add both folders, install recommended extensions, and configure tasks/launch settings.

