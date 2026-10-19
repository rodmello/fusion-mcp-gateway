# Fusion MCP Gateway — Learning Roadmap

**Status:** Active  
**Last updated:** 2026-10-19  
**Working mode:** LEARNING  
**Repository:** https://github.com/rodmello/fusion-mcp-gateway

## 1. Learning Philosophy

The Fusion MCP Gateway is both a software product and a hands-on learning project.

The objective is to understand architecture, protocols, integration, security, cloud infrastructure, and software engineering by implementing real components incrementally.

The default workflow is:

**Understand → Implement → Execute → Validate → Document → Commit**

In LEARNING mode, the user executes each step manually. The agent must wait for validation before advancing.

AUTOMATION mode may be activated explicitly for familiar tasks.

See `AGENTS.md` for mandatory instructions.

## 2. Completed Laboratories

### Laboratory 1 — MCP Fundamentals

**Status: COMPLETED**

Implemented and validated:

- Windows development environment.
- Python, uv, Git, Node.js, npm and VS Code.
- First MCP Server using Python SDK 2.x.
- MCP Inspector connectivity.
- `hello_fusion` tool discovery and execution.
- Understanding of `tools/list`, `tools/call` and JSON-RPC 2.0.
- First Git commit.

### Laboratory 2 — Fusion Payables MCP Tools

**Status: COMPLETED**

Implemented and validated:

- `get_invoice` with simulated Payables data.
- `search_invoices` with optional filters.
- Error handling for nonexistent invoices.
- Handling of empty strings submitted by MCP clients.
- Separation of MCP server, business service and mock data.
- Five automated pytest tests.
- GitHub remote configured and initial push completed.

Key learning: MCP tool contracts should remain independent of their implementation.

### Laboratory 3 — API Contract Registry

**Status: IN PROGRESS**

Verified milestones:

- Contract-Driven Architecture approved as ADR-001.
- Contract Registry folders created.
- Simulated Payables contract v1 created.
- Contract Loader implemented.
- Four automated Contract Registry tests passed.
- Full test suite: nine tests passed.

Next planned milestone:

**Step 7 — Create a simulated Payables contract v2 and prepare the Contract Diff Engine.**

Planned v2 changes:

1. `contract_version`: `1.0.0` → `1.1.0`.
2. Add `due_date` to the invoice response.
3. Add the `search_invoices` operation.

Expected v2 validation:

- Two operations.
- Seven attributes in the `get_invoice` response.
- Valid JSON.

Do not assume the v2 contract is complete without inspecting the repository and validating its contents.

## 3. Upcoming Laboratories

### Laboratory 4 — Contract Diff Engine

**Status: PLANNED**

- Compare contract versions.
- Detect added and removed operations.
- Detect added, removed and changed attributes.
- Produce structured difference reports.
- Implement automated tests.
- Begin compatibility classification.

### Laboratory 5 — Oracle REST Metadata Discovery

**Status: PLANNED**

- Study Oracle Fusion REST `/describe`.
- Retrieve supported API metadata.
- Examine OpenAPI representations.
- Store immutable contract snapshots.
- Record provenance, release and capture timestamps.
- Normalize Oracle metadata into our internal model.

### Laboratory 6 — MCP Tool Factory

**Status: PLANNED**

- Generate candidate tool definitions from metadata.
- Map API parameters to MCP input schemas.
- Maintain stable public tool contracts.
- Validate generated tools.
- Implement approval and publication policies.

### Laboratory 7 — OCI Always Free Deployment

**Status: PLANNED**

- Provision an AMD Micro Compute instance.
- Configure Linux and Python.
- Deploy the repository from GitHub.
- Run the MCP server under systemd.
- Measure memory and CPU consumption.
- Introduce secure remote MCP connectivity.
- Validate operational recovery.

Infrastructure constraint: AMD Micro, 1 GB RAM, 1/8 OCPU base.

### Laboratory 8 — Real Oracle Fusion Payables Integration

**Status: PLANNED**

- Configure a TEST/DEV Fusion connection.
- Study authentication and authorization.
- Consume real Payables REST APIs.
- Add pagination, errors, retries and observability.
- Validate access restrictions.
- Map real REST responses to stable tool contracts.

### Laboratory 9 — SOAP and Extended Discovery

**Status: PLANNED**

- Study SOAP WSDL and XSD.
- Explore Oracle service discovery mechanisms.
- Add SOAP adapter capabilities.
- Compare REST and SOAP contracts.
- Introduce contract-change detection across releases.

### Laboratory 10 — Product Hardening

**Status: PLANNED**

- Multi-instance configuration.
- Tool registry and capability packs.
- Security and governance.
- MCP protocol-level regression tests.
- Version compatibility.
- Packaging and release procedures.
- Documentation and reproducible deployment.

## 4. Development Milestone Rules

Each milestone should have:

- A clear learning objective.
- A defined implementation scope.
- Executable commands.
- Expected results.
- Positive and negative tests.
- Evidence of completion.
- A Git commit when appropriate.

A milestone is considered completed only after successful validation.

## 5. Architecture Decisions

Approved:

- **ADR-001:** Contract-Driven Architecture.
- Hybrid Windows + GitHub + OCI Always Free deployment direction.

Pending documentation:

- **ADR-002:** Hybrid Development and OCI Always Free Deployment.

## 6. Documentation Responsibilities

- `AGENTS.md` defines how the agent collaborates.
- `PROJECT_CONTEXT.md` describes product vision and current state.
- `LEARNING_ROADMAP.md` describes the learning sequence and verified milestones.
- `docs/adr/` records architectural decisions.
- `README.md` will describe product installation and usage.

## 7. Current Resumption Point

Resume from:

**Laboratory 3 — Step 7: Simulated Payables Contract v2.**

Before acting:

1. Inspect the actual repository.
2. Verify the v2 contract's current state.
3. Run relevant tests when authorized.
4. Explain the next small implementation step.
5. Wait for user confirmation.

Do not skip ahead to the Contract Diff Engine before validating the v2 snapshot.

## 8. Long-Term Success Criteria

The learning project will have reached a meaningful product POC when it can demonstrate:

- Independent MCP clients consuming the same tools.
- Portability between different Fusion environments.
- Real Oracle REST API integration.
- A versioned API Contract Registry.
- Automatic contract difference detection.
- Controlled tool generation and publication.
- Security and auditable execution.
- Automated regression testing.
- Successful lightweight deployment in OCI Always Free.

The objective is progressive mastery of the concepts while building a maintainable and portable software product.