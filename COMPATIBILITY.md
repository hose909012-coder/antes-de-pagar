# Compatibilidad multiagente

Antes de Pagar usa un núcleo canónico y adaptadores pequeños. El núcleo es [`skills/antes-de-pagar/SKILL.md`](skills/antes-de-pagar/SKILL.md); los adaptadores no deben copiar ni reescribir su lógica.

No existe un formato que todos los agentes del mercado carguen automáticamente. La compatibilidad universal se consigue con dos capas:

1. **Agent Skills:** para productos que descubren `SKILL.md`.
2. **Instrucciones Markdown:** para productos que cargan un archivo de contexto o aceptan un prompt de sistema.

## Instalación por entorno

### Codex y ChatGPT Work

```bash
codex plugin marketplace add hose909012-coder/antes-de-pagar --ref main
codex plugin add antes-de-pagar@antes-de-pagar
```

### Claude Code

Clona el repositorio y abre Claude Code en su raíz. `CLAUDE.md` importa `AGENTS.md`, que dirige a la skill canónica. Para disponibilidad global, copia la carpeta `skills/antes-de-pagar` a `~/.claude/skills/antes-de-pagar`.

### Gemini CLI

Clona el repositorio y abre Gemini CLI en su raíz. `GEMINI.md` contiene la ruta y las reglas de activación. Si trabajas desde otro proyecto, importa el contenido de `GEMINI.md` en el archivo de contexto de ese proyecto y ajusta la ruta a la skill.

### GitHub Copilot

Usa este repositorio como base o copia `.github/copilot-instructions.md` y `skills/antes-de-pagar/` a tu repositorio. Las instrucciones indican a Copilot cuándo cargar el flujo.

### Cursor

Copia `.cursor/rules/antes-de-pagar.mdc` y `skills/antes-de-pagar/` al proyecto donde quieras usarla. La regla está configurada para activarse por descripción, no para todas las conversaciones.

### OpenCode y agentes compatibles con AGENTS.md

Abre el agente en la raíz del repositorio o copia `AGENTS.md` junto con `skills/antes-de-pagar/` a tu proyecto.

### Cualquier otro agente

Adjunta [`adapters/UNIVERSAL.md`](adapters/UNIVERSAL.md) como instrucción de sistema o contexto de proyecto. Si el agente puede leer archivos, conserva la ruta a la skill. Si no puede, adjunta también `SKILL.md` y los tres archivos de `references/`.

## Garantías y límites

- Todos los adaptadores apuntan al mismo núcleo, probado por `scripts/validate_repo.py`.
- La investigación web, lectura de imágenes y apertura de archivos dependen de las capacidades y permisos del agente anfitrión.
- Un agente sin búsqueda web puede analizar la evidencia, pero debe marcar como no verificadas las afirmaciones actuales.
- La skill no convierte a ningún agente en asesor financiero, autoridad policial ni servicio de recuperación de fondos.
