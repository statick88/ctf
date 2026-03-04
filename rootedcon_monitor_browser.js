#!/usr/bin/env node
/**
 * RootedCON CTF Monitor - Uses Puppeteer for automated browser checking
 * 
 * Setup:
 *   npm install puppeteer
 * 
 * Run:
 *   node rootedcon_monitor_browser.js
 */

const puppeteer = require('puppeteer');

const CTF_ACTIVITIES = [
  { id: 367, name: 'CTF BADGES 2026' },
  { id: 366, name: 'ROBOCOMBAT\'26' },
  { id: 365, name: 'RootedCON Hacker Night' },
];

const LOG_FILE = '/Users/statick/apps/ctf/ctf_alerts.json';
const NOTIFIED_FILE = '/Users/statick/apps/ctf/notified_ctfs.txt';

function log(message) {
  console.log(`[${new Date().toISOString()}] ${message}`);
}

function loadNotified() {
  try {
    const fs = require('fs');
    if (fs.existsSync(NOTIFIED_FILE)) {
      return new Set(fs.readFileSync(NOTIFIED_FILE, 'utf-8').split('\n').filter(Boolean));
    }
  } catch (e) {}
  return new Set();
}

function saveNotified(ctfId) {
  try {
    const fs = require('fs');
    fs.appendFileSync(NOTIFIED_FILE, `${ctfId}\n`);
  } catch (e) {
    log(`Error saving notification: ${e}`);
  }
}

async function checkCTFs() {
  log('Starting CTF check with browser...');
  
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const page = await browser.newPage();
    
    // Go to activities page
    await page.goto('https://reg.rootedcon.com/main/activities', { 
      waitUntil: 'networkidle2',
      timeout: 30000 
    });
    
    // Check if logged in
    const cookies = await page.cookies();
    const isLoggedIn = cookies.some(c => c.name === 'csrftoken');
    
    if (!isLoggedIn) {
      log('Not logged in - skipping check');
      return;
    }
    
    log('Logged in, checking activities...');
    
    // Get page content
    const content = await page.content();
    
    const results = [];
    
    for (const activity of CTF_ACTIVITIES) {
      // Check if activity exists and get price - use evaluate
      const activityInfo = await page.evaluate((activityId) => {
        // Find all activity links
        const links = Array.from(document.querySelectorAll('a[href*="/payment/activity/"]'));
        const activityLink = links.find(l => l.href.includes(`/payment/activity/${activityId}`));
        
        if (activityLink) {
          const parent = activityLink.parentElement;
          const text = parent ? parent.textContent : '';
          
          return {
            id: activityId,
            text: text,
            isFree: text.includes('0.00') || text.trim() === '-',
            isMadrid: text.includes('Madrid')
          };
        }
        return null;
      }, activity.id);
      
      if (activityInfo) {
        results.push({
          ...activity,
          isFree: activityInfo.isFree,
          isMadrid: activityInfo.isMadrid,
          isVirtual: !activityInfo.isMadrid
        });
        
        log(`  ${activity.name}: Free=${activityInfo.isFree}, Madrid=${activityInfo.isMadrid}`);
      }
    }
    
    // Check for new free virtual CTFs
    const notified = loadNotified();
    
    for (const result of results) {
      if (result.isFree && result.isVirtual) {
        const id = result.id.toString();
        if (!notified.has(id)) {
          log(`🎉 FOUND FREE VIRTUAL CTF: ${result.name}!`);
          
          // Create alert
          const fs = require('fs');
          let alerts = [];
          if (fs.existsSync(LOG_FILE)) {
            try { alerts = JSON.parse(fs.readFileSync(LOG_FILE, 'utf-8')); } catch(e) {}
          }
          
          alerts.push({
            name: result.name,
            id: result.id,
            foundAt: new Date().toISOString(),
            url: `https://reg.rootedcon.com/payment/activity/${result.id}`
          });
          
          fs.writeFileSync(LOG_FILE, JSON.stringify(alerts, null, 2));
          
          saveNotified(id);
          
          // Send email notification
          await sendEmailAlert(result.name, result.id);
        }
      }
    }
    
    if (results.filter(r => r.isFree && r.isVirtual).length === 0) {
      log('No free virtual CTFs found');
    }
    
  } catch (error) {
    log(`Error: ${error.message}`);
  } finally {
    await browser.close();
  }
}

async function sendEmailAlert(ctfName, ctfId) {
  // This would require SMTP setup
  log(`📧 Would send email alert for: ${ctfName}`);
  log(`   URL: https://reg.rootedcon.com/payment/activity/${ctfId}`);
}

// Run if called directly
if (require.main === module) {
  checkCTFs().then(() => {
    log('Check complete');
    process.exit(0);
  }).catch(err => {
    log(`Fatal error: ${err}`);
    process.exit(1);
  });
}

module.exports = { checkCTFs };
