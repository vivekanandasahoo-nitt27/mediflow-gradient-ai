# 🩺 AI Medical Agent — Multimodal Diagnosis & Smart Appointment System

## ⚡ Quick Access for Judges
- 🔓 This repository is **public and open-source (MIT License)** — visible in the GitHub About section.
- 🚀 The project can be tested instantly via live demo or locally using the steps below.


### 🚀 Option 1: Use Live Demo (Recommended)
http://152.42.182.113/

### 💻 Option 2: Run Locally (2 minutes setup)

git clone https://github.com/vivekanandasahoo-nit27/mediflow-gradient-ai.git  
cd mediflow-gradient-ai  
pip install -r requirements.txt  
python app.py  

Open in browser: http://localhost:7860




An end-to-end **Multimodal Healthcare AI Agent** that analyzes **voice, medical images, and text** to predict diseases, generate reports, and enable intelligent clinical appointment booking.

Built using **DigitalOcean Gradient AI + Droplets + Spaces**, this system provides a **real-world AI-powered healthcare workflow**.

---

## 🚀 Live Demo

🌐 **Live App:** http://152.42.182.113/  
☁️ **Hosted on:** DigitalOcean Droplet  
📦 **Model Storage:** DigitalOcean Spaces  
🐳 **Deployment:** Docker Container  
🖥️ **Interface:** Gradio Web UI  

---

## 🧠 What This Project Does

This AI system acts as a **multilingual virtual doctor assistant** that can:

- 🎙️ Understand patient speech in multiple languages  
- 🌍 Automatically respond in the same language as the patient  
- 🗣️ Generate realistic doctor-like voice responses (Text-to-Speech)  
- 🖼️ Analyze medical images (X-ray, MRI, ultrasound)  
- 💬 Provide AI-based diagnosis & conversational guidance  
- 📄 Generate structured medical reports (PDF)  
- 📅 Enable smart clinical appointment booking  
- 📧 Send reports to both patient and doctor  

👉 The system ensures **natural, human-like interaction**, making it accessible even for non-technical or rural users.

---

## 🏥 New Feature (Key Highlight)

### 🔬 AI-Powered Medical Image Diagnosis + Appointment System

Patients can:

1. Upload medical images:
   - Brain MRI (Tumor detection)
   - Kidney scans
   - Pneumonia X-rays
   - Fracture detection

2. AI performs:
   - Disease classification  
   - Severity scoring  
   - Clinical reasoning  

3. System generates:
   - 📄 Final medical report (PDF)
   - 🧠 AI diagnosis summary
   - 📊 Severity score
   - 🖼️ Image + prediction

4. Automatically:
   - 📧 Sends report to patient & doctor
   - 📅 Suggests and books appointment

👉 This directly assists doctors in **pre-diagnosis and prioritization**

---

## 🤖 Core Features

### 🧠 Multimodal AI Consultation
- Voice + Image + Text understanding
- LLM-powered medical reasoning

## 🌍 Multilingual & Voice Intelligence (Key Innovation)

- Supports **multi-language speech input**
- Automatically detects language
- Responds in **same language as user**
- Provides **realistic doctor voice output**
- Enables accessibility for:
  - Non-English users
  - Rural healthcare scenarios
  - Low-literacy environments

👉 This makes the system usable beyond urban/English-speaking populations.

### 📄 Medical Report Generation
- Auto-generated structured PDF reports
- Stored per user
- Download + history tracking

### 📊 Health Dashboard
- Track reports and health metrics
- Historical insights

### 📅 Smart Appointment Booking
- AI suggests appointments based on severity
- Slot selection system
- Doctor-side assistance

### 📧 Email Automation
- Sends:
  - Appointment confirmation
  - AI-generated medical report
- Powered by SendGrid

### 🔐 Authentication System
- User login/signup
- Personalized medical history

---

## 🧠 AI Architecture
User Input (Voice/Image/Text)
↓
Agent Router
↓
Multimodal AI Reasoning
↓
Report Generation + Prediction
↓
Appointment + Email System

---

## ⚙️ Tech Stack

### 💻 Core
- Python
- Gradio
- Docker

### 🤖 AI / ML
- Groq (LLaMA models)
- OpenAI Embeddings
- FAISS Vector Database
- TensorFlow / Keras
- Computer Vision Models

### 🎤 Multimodal
- Whisper (Speech-to-Text)
- ElevenLabs (Text-to-Speech)

### 🗄️ Backend
- SQLAlchemy
- SQLite

### ☁️ Cloud (IMPORTANT)
- **DigitalOcean Droplet (App Hosting)**
- **DigitalOcean Spaces (Model Storage)**
- Docker Deployment

### 📡 APIs
- SendGrid (Email)

---


---

## 🐳 Docker Deployment

```bash
docker build -t mediflow-ai .
docker run -d -p 80:7860 --env-file .env mediflow-ai
```
## 🔑 Environment Setup

Create a `.env` file using the following format:

GROQ_API_KEY=your_key  
OPENAI_API_KEY=your_key  
ELEVEN_API_KEY=your_key  
SENDGRID_API_KEY=your_key  

⚠️ Note: If API keys are not provided, please use the live demo for testing.

## 👨‍💻 Author

Vivekananda Sahoo
AI Medical Agent — Multimodal Diagnosis & Smart Appointment System
Built for DigitalOcean Gradient AI Hackathon 