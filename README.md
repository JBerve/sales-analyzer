# Sales Analyzer

## Objetivo

Trabajar con datos estructurados (CSV) y practicar un workflow de desarrollo colaborativo usando Git:

- trabajo con branches
- pull requests
- code reviews
- resolución de merge conflicts
- colaboración sobre un mismo repositorio

El foco no está en complejidad, sino en:

- organización del código
- claridad
- uso correcto de Git
- comunicación técnica

## Reglas del proyecto

- No trabajar directamente en main
- Cada feature tiene que ir en una branch
- Todo cambio tiene que entrar vía Pull Request
- Todo PR tiene que ser revisado por el otro trainee
- Todo PR Y Review tiene que ser revisado por alguien de Pento

## Workflow esperado

Trabajar usando the pento way como guía y hacer un PR.

El otro trainee le hace code review

Alguien más del equipo hacer review al PR y a los comments del trainee

Recién ahí merge.

## Code Review

Mirar:

- claridad del código
- nombres de variables
- separación de responsabilidades
- duplicación de lógica
- manejo de errores

No solo aprobar.

Intentar hacer un merge conflict para:

- entender el conflicto
- resolverlo manualmente
- commitear fix

## Requisitos técnicos

El código tiene que:

- leer CSV
- separar parsing de analytics
- evitar mezclar lógica con CLI
- ser legible
