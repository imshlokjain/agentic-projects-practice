from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.tools import tool

from langchain_core.messages import (
    HumanMessage,
    ToolMessage
)

load_dotenv()


@tool
def get_current_year() -> int:
    """
    Returns the current year.
    """
    return 2026


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


llm_with_tools = llm.bind_tools(
    [get_current_year]
)


query = "What year is it?"


response = llm_with_tools.invoke(query)

print("FIRST RESPONSE")
print(response)

print("\nTOOL CALLS")
print(response.tool_calls)


tool_call = response.tool_calls[0]

tool_result = get_current_year.invoke(
    tool_call["args"]
)

print("\nTOOL RESULT")
print(tool_result)


tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)


final_response = llm_with_tools.invoke(
    [
        HumanMessage(content=query),
        response,
        tool_message
    ]
)

print("\nFINAL ANSWER")
print(final_response.content)