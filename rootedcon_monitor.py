#!/usr/bin/env python3
"""
Monitor for Free Virtual CTF events at RootedCON
Checks every hour and creates Google Calendar event when found

Usage:
    python3 rootedcon_monitor.py

Setup cron (runs every hour):
    crontab -e
    0 * * * * /usr/bin/python3 /Users/statick/apps/ctf/rootedcon_monitor.py >> /Users/statick/apps/ctf/cron.log 2>&1
"""

import os
import sys
import json
import subprocess
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
CTF_ACTIVITIES = [
    {
        "id": 367,
        "name": "CTF BADGES 2026",
        "url": "https://reg.rootedcon.com/payment/activity/367",
    },
    {
        "id": 366,
        "name": "ROBOCOMBAT'26",
        "url": "https://reg.rootedcon.com/payment/activity/366",
    },
    {
        "id": 365,
        "name": "RootedCON Hacker Night",
        "url": "https://reg.rootedcon.com/payment/activity/365",
    },
]

LOG_FILE = "/Users/statick/apps/ctf/ctf_alerts.json"
ALREADY_NOTIFIED_FILE = "/Users/statick/apps/ctf/notified_ctfs.txt"


def log_message(message):
    """Log message to stdout and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def fetch_page(url):
    """Fetch page content"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        log_message(f"Error fetching {url}: {e}")
        return ""


def check_ctf_status(activity):
    """Check if a CTF is free and available"""
    url = activity["url"]
    content = fetch_page(url)

    if not content:
        return None

    # Check if it's free (looking for "0.00" or "-" in price)
    is_free = False
    if "0.00" in content:
        is_free = True
    elif '"-">' in content and "EUR" not in content:
        is_free = True

    # Check if it's available (not "NOT enabled" or "Closed")
    is_available = "NOT enabled" not in content and "Closed" not in content

    # Check location - if it says "Madrid" it's in-person, otherwise might be virtual
    is_madrid = "Madrid" in content

    return {
        "name": activity["name"],
        "id": activity["id"],
        "url": url,
        "is_free": is_free,
        "is_available": is_available,
        "is_madrid": is_madrid,
        "is_virtual": not is_madrid,
    }


def load_notified_ctfs():
    """Load list of already notified CTFs"""
    path = Path(ALREADY_NOTIFIED_FILE)
    if path.exists():
        with open(path, "r") as f:
            return set(line.strip() for line in f if line.strip())
    return set()


def save_notified_ctf(ctf_id):
    """Save CTF ID to notified list"""
    with open(ALREADY_NOTIFIED_FILE, "a") as f:
        f.write(f"{ctf_id}\n")


def create_calendar_alert(ctf_info):
    """Create alert data for Google Calendar event"""
    # This creates the event data - would need Google API credentials to actually create
    event_data = {
        "summary": f"🎯 {ctf_info['name']} - RootedCON CTF DISPONIBLE!",
        "description": f"""🚨 FREE CTF EVENT ENCONTRADO en RootedCON!

Actividad: {ctf_info["name"]}
Precio: FREE (0€)
Estado: {"Disponible" if ctf_info["is_available"] else "Próximamente"}
Modalidad: {"Virtual/Online" if ctf_info["is_virtual"] else "Presencial (Madrid)"}

📝 Registro: {ctf_info["url"]}

¡Date prisa en registrarte!""",
        "ctf_id": ctf_info["id"],
        "detected_at": datetime.now().isoformat(),
    }

    # Save to alerts file
    alerts = []
    if Path(LOG_FILE).exists():
        with open(LOG_FILE, "r") as f:
            alerts = json.load(f)

    alerts.append(event_data)

    with open(LOG_FILE, "w") as f:
        json.dump(alerts, f, indent=2)

    return event_data


def main():
    """Main monitoring function"""
    log_message("=" * 50)
    log_message("Iniciando verificación de CTFs gratuitos en RootedCON...")

    notified_ctfs = load_notified_ctfs()
    new_alerts = []

    for activity in CTF_ACTIVITIES:
        log_message(f"Verificando: {activity['name']}...")

        status = check_ctf_status(activity)

        if status:
            log_message(
                f"  - Free: {status['is_free']}, Disponible: {status['is_available']}, Madrid: {status['is_madrid']}"
            )

            # Check if it's a free virtual CTF
            if status["is_free"] and (status["is_virtual"] or not status["is_madrid"]):
                ctf_id = str(status["id"])

                if ctf_id not in notified_ctfs:
                    log_message(
                        f"  🎉 ¡ENCONTRADO! CTF gratuito disponible: {status['name']}"
                    )
                    alert = create_calendar_alert(status)
                    new_alerts.append(alert)
                    save_notified_ctf(ctf_id)
                else:
                    log_message(f"  ✓ Ya notificado anteriormente")
            elif status["is_free"] and status["is_madrid"]:
                log_message(f"  ℹ️ Gratuito pero presencial en Madrid")

    if new_alerts:
        log_message(f"\n🎊 ¡Se encontraron {len(new_alerts)} nuevos CTFs gratuitos!")
        for alert in new_alerts:
            log_message(f"  📅 {alert['summary']}")
            log_message(f"     {alert['description']}")
    else:
        log_message("\n😔 No se encontraron CTFs gratuitos virtuales nuevos.")
        log_message("   Los CTFs gratuitos actuales son presenciales en Madrid.")

    log_message("=" * 50)


if __name__ == "__main__":
    main()
