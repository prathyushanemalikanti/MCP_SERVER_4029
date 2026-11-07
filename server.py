from typing import List, Dict, Union
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Hello MCP")

@mcp.tool()
def get_greeting(name: str) -> str:     
    """Return a greeting for a student."""     
    return f"Hello, {name}! Your first MCP tool works."

@mcp.tool() 
def add_numbers(a: int, b: int) -> int:     
    """Add two numbers."""     
    return a + b

@mcp.tool()
def analyze_data(numbers: List[float]) -> Dict[str, Union[float, int, str]]:
    """
    Analyze a list of numbers and return summary statistics.
    
    Handles empty lists gracefully and calculates the count, 
    minimum value, maximum value, and average.
    """
    if not numbers:
        return {
            "status": "error",
            "message": "The provided list is empty. Cannot perform analysis."
        }
        
    total_count = len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum(numbers) / total_count
    
    return {
        "status": "success",
        "count": total_count,
        "min": min_val,
        "max": max_val,
        "average": round(avg_val, 2)
    }

if __name__ == "__main__":
    mcp.run()
