import os
from google import genai

client = genai.Client()

# 1. Memory Loop: Active in-memory array for chat history
chat_history = []

print("[SYSTEM] Stateful AI Terminal Initialized. Type 'exit' to terminate session.\n")

# Main conversational loop 
while True:
    user_input = input("User >> ")
    
    if user_input.lower() == 'exit':
        print("\n[SYSTEM] Session terminated safely. Goodbye!")
        break
        
    # 2. Structural Validation Gate: Empty payload check
    if not user_input.strip():
        print("[GUARD] Empty payload blocked. Validation failed.\n")
        continue
        
    # 3. Ingest & Append: User input mapped to structured dictionary schema
    chat_history.append({'role': 'user', 'parts': [{'text': user_input}]})
    
    # 4. Sliding Window Algorithm: FIFO pruning to safeguard context window
    MAX_HISTORY_LIMIT = 10
    while len(chat_history) > MAX_HISTORY_LIMIT:
        chat_history.pop(0)  # Oldest message truncation
    
    # 5. Transmit & Record: Payload execution
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=chat_history
        )
        model_response = response.text
    
        chat_history.append({'role': 'model', 'parts': [{'text': model_response}]})
    
        # Display output on terminal 
        print(f"Model >> {model_response}\n")
    
    except Exception as e:
        print(f"[ERROR] API Transaction failed: {e}\n")
        if chat_history:
            chat_history.pop()