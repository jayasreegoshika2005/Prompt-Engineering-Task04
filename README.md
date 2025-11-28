# Prompt-Engineering-Task04
"SkillCraft Technology Task-04-Simulating an Assistant
# Task 04 – Simulating an Assistant

This project creates a simple persona-based assistant (a friendly study tutor).  
It responds based on keywords and simulates a natural conversation across multiple turns.

---

## Files Included
1. *assistant.py* – The simulated assistant code.
2. *conversation_log.txt* – A sample conversation.
3. *README.md* – Documentation and explanation.

---

## Assistant Flow (Step-by-step)
1. Start with a fixed *system prompt*:  
   - “You are a friendly study assistant.”
2. The user types a message.
3. The assistant checks if keywords exist:  
   - “help” → assistant gives help  
   - “python” → gives Python explanation  
   - “ml” → gives Machine Learning explanation  
4. If no keywords match, the assistant gives a general helpful reply.
5. Conversation continues until the user types exit.

---

## Improvements Made
- Added keyword matching for consistent responses.
- Limited the assistant to short, simple replies.
- Ensured persona consistency (friendly study assistant).
- Added a conversation log to verify behavior.

---

## How to Run
