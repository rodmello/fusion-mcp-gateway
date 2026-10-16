
from mcp.server import MCPServer

# Cria nosso servidor MCP
mcp = MCPServer("Fusion MCP Gateway")


@mcp.tool()
def hello_fusion(name: str) -> str:
    """Retorna uma mensagem de boas-vindas."""
    return f"Olá, {name}! Fusion MCP Gateway funcionando."


if __name__ == "__main__":
    mcp.run()
