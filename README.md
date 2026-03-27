# AI/ML OCR Project 🏆  
OCR + Backend + Cloud + Deployment  

## 📂 Project Structure  
- `backend/` → FastAPI backend (auth, prescriptions, reminders, OCR API integration)  
- `ocr/` → OCR model & inference scripts  
- `deploy/` → Docker / cloud deployment files (to be added)  
- `.env.example` → Example environment variables  
- `.gitignore` → Ignore unnecessary files (cache, models, secrets)  

---

## 🚀 How to Run  

### 1. Clone repo  
```bash
git clone https://github.com/anshii8765-ui/hackathon-ocr-project.git
cd hackathon-ocr-project
### 2. Setup environment  
```bash
cp .env.example .env
# Edit .env and add DB, secret key, etc.
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5000
cd ../ocr
pip install -r requirements.txt
python inference.py --input tests/sample.jpg
### 5. Deployment (Cloud/Docker)  
Once deployment files are ready in the `deploy/` folder, run the following commands:

```bash
cd ../deploy
docker-compose up

---

⚡ So basically:  
- `cd ../deploy` → move into the deployment folder.  
- `docker-compose up` → runs everything together using Docker.  
---

## 🛠 Tech Stack
- **Backend**: FastAPI (Python)  
- **AI/OCR**: Custom OCR model, inference scripts (PyTorch/TensorFlow)  
- **Database**: PostgreSQL (or SQLite for testing)  
- **Deployment**: Docker & Docker-Compose (Cloud-ready)  
- **Version Control**: Git & GitHub  

---

## ✨ Features
- 📄 **Prescription Upload** → Extracts text using OCR model  
- ⏰ **Reminders** → For medicines and health tasks  
- 🔐 **Authentication** → Secure user login and data handling  
- ☁️ **Cloud Ready** → Easy deployment with Docker  
- 📊 **Scalable Design** → Can integrate AI/ML APIs in future  

---

## 🚀 Future Scope
- 📱 Build a **Mobile App** for patients & doctors  
- 🤖 Integrate **Advanced AI/ML** for more accurate OCR and health predictions  
- 🌐 Add **Multi-language OCR** support  
- 🔔 Push **Notifications** for medicine reminders  
- 🏥 Integration with **Hospital Systems** for e-prescriptions  

---
---

## 🎥 Demo
📌 Screenshots / Demo video link will be added here.  

- **Backend API running** → screenshot of FastAPI docs (`/docs`)  
- **OCR in action** → screenshot of text extraction from prescription  
- **Deployment** → screenshot of container running (Docker)  
