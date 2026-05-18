from core.responder import respond
from memory.chat_memory import load_memory, save_memory

memory = load_memory()

respond("FRIDAY is now online.")

while True:

    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        respond("Goodbye.")
        break

    reply = f"I received: {user_input}"

    respond(reply)

    memory.append({
        "user": user_input,
        "assistant": reply
    })

    save_memory(memory)
