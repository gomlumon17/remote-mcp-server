from random import randint
from fastmcp import FastMCP

mcp = FastMCP("Demo Server")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b


@mcp.tool()
def generate_random_number() -> int:
    """
    Generate a random number between 1 and 100
    """
    return randint(1, 100)


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)