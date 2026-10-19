# AGENTS.md — Fusion MCP Gateway

## Required Project Context

Before proposing implementation or making changes:

1. Read `docs/PROJECT_CONTEXT.md` to understand the product vision, architecture and current implementation.
2. Read `docs/LEARNING_ROADMAP.md` to identify verified milestones and the next laboratory.
3. Review relevant Architecture Decision Records in `docs/adr/`.
4. Inspect the actual repository state and reconcile it with the documentation.
5. If documentation and repository contents disagree, report the discrepancy before proceeding.

These documents provide persistent project context, but must not override the user's explicit instructions or the verified state of the repository.

In LEARNING mode, read and explain first. Do not modify files or execute implementation commands without explicit authorization.

## Project Mission

Build a portable, secure, contract-driven MCP Gateway for Oracle Fusion Cloud Applications.

The product must support multiple Oracle Fusion customer environments, different MCP clients, and progressive expansion across ERP, SCM, HCM, and CX.

The initial proof of concept focuses on Oracle Fusion ERP Payables.

## Mandatory Working Mode: LEARNING

The default interaction mode is **LEARNING**.

The user is learning software architecture and engineering by building the product hands-on.

Rules:

1. Explain the concept before proposing implementation.
2. Work in small, independently verifiable steps.
3. Provide commands for Windows PowerShell unless another environment is explicitly selected.
4. Let the user execute commands and share their results.
5. Wait for validation before advancing to the next step.
6. Do not edit files or execute implementation commands without explicit authorization.
7. Diagnose errors using evidence before suggesting corrections.
8. State expected results and acceptance criteria.
9. Use automated tests whenever practical.
10. Propose Git commits at meaningful checkpoints, but request authorization before executing Git write operations.

Do not execute an entire laboratory autonomously.

## Optional Working Mode: AUTOMATION

The user may explicitly activate **AUTOMATION** mode.

Only in this mode may the agent implement approved changes, edit files, and run authorized commands.

Before implementing, summarize the intended scope.

After implementing, report:

- Files modified.
- Design decisions.
- Tests executed and their results.
- Risks and limitations.
- Recommended next steps.

Never interpret access to the repository as authorization to modify it.

## Architecture Principles

Follow ADR-001: Contract-Driven Architecture.

Key principles:

- Separate MCP transport and tools from business logic.
- Separate Oracle API contracts from MCP tool contracts.
- Maintain a versioned API Contract Registry.
- Discover REST/SOAP metadata from supported Oracle sources.
- Detect differences between contract versions.
- Generate candidate MCP tools from validated metadata.
- Publish tools only after compatibility and security checks.
- Prefer read-only capabilities during initial development.
- Preserve stable public MCP contracts when Oracle APIs evolve.
- Support configuration-driven connectivity to different Fusion environments.
- Avoid customer-specific logic in the core platform.

## Oracle Fusion Integration Rules

- Prefer Oracle-supported standard APIs and integration mechanisms.
- Never invent Oracle API endpoints, attributes, parameters, privileges, or operations.
- Validate API behavior against official documentation and actual environment capabilities.
- Clearly distinguish mock contracts from official Oracle metadata.
- Consider quarterly release compatibility.
- Respect Oracle Fusion authorization and data security.
- Do not expose unrestricted arbitrary REST/SOAP execution tools to agents.
- Require explicit controls for operations that create, modify, approve, release, or delete business data.

## Technical Stack

- Python 3.13 development environment.
- `uv` dependency management.
- MCP Python SDK 2.x.
- `MCPServer` from `mcp.server.mcpserver`.
- `httpx` for REST integrations.
- `pytest` for automated testing.
- Git and GitHub for version control.
- MCP Inspector for protocol-level tests.

Use the installed SDK documentation and project lockfile as the source of truth for API compatibility.

## Repository Structure

The current architecture includes:

- `server.py`: MCP tools and server entry point.
- `src/fusion_mcp_gateway/payables/`: Payables domain module.
- `src/fusion_mcp_gateway/contracts/`: Contract Registry implementation.
- `contracts/oracle/`: Versioned Oracle API contract snapshots.
- `tests/`: Automated tests.
- `docs/adr/`: Architecture Decision Records.

Inspect the actual repository before assuming additional files exist.

## Testing and Quality

- Preserve existing behavior during refactoring.
- Run `uv run pytest -v` when validating code changes.
- Add unit tests for new business rules and contract-processing functions.
- Introduce integration and protocol tests as the architecture evolves.
- Never claim tests passed unless they were actually executed or the user provided evidence.
- Do not modify existing tests merely to make failing implementation code pass.
- Validate that credentials and sensitive information are not included in commits.

## Git and Change Management

Repository: https://github.com/rodmello/fusion-mcp-gateway

The initial branch is `master`.

- Inspect `git status` before proposing modifications.
- Preserve uncommitted user changes.
- Do not force-push, reset, rebase, discard changes, or rewrite history without explicit approval.
- Ask permission before commits or pushes.
- Use descriptive commit messages.
- Prefer small, reviewable changes.

## OCI Deployment Strategy

The target POC architecture is hybrid:

- Windows: development, debugging, and testing.
- GitHub: version control.
- OCI Always Free: deployment and runtime validation.

The realistically available OCI Compute shape is AMD Micro with 1 GB RAM and 1/8 OCPU base.

Optimize the runtime for low memory consumption.

Do not assume Ampere A1 availability.

Avoid heavy local databases, local LLMs, and unnecessary background services in the initial OCI deployment.

Use secure configuration, least-privilege access, protected secrets, and controlled network exposure.

## Current Learning Roadmap

Before proposing the next implementation step:

1. Inspect the current repository state.
2. Review relevant ADRs and existing tests.
3. Identify the last verified laboratory milestone.
4. Confirm the next step with the user.
5. Proceed in LEARNING mode unless explicitly instructed otherwise.

The last verified milestone before the Codex handoff was:

- MCP server functioning.
- `get_invoice` and `search_invoices` tools validated.
- Payables module refactored.
- Contract Loader implemented.
- Nine automated tests passing.

The next planned activity was **Laboratory 3, Step 7: Create a simulated v2 Payables API contract and prepare the Contract Diff Engine**.

This milestone is historical context; inspect the repository and conversation before assuming it remains current.

## Communication

- Respond in Brazilian Portuguese.
- Use concise, structured, implementation-oriented explanations.
- Explain why each technical step matters.
- Distinguish verified facts, assumptions, and future architecture.
- Favor practical learning over unexplained code generation.

The goal is not merely to finish the software quickly.

**The goal is to learn by building a real, supportable engineering product.**