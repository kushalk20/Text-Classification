
# 🎯 Text Classification API Service

[![FastAPI](https://img.shields.io/badge/FastAPI-0.119.0-brightgreen?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com) 
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://docker.com) 
[![Kubernetes](https://img.shields.io/badge/K8s-Deployed-purple)](https://kubernetes.io/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-orange)](https://huggingface.co/)

**Production-ready FastAPI service for BERT-based text classification** with web UI, Docker container, and Kubernetes deployment.


---

## 🚀 Features

- **BERT-base-uncased** fine-tuned with **PEFT LoRA** (0.1% trainable params)
- **FastAPI** production API with automatic Swagger docs (`/docs`)
- **Static HTML UI** for instant ticket classification
- **Docker** container with bundled 400MB model
- **Kubernetes** Deployment + LoadBalancer ready
- **5 IT Ticket Categories** - Real-world service desk data
- **BERT-base-uncased** fine-tuned on AG News dataset (5 categories)
- **400MB model** bundled with Git LFS support

---

## 📁 Repository Structure
```
.
├── app.py              # FastAPI inference API
├── index.html          # Simple web UI for calling the API
├── Dockerfile          # Docker image definition
├── deployment.yaml     # Kubernetes Deployment + Service
├── requirements.txt    # Python dependencies
├── .gitattributes      # Large file (model) handling
└── model/              # Fine-tuned BERT model
    ├── config.json
    ├── model.safetensors
    ├── special_token_map.json
    ├── tokenizer.json
    └── vocab.txt
```

## 🎯 Dataset Details

### **5 IT Support Ticket Categories**
| **Label** | **Examples** |
|-----------|--------------|
| **Urgent/Important** | "Printer down before board presentation", "VPN failed during client call" |
| **Password Change/Reset** | "Forgot password", "Account locked after 5 tries" |
| **Software Malfunction** | "Outlook crashing", "Teams won't load", "Excel frozen" |
| **Hardware Malfunction** | "Keyboard stopped", "Screen flickering", "SSD SMART errors" |
| **Others** | "Request new headset", "VPN setup help", "IT policy document" |


### **Training Details**
| **Detail** | **Value** |
|------------|-----------|
| **Base Model** | `bert-base-uncased` (110M params) |
| **Dataset** | **10K IT tickets** (2K per class) |
| **Accuracy** | **92-93%** validation accuracy |
| **Model Size** | **~425MB** (bundled in repo) |


## 🚀 Quick Start

### 1. **Local Development**
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 2. **Docker**
```
docker build -t text-classifier .
docker run -p 8000:8000 text-classifier
```

### 3. **Kubernetes**
```
kubectl apply -f deployment.yaml
kubectl get svc text-classifier-service
```

## 🔌 API Endpoints
### Health Check
```
curl http://localhost:8000/
```
```json
{"message": "API is running"}
```

### Classify IT Ticket
```
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Excel Not Working"}'
```
```json
{"Category": "Software Malfunction"}
```

## 🌐 Web Interface Demo
1. Open index.html in browser
2. Paste IT ticket text:
```text
My laptop screen went black, won't turn on
```
3. Click Classify → "Hardware Malfunction"

## 🐳 Docker Deployment
### Single command build
```
docker build -t it-ticket-classifier:latest .
docker run -p 8000:8000 it-ticket-classifier:latest
```
### Dockerfile optimized for production:
```
FROM python:3.10-slim
COPY model /app/model        # BERT model
COPY app.py requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## ☸️ Kubernetes (Production)
## Deploy with 1 command:
```
kubectl apply -f deployment.yaml
```

## 🤝 **Contributing**

1. Fork the repo
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open Pull Request


## 🙏 **Acknowledgments**
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers)** - State-of-the-art NLP models & pipelines  
- **[FastAPI](https://fastapi.tiangolo.com/)** - Production-ready API framework  
- **[PEFT](https://huggingface.co/docs/peft)** - Parameter-efficient fine-tuning (LoRA)  
- **[BERT-base-uncased](https://huggingface.co/google-bert/bert-base-uncased)** - Base model foundation  
- **[Docker](https://www.docker.com/)** - Containerization platform  
- **[Kubernetes](https://kubernetes.io/)** - Production orchestration   
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server for FastAPI  
---

<div align="center">

**⭐ Star this repo if it helped you!**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Made with-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white](https://img.shields.io/badge/Made%20with-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org)
[![Made with-FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white](https://img.shields.io/badge/Made%20with-FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Made with Docker](https://img.shields.io/badge/Made%20with-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
</div>



