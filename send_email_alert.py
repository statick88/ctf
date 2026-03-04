#!/usr/bin/env python3
"""
Send email alert when free virtual CTF is found
Requires: pip install yagmail
"""

import subprocess
import sys


def send_email_alert(ctf_name, ctf_url):
    """Send email alert about free virtual CTF"""

    subject = f"🎯 CTF Gratuito Virtual encontrado: {ctf_name}"
    body = f"""
🚨 ALERTA: CTF Gratuito Virtual encontrado en RootedCON!

Nombre: {ctf_name}
URL de registro: {ctf_url}

Fecha de detección: 2026-03-04

¡Date prisa en registrarte!

---
Este mensaje fue enviado automáticamente por el monitor de CTFs de RootedCON
"""

    # Try using sendmail or mail command
    try:
        # Try using mail command (macOS)
        result = subprocess.run(
            ["mail", "-s", subject, "dsaavedra88@gmail.com"],
            input=body,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"✅ Email enviado a dsaavedra88@gmail.com")
            return True
    except Exception:
        pass

    # Try using Python yagmail if available
    try:
        import yagmail

        yag = yagmail.SMTP()
        yag.send(to="dsaavedra88@gmail.com", subject=subject, contents=body)
        print(f"✅ Email enviado con yagmail a dsaavedra88@gmail.com")
        return True
    except ImportError:
        print("⚠️ yagmail no está instalado. Para instalar: pip install yagmail")
    except Exception as e:
        print(f"⚠️ Error enviando email: {e}")

    return False


def main():
    # Test email sending
    print("📧 Probando envío de email de alerta...")

    result = send_email_alert(
        "CTF de prueba", "https://reg.rootedcon.com/payment/activity/367"
    )

    if not result:
        print("\n📝 Para recibir alertas por email, necesitas configurar:")
        print("   1. Instalar yagmail: pip install yagmail")
        print("   2. O configurar tu cliente de email")
        print("   3. O usar un servicio como SendGrid/Mailgun")


if __name__ == "__main__":
    main()
