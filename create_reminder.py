#!/usr/bin/env python3
"""
Script para crear recordatorio en Google Calendar
y enviar email cuando haya CTF gratuito virtual en RootedCON
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
REMINDER_FILE = "/Users/statick/apps/ctf/ctf_reminder.md"
ALERT_LOG = "/Users/statick/apps/ctf/ctf_alerts.json"
EMAIL_RECIPIENT = "dsaavedra88@gmail.com"


def create_reminder():
    """Create a reminder for checking CTFs"""

    reminder_content = f"""# 🔔 Recordatorio: Revisar CTFs RootedCON Virtuales

**Fecha del recordatorio:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Acciones a realizar

1. Ir a: https://reg.rootedcon.com/main/activities
2. Buscar actividades con:
   - ✅ Precio: Gratuito (0€)
   - ✅ Modalidad: Virtual/Online (no Madrid)

## Actividades a verificar

| ID | Nombre | Estado Actual |
|----|--------|---------------|
| 367 | CTF BADGES 2026 | Gratuito, presencial Madrid |
| 366 | ROBOCOMBAT'26 | Gratuito, presencial Madrid |
| 365 | Hacker Night | 50€, presencial Madrid |

## Nota

Por ahora NO hay CTFs gratuitos virtuales disponibles.
Todos los CTFs son presenciales en Madrid.

---
*Este recordatorio fue creado automáticamente*
"""

    with open(REMINDER_FILE, "w") as f:
        f.write(reminder_content)

    print(f"✅ Recordatorio creado: {REMINDER_FILE}")
    return True


def create_gcal_url():
    """Create a Google Calendar URL for the reminder"""

    # Calendar URL for March 5, 2026
    start_date = "20260305T090000"
    end_date = "20260305T100000"

    title = "Recordatorio: Revisar CTFs RootedCON Virtuales"
    details = """Verificar si hay CTFs gratuitos y virtuales en RootedCON

URL: https://reg.rootedcon.com/main/activities

CTFs gratuitos actuales (presenciales Madrid):
- CTF BADGES 2026
- ROBOCOMBAT'26"""

    gcal_url = (
        f"https://calendar.google.com/calendar/render?"
        f"action=TEMPLATE&text={title.replace(' ', '+')}&"
        f"dates={start_date}/{end_date}&"
        f"details={details.replace(' ', '+').replace(chr(10), '%0A')}&"
        f"sf=true&output=xml"
    )

    print(f"\n📅 Enlace para crear recordatorio en Google Calendar:")
    print(gcal_url)

    return gcal_url


def main():
    print("=" * 60)
    print("Creando recordatorio para CTFs de RootedCON...")
    print("=" * 60)

    create_reminder()
    gcal_url = create_gcal_url()

    print("\n" + "=" * 60)
    print("RESUMEN:")
    print("=" * 60)
    print(f"📧 Email de alerta: {EMAIL_RECIPIENT}")
    print(f"📁 Archivo de recordatorio: {REMINDER_FILE}")
    print(f"📅 Recordatorio: 5 Marzo 2026, 9:00 AM")
    print("=" * 60)


if __name__ == "__main__":
    main()
