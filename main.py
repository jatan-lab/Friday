from core.responder import respond
from memory.chat_memory import load_memory, save_memory
from ai.brain import get_ai_response

memory = load_memory()

respond("FRIDAY AI Core is now online.")

while True:

    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        respond("Goodbye.")
        break

    # 🧠 AI RESPONSE
    reply = get_ai_response(user_input)

    respond(reply)

    # 💾 SAVE MEMORY
    memory.append({
        "user": user_input,
        "assistant": reply
    })

    save_memory(memory)
