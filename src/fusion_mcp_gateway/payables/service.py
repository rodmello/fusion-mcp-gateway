
from .mock_data import MOCK_INVOICES


def get_invoice(invoice_id: int) -> dict:
    """Consulta uma fatura pelo identificador."""
    invoice = MOCK_INVOICES.get(invoice_id)

    if invoice is None:
        return {
            "found": False,
            "message": f"Fatura {invoice_id} não encontrada."
        }

    return {
        "found": True,
        "invoice": invoice
    }


def search_invoices(
    supplier: str | None = None,
    status: str | None = None,
) -> dict:
    """Pesquisa faturas utilizando filtros opcionais."""
    supplier = (supplier or "").strip()
    status = (status or "").strip().upper()

    results = []

    for invoice in MOCK_INVOICES.values():
        if supplier:
            if supplier.lower() not in invoice["supplier"].lower():
                continue

        if status:
            if invoice["status"].upper() != status:
                continue

        results.append(invoice)

    return {
        "count": len(results),
        "invoices": results
    }
