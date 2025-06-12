# AI-CHATBOT-WITH-NLP_TASK3

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ATHARVA PARESH CHALKE

*INTERN ID*: CT04DL947

*DOMAIN*:  PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

# Wikipedia Query Bot with NLP (Spacy)

This Python project simplifies factual question-answering by fetching concise Wikipedia summaries using natural language processing (NLP).The bot processes user queries, identifies key topics with Spacy and returns relevant information—ideal for quick research or learning.At its core, the system uses Spacy’s NLP model (en_core_web_sm) to analyze input text and extract key nouns or noun phrases (e.g., "Mumbai," "Quantum Physics"). These terms trigger a Wikipedia search via the wikipedia library which returns a summarized response in four sentences.The bot intelligently filters noise by focusing only on meaningful keywords, ensuring precise results.For example, a query like "Explain machine learning" retrieves a summary about ML, while vague terms like "Apple" prompt the user to clarify.

The project implements robust error handling to manage various real-world scenarios. When faced with ambiguous terms like "Python" (which could refer to the programming language or the snake), the system detects multiple possible meanings and prompts the user to refine their query. Similarly, if a requested topic doesn't exist in Wikipedia's database, the bot provides a polite notification rather than failing silently. These thoughtful touches create a more polished and user-friendly experience.The loop runs interactively until the user types "exit" or "quit," ending with a "Sayonara!".The Program demonstrates several important programming concepts.The continuous while loop allows for ongoing conversation until the user explicitly exits.The input processing converts all text to lowercase for case-insensitive matching, making the bot more forgiving of formatting variations. The output formatting ensures clean, readable responses every time.

*OUTPUT:*

![Image](https://github.com/user-attachments/assets/60e3e653-6b25-4629-96f8-110dcb355fd0)

Since the bot for now works on searching the keyword provided via a Wikipedia search, it can be inaccurate or even cause errors if multiple faactor comparision is done.

![Image](https://github.com/user-attachments/assets/999c33e8-fb94-4e75-8e95-3ed21f46e16c)




