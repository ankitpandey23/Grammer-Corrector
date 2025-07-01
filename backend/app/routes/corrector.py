import os
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import ollama

router = APIRouter()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    corrected_text: str
    explanation: str

# Load or initialize conversation history
history_file = "conversation_history.json"
if os.path.exists(history_file):
    with open(history_file, 'r') as f:
        try:
            conversation_history = json.load(f)
        except json.JSONDecodeError:
            conversation_history = []
else:
    conversation_history = []

@router.post("/correct", response_model=TextResponse)
async def correct_text(req: TextRequest):
    prompt = f"Correct the following sentence for grammar, punctuation, and clarity explain the mistakes: {req.text}"
    conversation_history.append({'role': 'user', 'content': prompt})

    try:
        response = ollama.chat(
            model='llama3.2:1b',
            messages=conversation_history
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")

    reply = response['message']['content'].strip()
    conversation_history.append({'role': 'assistant', 'content': reply})

    # Save history
    with open(history_file, 'w') as f:
        json.dump(conversation_history, f, indent=2)

    # Assume the model returns response in "✅ corrected\n\n📝 explanation" format
    if "\n\n" in reply:
        corrected_text, explanation = reply.split("\n\n", 1)
    else:
        corrected_text = reply
        explanation = "Explanation could not be parsed."

    return {"corrected_text": corrected_text, "explanation": explanation}
 