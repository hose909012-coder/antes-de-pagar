# Contribuir

Gracias por mejorar Antes de Pagar.

## Principios

- Añade instrucciones que cambien decisiones reales; evita listas genéricas o alarmistas.
- No conviertas una señal aislada en prueba de fraude.
- Mantén separados hechos, inferencias e incertidumbre.
- No agregues ejemplos con datos personales reales.
- Conserva la prioridad de las instrucciones explícitas del usuario, excepto cuando pidan exponer secretos, acusar sin evidencia o realizar acciones no autorizadas.

## Flujo

1. Crea una rama y realiza un cambio enfocado.
2. Añade o actualiza un caso en `tests/cases.md` cuando cambie el comportamiento.
3. Ejecuta `python3 scripts/validate_repo.py`.
4. Abre un pull request explicando el problema, el comportamiento esperado y los límites de seguridad considerados.

Los cambios a `plugin.json` y `.codex-plugin/plugin.json` deben mantener el mismo nombre y versión.
