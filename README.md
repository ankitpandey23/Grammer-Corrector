# Grammar Corrector Chatbot

This project is a full-stack grammar correction chatbot that uses a FastAPI backend and a Next.js frontend. The backend leverages the Ollama API with a language model to correct grammar, punctuation, and clarity in user-submitted text, and provides explanations for the corrections.

## Project Structure

```
Grammer-Corrector/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── routes/
│   │       └── corrector.py
│   ├── conversation_history.json
│   └── requirement.txt
└── grammar-corrector-frontend/
    ├── src/
    │   └── app/
    │       └── ...
    └── ...
```

## Backend Workflow (`backend/app/routes/corrector.py`)

1. **API Endpoint**: The backend exposes a POST endpoint `/correct` that accepts a JSON payload with a `text` field.
2. **Prompt Construction**: The input text is formatted into a prompt asking the language model to correct grammar, punctuation, and clarity, and to explain the mistakes.
3. **Conversation History**: The prompt and all previous messages are stored in `conversation_history.json` to maintain context for the chatbot.
4. **Model Interaction**: The Ollama API is called with the conversation history, using the `llama3.2:1b` model.
5. **Response Handling**: The model's reply is split into the corrected text and an explanation. Both are returned in the API response.
6. **Persistence**: The updated conversation history is saved back to `conversation_history.json` for future requests.

## Example API Request

```
POST /correct
Content-Type: application/json

{
  "text": "He go to school every day."
}
```

**Response:**
```
{
  "corrected_text": "He goes to school every day.",
  "explanation": "The verb 'go' should be 'goes' to agree with the singular subject 'He'."
}
```

## Frontend
The frontend (in `grammar-corrector-frontend/`) is a Next.js app that provides a user interface for submitting text and displaying corrections and explanations.

## Requirements
- Python 3.10+
- FastAPI
- Ollama Python SDK
- Node.js (for frontend)

## Running the Project

1. **Backend**
   - Install dependencies: `pip install -r requirement.txt`
   - Start the FastAPI server (e.g., `uvicorn app.main:app --reload`)

2. **Frontend**
   - Install dependencies: `npm install`
   - Start the Next.js app: `npm run dev`

## Notes
- The backend uses a local file for conversation history. For production, consider using a database.
- The Ollama model must be available and running for the backend to function.
