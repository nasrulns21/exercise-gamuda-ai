import random

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Dice Roller")


@mcp.tool()
def roll_dice(n_dice: int) -> list[int]:
    """Roll between one and ten six-sided dice."""
    if not 1 <= n_dice <= 10:
        raise ValueError("n_dice must be between 1 and 10")
    return [random.randint(1, 6) for _ in range(n_dice)]


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
