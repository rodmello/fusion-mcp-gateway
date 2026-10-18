
from mcp.server.mcpserver import MCPServer

from fusion_mcp_gateway.payables import service


mcp = MCPServer("Fusion MCP Gateway")


@mcp.tool()
def get_invoice(invoice_id: int) -> dict:
    """Consulta uma fatura simulada do Oracle Fusion Payables."""
    return service.get_invoice(invoice_id)


@mcp.tool()
def search_invoices(
    supplier: str | None = None,
    status: str | None = None,
) -> dict:
    """Pesquisa faturas simuladas por fornecedor e status."""
    return service.search_invoices(supplier, status)


if __name__ == "__main__":
    mcp.run()
