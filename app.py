from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import uvicorn
import os

# Dataset used to Fine Tune the model: AG News Dataset (https://huggingface.co/datasets/fancyzhx/ag_news)
# Model used to Fine Tune: bert-base-uncased (https://huggingface.co/google-bert/bert-base-uncased)

# Initialize FastAPI app
app = FastAPI(title="Text Classification API")

# Model Path
model_path = os.path.join(os.getcwd(), "model")

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=5)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Define request body structure
class TextRequest(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return {"message": "API is running"}

@app.post("/predict")
async def predict(request: TextRequest):
    text = request.text.strip()
    if not text:
        return {"error": "No text provided"}
    
    result = classifier(request.text)[0]['label']
    return {"Category": result}

# For local testing
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)