
import json
from pathlib import Path


REQUIRED_FIELDS = (
    "contract_id",
    "contract_version",
    "source",
    "resource",
)


def load_contract(file_path: str | Path) -> dict:
    """Carrega um contrato JSON do Fusion API Contract Registry."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Arquivo de contrato não encontrado: {path}"
        )

    with path.open("r", encoding="utf-8-sig") as file:
        contract = json.load(file)

    if not isinstance(contract, dict):
        raise ValueError(
            "O contrato deve ser um objeto JSON."
        )

    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in contract
    ]

    if missing_fields:
        raise ValueError(
            f"Campos obrigatórios ausentes: {missing_fields}"
        )

    return contract
