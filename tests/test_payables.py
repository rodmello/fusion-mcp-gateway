
from fusion_mcp_gateway.payables import service


def test_get_invoice_existing():
    result = service.get_invoice(1001)

    assert result["found"] is True
    assert result["invoice"]["invoice_number"] == "INV-2026-001"


def test_get_invoice_not_found():
    result = service.get_invoice(9999)

    assert result["found"] is False


def test_search_invoices_without_filters():
    result = service.search_invoices()

    assert result["count"] == 2


def test_search_invoices_by_supplier():
    result = service.search_invoices(supplier="ABC")

    assert result["count"] == 1
    assert result["invoices"][0]["invoice_id"] == 1001


def test_search_invoices_empty_strings():
    result = service.search_invoices(supplier="", status="")

    assert result["count"] == 2
