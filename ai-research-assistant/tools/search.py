from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()


@tool
def search_web(query: str) -> str:
    """
    Search the web for current information.
    """
    return search.run(query)


if __name__ == "__main__":
    result = search_web.invoke(
        {
            "query": "Messi"
        }
    )

    print(result)