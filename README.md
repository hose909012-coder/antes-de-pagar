# Antes de Pagar

**Antes de mandar dinero, manda primero la evidencia.**

Antes de Pagar es un plugin abierto para ChatGPT Work y Codex que analiza posibles estafas, phishing, suplantaciones, ofertas engañosas y solicitudes de pago. Puede trabajar con capturas, mensajes, correos, enlaces, facturas, ofertas de trabajo y ventas en línea.

No etiqueta automáticamente a personas como estafadoras y nunca promete que una operación es “100 % segura”. Separa hechos, señales e incertidumbre; después propone una verificación independiente.

## Qué hace

- Clasifica el caso como `Riesgo alto`, `Precaución`, `Pocas señales de riesgo` o `No hay datos suficientes`.
- Explica las señales concretas que influyen en la conclusión.
- Investiga afirmaciones actuales usando fuentes oficiales cuando hay acceso a búsqueda web.
- Indica qué no hacer y cómo verificar por un canal independiente.
- Da un plan de contención si el usuario ya pagó o compartió credenciales.
- Responde en el idioma del usuario.

## Ejemplos

- “Analiza esta captura antes de que pague.”
- “Me ofrecieron trabajo y quieren que deposite un cheque. ¿Es normal?”
- “Este correo dice que mi cuenta bancaria será bloqueada. Revisa el enlace.”
- “Ya mandé la transferencia, ¿qué hago ahora?”

## Instalación desde GitHub

Requiere una versión de Codex compatible con Agent Plugins.

```bash
codex plugin marketplace add hose909012-coder/antes-de-pagar --ref main
codex plugin add antes-de-pagar@antes-de-pagar
```

Después, inicia un chat nuevo e invoca `$antes-de-pagar`, o abre el directorio de Plugins en la aplicación de escritorio de ChatGPT, selecciona el catálogo **Antes de Pagar** e instala el plugin.

Para recibir actualizaciones:

```bash
codex plugin marketplace upgrade antes-de-pagar
codex plugin add antes-de-pagar@antes-de-pagar
```

## Uso seguro

- Censura números de cuenta, direcciones, documentos, contraseñas y códigos antes de subir capturas.
- Nunca compartas contraseñas, códigos de un solo uso, frases semilla ni claves privadas.
- No abras enlaces sospechosos para “comprobarlos”; comparte el texto o una captura.
- Una conclusión de pocas señales de riesgo no sustituye la verificación con el banco, plataforma o empresa por un canal oficial.

## Estructura

```text
plugin.json                              Manifiesto portátil
.codex-plugin/plugin.json                Compatibilidad con Codex
.agents/plugins/marketplace.json         Catálogo instalable desde GitHub
skills/antes-de-pagar/SKILL.md           Flujo principal
skills/antes-de-pagar/references/        Marco, formato y respuesta a incidentes
tests/cases.md                            Casos de evaluación
scripts/validate_repo.py                  Validación sin dependencias
```

## Desarrollo

```bash
python3 scripts/validate_repo.py
python3 /ruta/a/skill-creator/scripts/quick_validate.py skills/antes-de-pagar
python3 /ruta/a/plugin-creator/scripts/validate_plugin.py .
```

Las dos últimas rutas dependen de dónde estén instaladas las skills de creación. El primer comando funciona directamente en este repositorio.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para proponer cambios. Los reportes de seguridad deben seguir [SECURITY.md](SECURITY.md) y no deben incluir datos personales reales en issues públicos.

## Privacidad y limitaciones

La versión actual es un plugin de instrucciones: no incluye servidor, base de datos ni telemetría propios. El tratamiento de los mensajes y archivos depende del producto anfitrión y de las herramientas que el usuario habilite. Consulta [PRIVACY.md](PRIVACY.md) y [TERMS.md](TERMS.md).

## Licencia

[MIT](LICENSE)
