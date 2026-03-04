#!/usr/bin/env node
/**
 * Send email notification for CTF alerts
 * Uses nodemailer - install with: npm install nodemailer
 */

const nodemailer = require('nodemailer');

const EMAIL_CONFIG = {
  // You'll need to configure this with your email provider
  // For Gmail, use App Password: https://support.google.com/accounts/answer/185833
  host: 'smtp.gmail.com',
  port: 587,
  secure: false,
  auth: {
    user: 'dsaavedra88@gmail.com',
    pass: 'YOUR_APP_PASSWORD' // Generate from Google Account > Security > App Passwords
  }
};

const RECIPIENT = 'dsaavedra88@gmail.com';

async function sendAlert(ctfName, ctfUrl) {
  // Create transporter
  const transporter = nodemailer.createTransport(EMAIL_CONFIG);
  
  const mailOptions = {
    from: 'CTF Alert <dsaavedra88@gmail.com>',
    to: RECIPIENT,
    subject: `🎯 CTF Gratuito Virtual: ${ctfName}`,
    text: `
🚨 ALERTA: CTF Gratuito Virtual encontrado en RootedCON!

Nombre: ${ctfName}
URL: ${ctfUrl}

¡Date prisa en registrarte!

---
Enviado automáticamente por el monitor de CTFs
    `,
    html: `
<h1>🚨 ALERTA: CTF Gratuito Virtual</h1>
<p><strong>Nombre:</strong> ${ctfName}</p>
<p><strong>URL de registro:</strong> <a href="${ctfUrl}">${ctfUrl}</a></p>
<p><em>¡Date prisa en registrarte!</em></p>
<hr>
<small>Enviado automáticamente por el monitor de CTFs RootedCON</small>
    `
  };
  
  try {
    await transporter.sendMail(mailOptions);
    console.log('✅ Email enviado exitosamente');
    return true;
  } catch (error) {
    console.log('❌ Error enviando email:', error.message);
    return false;
  }
}

// Test if run directly
if (require.main === module) {
  const testName = process.argv[2] || 'CTF Test';
  const testUrl = process.argv[3] || 'https://reg.rootedcon.com';
  
  console.log('📧 Enviando email de prueba...');
  sendAlert(testName, testUrl)
    .then(() => process.exit(0))
    .catch(e => {
      console.error(e);
      process.exit(1);
    });
}

module.exports = { sendAlert };
