# ADR-001 — Contract-Driven Architecture

**Status:** Accepted  
**Project:** Fusion MCP Gateway  
**Scope:** Oracle Fusion Cloud Applications — ERP, SCM, HCM, CX

## Context

O Fusion MCP Gateway pretende disponibilizar capacidades nativas do Oracle Fusion Cloud Applications por meio do Model Context Protocol (MCP).

As APIs REST e SOAP da Oracle evoluem ao longo dos releases do Fusion. Novos recursos, operações, atributos e parâmetros podem ser introduzidos, alterados ou descontinuados.

Manter manualmente todos os contratos dentro do código das ferramentas MCP criaria forte acoplamento, dificuldades de atualização e riscos de incompatibilidade.

## Decision

O Fusion MCP Gateway adotará uma arquitetura Contract-Driven e Metadata-Driven.

A implementação deverá:

1. Descobrir e coletar contratos REST e SOAP a partir de fontes Oracle suportadas.
2. Armazenar snapshots versionados dos contratos.
3. Normalizar metadados para um modelo interno consistente.
4. Comparar contratos entre releases e identificar mudanças.
5. Distinguir contratos Oracle dos contratos públicos das ferramentas MCP.
6. Gerar ferramentas MCP candidatas a partir de metadados estruturados.
7. Validar compatibilidade, segurança e comportamento antes de publicar ferramentas.
8. Permitir configuração por instância Oracle Fusion sem modificar o código-fonte.
9. Preservar contratos públicos estáveis sempre que possível.

## Architecture Components

- **Contract Discovery Engine:** coleta e identifica contratos REST e SOAP.
- **Contract Registry:** armazena contratos, metadados, versões e estados de certificação.
- **Contract Diff Engine:** identifica mudanças e possíveis incompatibilidades.
- **Compatibility Resolver:** seleciona contratos e adaptadores compatíveis com cada ambiente Fusion.
- **MCP Tool Factory:** transforma contratos aprovados em ferramentas MCP.
- **Fusion Adapters:** executam operações REST e SOAP.
- **MCP Runtime:** disponibiliza ferramentas aos clientes MCP.

## Security Principles

- Descoberta de uma API não significa autorização para utilizá-la.
- Ferramentas de escrita exigem políticas e controles explícitos.
- Credenciais de clientes não serão armazenadas nos contratos versionados.
- O acesso respeitará as autorizações e restrições de dados aplicáveis no Oracle Fusion.
- Operações deverão produzir registros de auditoria adequados.

## Consequences

### Benefits

- Redução do esforço de manutenção manual.
- Melhor rastreabilidade das mudanças trimestrais.
- Reutilização entre clientes Oracle Fusion.
- Separação entre contratos Oracle e contratos MCP.
- Possibilidade de automatizar testes e análises de compatibilidade.

### Trade-offs

- Maior complexidade arquitetural inicial.
- Necessidade de manter um catálogo versionado.
- Nem todas as regras funcionais poderão ser inferidas automaticamente de metadados.
- Certificação e publicação continuarão exigindo validações controladas.

## Initial Implementation Strategy

O desenvolvimento começará com Oracle Fusion ERP Payables.

Inicialmente serão implementadas ferramentas somente de leitura e contratos simulados.

Posteriormente serão introduzidos descoberta REST, snapshots, comparação de contratos, geração controlada de ferramentas e integração com ambientes Fusion reais.

O suporte a SOAP será incorporado por meio de um adaptador específico.

## Decision Validation

Esta decisão será considerada tecnicamente validada quando o produto demonstrar:

- Captura de um contrato Oracle REST.
- Armazenamento de duas versões de um contrato.
- Identificação automática de diferenças.
- Geração de uma ferramenta MCP candidata.
- Execução de testes de regressão.
- Publicação controlada de uma ferramenta aprovada.