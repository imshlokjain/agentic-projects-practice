from langchain_core.tools import tool


@tool
def square(number: int) -> int:
    """
    Returns the square of a number.
    """
    return number * number


print(square.invoke({"number": 5}))