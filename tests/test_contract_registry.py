
from pathlib import Path

import pytest

from fusion_mcp_gateway.contracts.registry import load_contract


CONTRACT_FILE = (
    Path(__file__).resolve().parents[1]
    / "contracts"
    / "oracle"
    / "rest"
    / "payables_invoices_v1.json"
)


def test_load_valid_contract():
    contract = load_contract(CONTRACT_FILE)

    assert contract["contract_id"] == "fusion.erp.payables.invoices"
    assert contract["contract_version"] == "1.0.0"
    assert len(contract["resource"]["operations"]) == 1


def test_contract_file_not_found(tmp_path):
    nonexistent_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_contract(nonexistent_file)


def test_contract_missing_required_fields(tmp_path):
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text(
        '{"contract_id": "test"}',
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError, match="Campos obrigatórios ausentes"
    ):
        load_contract(invalid_file)


def test_contract_invalid_json(tmp_path):
    invalid_file = tmp_path / "broken.json"
    invalid_file.write_text(
        '{"contract_id": ',
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_contract(invalid_file)
