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


@tool
def square(number: int) -> int:
    """
    Returns the square of a number.
    """
    return number * number


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


llm_with_tools = llm.bind_tools([
    get_current_year,
    square
])


tools = {
    "get_current_year": get_current_year,
    "square": square
}


query = input("You: ")


response = llm_with_tools.invoke(query)

print("\nAI Response:")
print(response)

print("\nTool Calls:")
print(response.tool_calls)


tool_call = response.tool_calls[0]

selected_tool = tools[
    tool_call["name"]
]

tool_result = selected_tool.invoke(
    tool_call["args"]
)

print("\nTool Result:")
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

print("\nFinal Answer:")
print(final_response.content)