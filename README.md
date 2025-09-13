# Hackathon OCR Project 🏆
OCR + Backend + Cloud + Deployment

## 📂 Project Structure
- `backend/` → FastAPI backend (auth, prescriptions, reminders, OCR API integration)
- `ocr/` → OCR model & inference scripts
- `deploy/` → Docker / cloud deployment files (to be added)
- `.env.example` → Example environment variables
- `.gitignore` → Ignore unnecessary files (cache, models, secrets)

## 🚀 How to Run
### 1. Clone repo
```bash
git clone https://github.com/anshii8765-ui/hackathon-ocr-project.git
cd hackathon-ocr-project
cp .env.example .env
# edit .env and add DB, secret key, etc.
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5000
cd ocr
pip install -r requirements.txt
python inference.py --input tests/sample.jpg
### 6. Deployment (Cloud/Docker)
Once deployment files are ready in the `deploy/` folder, run:

```bash
cd deploy
docker-compose up
