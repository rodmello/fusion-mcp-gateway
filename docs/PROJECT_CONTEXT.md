# Fusion MCP Gateway — Project Context

**Document type:** Living project context  
**Status:** Active development  
**Last review:** 2026-10-19  
**Repository:** https://github.com/rodmello/fusion-mcp-gateway

## 1. Product Vision

Fusion MCP Gateway is an independent, portable, contract-driven integration platform that exposes native Oracle Fusion Cloud Applications capabilities through the Model Context Protocol (MCP).

The platform is designed to serve multiple MCP clients and connect to different customer Oracle Fusion environments through configuration rather than customer-specific code changes.

Target functional scope includes ERP, SCM, HCM, and CX.

The initial proof of concept uses Oracle Fusion ERP Payables.

## 2. Primary Product Goals

- Maintain compatibility with multiple MCP clients and AI agents.
- Support multiple Oracle Fusion instances.
- Discover and manage REST/SOAP API contracts.
- Detect differences between Oracle API releases.
- Generate candidate MCP tools from approved metadata.
- Preserve stable public MCP tool contracts.
- Enforce security, authorization, auditability, and controlled publication.
- Support deployment across different infrastructures.
- Minimize manual maintenance during Oracle quarterly updates.

## 3. Approved Architecture

ADR-001 establishes the Contract-Driven and Metadata-Driven architecture.

Main planned components:

1. Contract Discovery Engine.
2. API Contract Registry.
3. Contract Normalizer.
4. Contract Diff Engine.
5. Compatibility Resolver.
6. MCP Tool Factory.
7. Fusion REST/SOAP Adapters.
8. MCP Runtime.
9. Security and Governance.

Only some components have been implemented so far.

The architecture separates Oracle API contracts, business logic, and public MCP tool contracts.

## 4. Current Implementation

### MCP Runtime

Entry point: `server.py`

Implemented tools:

- `get_invoice`
- `search_invoices`

Both were validated using MCP Inspector.

### Payables Domain

Location: `src/fusion_mcp_gateway/payables/`

Implemented files:

- `mock_data.py`
- `service.py`
- `__init__.py`

The domain service can execute independently of MCP.

### Contract Registry

Location: `src/fusion_mcp_gateway/contracts/`

Implemented:

- `registry.py`, containing `load_contract()`.

Contracts:

- `contracts/oracle/rest/payables_invoices_v1.json`

The v1 contract is simulated and must not be treated as official Oracle metadata.

### Automated Testing

Implemented tests:

- Five Payables service tests.
- Four Contract Registry tests.

Last user-confirmed execution: nine tests passed.

## 5. Technology Stack

- Python 3.13.
- uv.
- Official MCP Python SDK 2.x.
- httpx.
- pytest.
- MCP Inspector.
- Git and GitHub.
- Windows PowerShell and VS Code.

SDK compatibility must be checked against installed dependencies.

## 6. Repository and Development

Local project directory:

`C:\Users\Rodrigo\Documents\MCP_Lab\fusion-mcp-gateway`

Git remote:

`https://github.com/rodmello/fusion-mcp-gateway.git`

Initial branch: `master`.

The repository has been pushed to GitHub.

Local changes may be newer than remote changes. Inspect Git status before making assumptions.

## 7. OCI Deployment Strategy

The approved direction is hybrid:

- Windows: development and testing.
- GitHub: version control.
- OCI Always Free: future POC runtime.

The available OCI Compute capacity is AMD Micro, with 1 GB RAM and 1/8 OCPU base.

The intended runtime is lightweight, initially without a local LLM or heavy database.

The OCI deployment has not yet been implemented.

## 8. Learning Method

The project is also a hands-on educational program.

Default mode: LEARNING.

The user executes one small step at a time and shares evidence before proceeding.

Automation is permitted only when explicitly requested.

See `AGENTS.md` for mandatory collaboration rules.

## 9. Current Milestone

Laboratory 3: Fusion API Contract Registry.

Last fully validated milestone:

- Contract Loader implemented.
- Nine automated tests passed.

Next planned task:

**Laboratory 3, Step 7 — Create a simulated Payables API contract v2 and prepare the Contract Diff Engine.**

The v2 file's current state must be verified in the repository before continuing.

## 10. Architecture and Product Risks

- Oracle REST/SOAP APIs evolve across releases.
- Metadata does not necessarily describe all business rules.
- Different Fusion tenants can expose different capabilities and permissions.
- Automatic discovery must not imply automatic publication.
- MCP clients can differ in optional-parameter handling.
- Public MCP contracts require backward-compatibility management.
- OCI Always Free imposes strict memory and compute constraints.
- Secrets and customer data must remain outside versioned source files.

## 11. Maintenance Rules

Update this document after significant project milestones.

Maintain a distinction between:

- Implemented and verified capabilities.
- Approved architecture not yet implemented.
- Planned future functionality.
- Open risks and assumptions.

Do not claim functionality is completed solely because it appears in the roadmap.

Refer to `AGENTS.md` for working instructions and `docs/adr/` for architectural decisions.