from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

from llm import llm


# ==================================================
# PROMPT FOR REWRITING CONVERSATIONAL QUESTIONS
# ==================================================

rewrite_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a question rewriting assistant for a PDF
question-answering system.

Your job is to rewrite the user's CURRENT question into a
standalone question that can be used to search the PDF.

Use the conversation history to resolve references such as:

- "it"
- "that"
- "this"
- "the first one"
- "the second one"
- "the previous topic"
- "the next one"

IMPORTANT RULES:

1. Identify the topic currently being discussed in the conversation.

2. Preserve that topic when resolving references.

3. If the user says "the first one", "the second one", etc.,
   interpret it relative to the list currently being discussed.

4. Do NOT switch to another section of the document unless
   the user explicitly changes the topic.

5. Do NOT answer the question.

6. Return ONLY the rewritten standalone question.

Example 1:

Conversation:
User: What topics are covered under Stability?
Assistant: The topics are Definition, Routh-Hurwitz criterion,
Root locus techniques, Nyquist criterion, and Bode plots.

User: Explain the first one.

Output:
Explain the definition of stability in control systems.


Example 2:

Conversation:
User: What topics are covered under Stability?
Assistant: The topics are Definition, Routh-Hurwitz criterion,
Root locus techniques, Nyquist criterion, and Bode plots.

User: Explain the first one.
Assistant: The definition of stability...

User: What about the second one?

Output:
Explain the Routh-Hurwitz criterion under Stability.


Example 3:

Conversation:
User: What topics are covered under State Space Analysis?
Assistant: The topics include state variables, state models,
state space equations, transfer function, controllability,
and observability.

User: Explain the last one.

Output:
Explain observability in the context of State Space Analysis.

"""
    ),
    (
        "human",
        """Conversation history:

{chat_history}

Current question:

{question}"""
    )
])


# ==================================================
# FORMAT CHAT HISTORY
# ==================================================

def format_chat_history(chat_history):

    formatted_history = []

    for message in chat_history:

        if isinstance(message, HumanMessage):

            formatted_history.append(
                f"User: {message.content}"
            )

        elif isinstance(message, AIMessage):

            formatted_history.append(
                f"Assistant: {message.content}"
            )

    return "\n\n".join(formatted_history)


# ==================================================
# REWRITE QUESTION
# ==================================================

def rewrite_question(question, chat_history):

    formatted_history = format_chat_history(
        chat_history
    )

    messages = rewrite_prompt.invoke(
        {
            "chat_history": formatted_history,
            "question": question
        }
    )

    response = llm.invoke(
        messages
    )

    return response.content.strip()