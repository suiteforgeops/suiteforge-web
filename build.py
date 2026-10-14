#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SuiteForge static site generator.
Generates: the home page, one landing + privacy + terms per app, sitemap.xml, robots.txt, CNAME.
Single source of truth = APPS config below. No external deps.
"""
import os, html, json, hashlib, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://suiteforge.app"

# ---------------------------------------------------------------------------
# SINGLE SOURCE OF TRUTH
# ---------------------------------------------------------------------------
APPS = {
    "fastclear": {
        "name": "FastClear",
        "full_name": "Fasting Timer: FastClear",
        "category_label": "Health & Wellness",
        "schema_category": "HealthApplication",
        "appstore_id": "6762476052",
        "accent": "#1f9d57", "accent_deep": "#157a42", "accent_tint": "#e3f3ea",
        "icon_svg": '<path d="M12 3l7 3v5c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3z"/><circle cx="12" cy="12" r="3.2"/><path d="M12 10.4V12l1.1.9"/>',
        "tagline": "A calm timer for intermittent fasting.",
        "hero_sub": "Pick a fasting protocol, start your timer, and watch your streak grow. No charts you can't read, no noise — just a clear view of where you are in your fast.",
        "seo_title": "FastClear — Private intermittent fasting timer for iPhone",
        "seo_desc": "FastClear is a privacy-first intermittent fasting timer for iPhone. Track 16:8, 18:6, OMAD and custom fasts. No account, no tracking, all data on your device.",
        "home_blurb": "A clean, focused intermittent-fasting timer. Pick a protocol, start your fast, watch your streak grow.",
        "price_note": "Free download · optional subscription",
        "highlights": [
            ("16:8 → OMAD", "Every protocol, or your own window"),
            ("Widgets", "Your fast on the Home Screen"),
            ("Apple Health", "Completed fasts, only if you allow it"),
            ("0", "Accounts, ads or trackers"),
        ],
        "features": [
            ("Every protocol, one tap", "16:8, 18:6, 20:4, OMAD or a custom window. Switch any time without losing your history.", '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.2 1.8"/>'),
            ("Honest streaks", "See completed fasts build into a streak that motivates without guilt-tripping. Miss a day? Pick right back up.", '<path d="M5 13l4 4 10-11"/>'),
            ("Apple Health, your way", "Completed fasts can be written to Apple Health so your wellness data stays together — only if you allow it.", '<path d="M12 21C7 17 4 14 4 9.5 4 7 6 5 8.5 5c1.6 0 3 .9 3.5 2 .5-1.1 1.9-2 3.5-2C21 5 22 7 22 9.5c0 4.5-3 7.5-8 11.5z"/>'),
            ("Widgets that glance", "Keep your current fast on your Home Screen. One look tells you how long is left.", '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>'),
        ],
        "steps": [
            ("Choose your window", "Tap a protocol or set your own fasting and eating hours."),
            ("Start the timer", "Your fast runs in the app, in a widget, and on your lock screen."),
            ("Build the habit", "Each completed fast adds to your streak and, optionally, to Apple Health."),
        ],
        "faq": [
            ("Is FastClear free?", "Yes — FastClear is free to download and the core timer is free to use. An optional subscription unlocks advanced protocols and extended history."),
            ("What's the best app for private intermittent fasting?", "FastClear is built specifically for people who want a private fasting timer: it has no account, no analytics and no trackers, and every fast is stored on your own device rather than on a company server."),
            ("Does FastClear need an internet connection?", "No. FastClear works fully offline. A connection is only used by Apple to manage an optional subscription."),
            ("Does FastClear share my fasting data?", "No. Your fasting history never leaves your device unless you choose to write completed fasts to Apple Health, which stays under your control in the Health app."),
            ("Does FastClear support 16:8 and OMAD?", "Yes. FastClear supports 16:8, 18:6, 20:4, OMAD and fully custom fasting windows."),
        ],
        "mock": """
          <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;padding:30px 18px;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-faint);font-weight:600;">16 : 8 · Fasting</div>
            <div style="width:150px;height:150px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--accent) 232deg,#e8e2d6 0);">
              <div style="width:120px;height:120px;border-radius:50%;background:var(--bg-card);display:grid;place-items:center;">
                <div style="text-align:center;"><div style="font-family:var(--serif);font-weight:900;font-size:1.9rem;color:var(--ink);line-height:1;">10:18</div><div style="font-size:.62rem;color:var(--ink-faint);margin-top:3px;">elapsed</div></div>
              </div>
            </div>
            <div style="font-size:.74rem;color:var(--accent-deep);font-weight:600;">5h 42m to goal</div>
            <div style="display:flex;gap:6px;margin-top:4px;">
              <span style="width:9px;height:9px;border-radius:50%;background:var(--accent);"></span><span style="width:9px;height:9px;border-radius:50%;background:var(--accent);"></span><span style="width:9px;height:9px;border-radius:50%;background:var(--accent);"></span><span style="width:9px;height:9px;border-radius:50%;background:#e0dacd;"></span><span style="width:9px;height:9px;border-radius:50%;background:#e0dacd;"></span>
            </div>
          </div>""",
        "permissions": [
            ("Apple Health (write only)", "If you allow it, FastClear writes your completed fasting periods to Apple Health. FastClear never reads other health data. This is optional and can be turned off in iOS Settings at any time."),
            ("Notifications", "Used only to remind you when a fasting or eating window starts or ends. Optional."),
        ],
        "hero_shot_alt": "FastClear home screen with a live 16:8 fast at 13 hours 30 minutes, currently in the Ketosis phase",
        "shots_type": "brut",
        "shots_w": 620, "shots_h": 1347,
        "shots": [
            ("shot-1.webp", "FastClear protocol picker with 16:8, 18:6, 20:4, OMAD, 5:2 and a custom option"),
            ("shot-2.webp", "FastClear history view listing recently completed fasts"),
            ("shot-3.webp", "FastClear stats screen with longer-term fasting trends"),
            ("shot-4.webp", "FastClear settings screen with notification and protocol options"),
        ],
    },
    "routineflow": {
        "name": "RoutineFlow",
        "full_name": "Morning Routine: RoutineFlow",
        "category_label": "Health & Wellness",
        "schema_category": "HealthApplication",
        "appstore_id": "6766101143",
        "accent": "#e8821e", "accent_deep": "#c26a14", "accent_tint": "#fbedd9",
        "icon_svg": '<path d="M12 4a8 8 0 1 1-7.5 5.2"/><path d="M4 4v4h4"/><path d="M12 8v4l2.6 1.6"/>',
        "tagline": "A morning routine that actually sticks.",
        "hero_sub": "Design a calm sequence of small steps and move through them one at a time. No streak shaming, no overwhelm — just a gentle flow to start the day on your terms.",
        "seo_title": "RoutineFlow — Calm morning routine builder for iPhone",
        "seo_desc": "RoutineFlow helps you build and keep a morning routine on iPhone. Step-by-step flows, gentle reminders, no account and no tracking. All data stays on your device.",
        "home_blurb": "Build a morning routine that actually sticks. One step at a time, calmly, every day.",
        "price_note": "Free download · optional subscription",
        "highlights": [
            ("1 step", "On screen at a time, never a wall of tasks"),
            ("Reminders", "A quiet nudge at the time you pick"),
            ("No guilt", "Miss a morning, simply begin again"),
            ("0", "Accounts, ads or trackers"),
        ],
        "features": [
            ("Build your sequence", "Add the steps that matter to you — water, stretch, journal, meditate — in the order that feels right.", '<path d="M4 6h16M4 12h16M4 18h10"/>'),
            ("One step at a time", "RoutineFlow shows you a single step, not an intimidating list. Finish it, flow to the next.", '<path d="M5 12h14M13 6l6 6-6 6"/>'),
            ("Gentle reminders", "A quiet nudge at the time you choose. No badges screaming at you from the Home Screen.", '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>'),
            ("Progress without pressure", "See the mornings you showed up. Miss one and nothing breaks — you simply begin again.", '<circle cx="12" cy="12" r="8.5"/><path d="M9 12l2 2 4-4"/>'),
        ],
        "steps": [
            ("Design your morning", "Add and reorder the steps you want to do each day."),
            ("Flow through it", "Each morning, move through your routine one calm step at a time."),
            ("Keep showing up", "Watch consistency build gently, with no guilt when life happens."),
        ],
        "faq": [
            ("Is RoutineFlow free?", "Yes — RoutineFlow is free to download with a free core routine. An optional subscription unlocks multiple routines and advanced options."),
            ("What's a good private morning routine app?", "RoutineFlow is designed for a calm, private start to the day: no account, no analytics, no trackers, and your routines stay on your own device."),
            ("Can I have more than one routine?", "You can build a morning routine for free; additional routines (evening, weekend, focus) are part of the optional subscription."),
            ("Does RoutineFlow track me?", "No. There are no analytics or advertising trackers. Your routine data never leaves your device unless you use private iCloud sync."),
        ],
        "mock": """
          <div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:26px 20px;">
            <div style="font-family:var(--serif);font-weight:600;font-size:1.15rem;color:var(--ink);">Good morning</div>
            <div style="font-size:.7rem;color:var(--ink-faint);margin-bottom:6px;">3 of 5 done</div>
            <div style="display:flex;align-items:center;gap:10px;padding:11px 13px;border-radius:12px;background:var(--accent-tint);"><span style="width:20px;height:20px;border-radius:50%;background:var(--accent);display:grid;place-items:center;color:#fff;font-size:.7rem;">✓</span><span style="font-size:.82rem;color:var(--accent-deep);font-weight:600;">Drink water</span></div>
            <div style="display:flex;align-items:center;gap:10px;padding:11px 13px;border-radius:12px;background:var(--accent-tint);"><span style="width:20px;height:20px;border-radius:50%;background:var(--accent);display:grid;place-items:center;color:#fff;font-size:.7rem;">✓</span><span style="font-size:.82rem;color:var(--accent-deep);font-weight:600;">Stretch</span></div>
            <div style="display:flex;align-items:center;gap:10px;padding:13px;border-radius:12px;background:var(--bg-deep);border:1.5px solid var(--accent);"><span style="width:20px;height:20px;border-radius:50%;border:2px solid var(--accent);"></span><span style="font-size:.84rem;color:var(--ink);font-weight:600;">Journal · now</span></div>
            <div style="display:flex;align-items:center;gap:10px;padding:11px 13px;border-radius:12px;opacity:.5;"><span style="width:20px;height:20px;border-radius:50%;border:2px solid var(--ink-faint);"></span><span style="font-size:.82rem;color:var(--ink-soft);">Meditate</span></div>
          </div>""",
        "permissions": [
            ("Notifications", "Used only to remind you to start your routine at the time you set. Optional and configurable in iOS Settings."),
        ],
        "hero_shot_alt": "RoutineFlow home screen listing a Morning Energizer, Evening Wind Down and Workday Reset routine",
        "shots_type": "brut",
        "shots_w": 620, "shots_h": 1347,
        "shots": [
            ("shot-1.webp", "RoutineFlow guiding through a routine one calm step at a time"),
            ("shot-2.webp", "RoutineFlow routine editor for adding, reordering and timing each step"),
            ("shot-3.webp", "RoutineFlow settings screen with reminder time and notification options"),
            ("shot-4.webp", "RoutineFlow history showing recently completed routines"),
        ],
    },
    "walkquest": {
        "name": "WalkQuest",
        "full_name": "Step Tracker: WalkQuest",
        "category_label": "Health & Wellness",
        "schema_category": "HealthApplication",
        "appstore_id": "6768080009",
        "accent": "#b7892f", "accent_deep": "#94701f", "accent_tint": "#f4ebd6",
        "icon_svg": '<path d="M12 3l7 3v5c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3z"/><path d="M9.5 11.5l1.8 1.8 3.2-3.6"/>',
        "tagline": "Turn your daily steps into a quiet quest.",
        "hero_sub": "Set a step goal that fits your life and watch your progress fill in, day after day. No leaderboards, no social pressure — just you, moving a little more.",
        "seo_title": "WalkQuest — Private step tracker for iPhone",
        "seo_desc": "WalkQuest is a privacy-first step tracker for iPhone: daily walking goals and honest progress from your Apple Health steps. No account, no tracking.",
        "home_blurb": "Turn your daily steps into a quiet quest. Simple goals, honest progress, no noise.",
        "price_note": "Free download · optional subscription",
        "highlights": [
            ("Apple Health", "Steps your iPhone already counts"),
            ("No Watch", "Needed: your iPhone is enough"),
            ("Milestones", "Challenges and achievements"),
            ("0", "Leaderboards, ads or trackers"),
        ],
        "features": [
            ("Goals that fit you", "Start where you are. Set a realistic daily step goal and adjust it as you build momentum.", '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.2"/>'),
            ("Honest progress", "A clean ring shows today at a glance and history shows the trend — no vanity metrics.", '<path d="M21 12a9 9 0 1 1-9-9" /><path d="M21 4v5h-5"/>'),
            ("Reads from Apple Health", "WalkQuest uses the step data already on your iPhone. Nothing new to wear, nothing extra to set up.", '<path d="M12 21C7 17 4 14 4 9.5 4 7 6 5 8.5 5c1.6 0 3 .9 3.5 2 .5-1.1 1.9-2 3.5-2C21 5 22 7 22 9.5c0 4.5-3 7.5-8 11.5z"/>'),
            ("Quietly motivating", "Gentle milestones celebrate consistency, not competition. Your walk is nobody else's business.", '<path d="M8 21h8M12 17v4M7 4h10v4a5 5 0 0 1-10 0V4z"/><path d="M5 5H3v2a3 3 0 0 0 3 3M19 5h2v2a3 3 0 0 1-3 3"/>'),
        ],
        "steps": [
            ("Set your goal", "Choose a daily step target that feels achievable today."),
            ("Walk your day", "WalkQuest reads your steps from Apple Health and fills your ring."),
            ("Watch it add up", "Small consistent days become a streak you can be proud of."),
        ],
        "faq": [
            ("Is WalkQuest free?", "Yes — WalkQuest is free to download with free daily step tracking. An optional subscription unlocks long-term trends and extra goals."),
            ("What's a good private step tracker for iPhone?", "WalkQuest is a privacy-first step tracker: it reads steps from Apple Health on your device, has no account, no analytics and no trackers, and keeps your data local."),
            ("Do I need an Apple Watch?", "No. WalkQuest uses the step data your iPhone already records through Apple Health. An Apple Watch simply adds more accurate counts."),
            ("Does WalkQuest sell my activity data?", "No. WalkQuest never sells or shares your activity data. Your steps stay on your device."),
        ],
        "mock": """
          <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:30px 18px;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-faint);font-weight:600;">Today</div>
            <div style="width:150px;height:150px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--accent) 270deg,#e8e2d6 0);">
              <div style="width:120px;height:120px;border-radius:50%;background:var(--bg-card);display:grid;place-items:center;">
                <div style="text-align:center;"><div style="font-family:var(--serif);font-weight:900;font-size:1.7rem;color:var(--ink);line-height:1;">7,540</div><div style="font-size:.62rem;color:var(--ink-faint);margin-top:3px;">of 10,000 steps</div></div>
              </div>
            </div>
            <div style="font-size:.74rem;color:var(--accent-deep);font-weight:600;">75% · keep going</div>
            <div style="display:flex;gap:5px;margin-top:2px;align-items:flex-end;">
              <span style="width:7px;height:14px;border-radius:3px;background:var(--accent);"></span><span style="width:7px;height:22px;border-radius:3px;background:var(--accent);"></span><span style="width:7px;height:11px;border-radius:3px;background:#e0dacd;"></span><span style="width:7px;height:26px;border-radius:3px;background:var(--accent);"></span><span style="width:7px;height:18px;border-radius:3px;background:var(--accent);"></span><span style="width:7px;height:24px;border-radius:3px;background:var(--accent);"></span>
            </div>
          </div>""",
        "permissions": [
            ("Apple Health (read steps)", "With your permission, WalkQuest reads your step count from Apple Health to show your daily progress. It never writes to or reads anything else from Health, and you can revoke access in iOS Settings at any time."),
            ("Notifications", "Used only for the goal reminders and milestones you opt into. Optional."),
        ],
        "hero_shot_alt": "WalkQuest Today screen showing 8,500 of 10,000 steps and a 12-day streak",
        "shots_type": "brut",
        "shots_w": 620, "shots_h": 1347,
        "shots": [
            ("shot-1.webp", "WalkQuest Challenges screen with optional step-goal challenges"),
            ("shot-2.webp", "WalkQuest Achievements screen with milestone badges"),
            ("shot-3.webp", "WalkQuest History screen showing daily step totals over recent days"),
            ("shot-4.webp", "WalkQuest Settings screen with goal and notification options"),
        ],
    },
    "keepcontact": {
        "name": "KeepContact",
        "full_name": "KeepContact - Personal CRM",
        "category_label": "Productivity",
        "schema_category": "ProductivityApplication",
        "appstore_id": "6761559776",
        # 1.6.0 "Lien" identity: violet #6B3FD4 (icon background), coral #FF7A59 second accent
        "accent": "#6b3fd4", "accent_deep": "#5530b0", "accent_tint": "#ece5fa",
        "icon_svg": '<path d="M4 5h11a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H9l-4 3v-3H4z"/><path d="M17 9h3v8h-1v3l-4-3h-4"/>',
        "tagline": "Stay close to the people who matter.",
        "hero_sub": "A friend you meant to call. A former colleague you never followed up with. KeepContact turns \"I should reach out\" into a simple daily habit — and helps you know what to say when you do. No cloud, no account, no server.",
        "seo_title": "KeepContact — Private personal CRM with on-device AI",
        "seo_desc": "Privacy-first personal CRM for iPhone: who to reach out to each morning, what matters to each person, message ideas from on-device AI. No account, 100% offline.",
        "updated": "11 October 2026",
        "icloud": False,
        "lifetime": True,
        "home_blurb": "A private personal CRM. Each morning, who to reach out to and what to say — written by your iPhone's on-device AI.",
        "price_note": "Free for up to 15 contacts · Pro with a 7-day trial",
        "highlights": [
            ("On-device AI", "Summaries and message ideas, on your iPhone"),
            ("Score /100", "Your relationship health at a glance"),
            ("15 free", "Contacts tracked, no time limit"),
            ("100% offline", "No server, no account, no sync"),
        ],
        "privacy_extra": [
            ("On-device AI", "On iPhones that support Apple Intelligence, {name} uses Apple's on-device language model to summarise a contact, suggest message ideas and spot facts in your notes. Voice notes are transcribed on your device too. This processing happens entirely on your iPhone: your notes and recordings are not sent to SuiteForge, to Apple or to any third party."),
        ],
        "features": [
            ("One clear next step, every morning", "See who is overdue, at the rhythm you chose for each person. KeepContact puts one person first, with a three-line summary and a way to open the conversation — and message ideas if you're stuck on the first words.", '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
            ("Remember what matters to them", "Hobbies, gift ideas, allergies, their kids' names, the topic you promised to follow up on. Plus birthdays, anniversaries, the day you met, and who introduced you.", '<path d="M4 4h12l4 4v12H4z"/><path d="M16 4v4h4M8 13h8M8 17h6"/>'),
            ("Keep the thread", "Log calls, coffees, messages and meetings in one journal. Dictate a voice memo, transcribed on your iPhone. Scan a business card and the contact fills itself in. KeepContact even spots who you saw in your calendar and offers to log it.", '<path d="M12 3a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3z"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
            ("Your network at a glance", "A relationship health score out of 100, circles from closest to most distant, and statistics on who you actually stay in touch with.", '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6"/>'),
            ("Your year in relationships", "In December, KeepContact puts together your year in relationships, in story format, ready to share — no names shown by default. With Pro, add a greetings card to send with your wishes.", '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M10 15h4M12 7v5"/>'),
            ("No guilt, no clutter", "Snooze anyone for a week, a month, or indefinitely. Updates from your Contacts are suggested field by field, and duplicates are found and merged in one tap.", '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>'),
        ],
        "steps": [
            ("Pick the people who matter", "Work, friends, family: choose who counts and how often you'd like to be in touch. Import from Contacts or add people by hand."),
            ("Reach out, with something to say", "Each morning, KeepContact shows who's due, what you know about them, and an idea to open the conversation."),
            ("Log it in a tap", "After the call or the coffee, log it in one tap or dictate a voice note. Next time, you pick up right where you left off."),
        ],
        "faq": [
            ("Is KeepContact free?", "Yes. KeepContact is free to download, and you can track up to 15 contacts and 3 reminders for free. KeepContact Pro removes the limits and unlocks the on-device AI, voice notes, the morning brief, the health score, circles, statistics, messages to several people and encrypted backups. Your year in review, every December, is free. Subscriptions come with a 7-day free trial, or you can get Pro for life with a single payment."),
            ("What's a good private personal CRM app?", "KeepContact is a privacy-first personal CRM for iPhone: no account, no server, no analytics and no trackers. Every name, note and reminder is stored on your device, and its App Store privacy label is \"Data Not Collected\"."),
            ("Does KeepContact upload my contacts?", "No. KeepContact never uploads your contacts or notes. It works 100% offline and everything stays on your iPhone. Backups are files you save yourself, and can be encrypted with a password only you know."),
            ("How does the AI work without sending my data?", "KeepContact uses Apple's on-device AI model. Summaries, message ideas and the facts it picks up from your notes are generated on your iPhone; your notes never leave it. It requires an iPhone that supports Apple Intelligence; the rest of the app works on any iPhone running a supported iOS version."),
            ("Does KeepContact sync with iCloud?", "Not at the moment. KeepContact keeps everything on your iPhone. To move your data to another iPhone, KeepContact Pro includes a backup in Settings, which you can encrypt with your own password."),
        ],
        "mock": """
          <div style="flex:1;display:flex;flex-direction:column;gap:11px;padding:24px 18px;">
            <div style="font-family:var(--serif);font-weight:600;font-size:1.1rem;color:var(--ink);">Today</div>
            <div style="font-size:.68rem;color:var(--ink-faint);margin-bottom:4px;">3 people to reach out to</div>
            <div style="padding:12px;border-radius:14px;background:var(--accent);color:#fff;font-size:.7rem;line-height:1.35;"><strong style="font-size:.82rem;">Write to Kate</strong><br>New studio opens in March. Ask how the Lyon trade show went.</div>
            <div style="display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:12px;background:var(--accent-tint);"><span style="width:30px;height:30px;border-radius:50%;background:#ffd9c9;display:grid;place-items:center;color:#a8452b;font-weight:700;font-size:.72rem;">DT</span><div><div style="font-size:.82rem;color:var(--ink);font-weight:600;line-height:1.1;">David Taylor</div><div style="font-size:.64rem;color:var(--accent-deep);">25 days overdue</div></div></div>
          </div>""",
        "permissions": [
            ("Contacts (optional)", "If you choose to import people from your address book, KeepContact reads your contacts on your device to import them and to suggest updates. It never uploads them anywhere and never writes to your address book. You can use KeepContact without granting this permission by adding people manually."),
            ("Calendar (optional)", "If you turn on calendar suggestions, KeepContact reads your past events on your device to suggest logging the time you spent with your contacts. Nothing is saved without your OK, and nothing leaves your iPhone."),
            ("Camera (optional)", "Only used when you scan a business card, to read it and prefill a contact. The image is neither saved nor sent."),
            ("Microphone (optional)", "Only used if you choose to record a voice note on an interaction. The microphone is accessed only while you are recording. Voice notes and their transcripts are created and stored on your device."),
            ("Notifications (optional)", "Used only for the stay-in-touch reminders, birthday notifications and the morning brief you choose to receive. They are scheduled locally on your iPhone."),
        ],
        "hero_shot_alt": "KeepContact Today screen: the one person to write to today with an on-device AI summary, then the others who are due",
        "shots_type": "brut",
        "shots_w": 620, "shots_h": 1347,
        "shots": [
            ("shot-1.webp", "KeepContact Prepare card on a contact: an on-device AI summary, Write and Call buttons, and message ideas"),
            ("shot-2.webp", "KeepContact What I know section: hobbies, gift ideas, allergies, loved ones and topics to bring up"),
            ("shot-3.webp", "KeepContact My Network view: your people arranged in circles from closest to most distant"),
            ("shot-4.webp", "KeepContact Statistics: a network health score out of 100 and your interactions over four weeks"),
            ("shot-5.webp", "KeepContact Year in review: your year in relationships as a story image, with names hidden by default"),
        ],
    },
    "jezko": {
        "name": "Ježko",
        "full_name": "Ježko: Learn Serbian",
        "category_label": "Education",
        "schema_category": "EducationalApplication",
        # In App Review (October 2026). Once live: put the App Store ID here and remove "status".
        "appstore_id": None,
        "status": "soon",
        # Palette « l'été chez baka » : crvena (icon background)
        "accent": "#d9483b", "accent_deep": "#b8372c", "accent_tint": "#fbe6e1",
        "icon_svg": '<path d="M4 15c0-4 3.5-7 8-7s8 3 8 7H4z"/><circle cx="16" cy="12" r=".8"/>',
        "tagline": "Serbian for your family, 10 minutes a day.",
        "hero_sub": "Your child understands baka and deka but doesn't dare answer? Ježko turns Serbian into a daily ritual: one story, one hedgehog, ten minutes. Children follow Milena's summer in Serbia, speak from the very first lesson and learn to read both alphabets.",
        "seo_title": "Ježko: Learn Serbian for kids & families — iPhone app",
        "seo_desc": "Ježko teaches Serbian to kids and families through one story in 100 lessons. Speak out loud, read Latin and Cyrillic, 10 minutes a day. No account, no ads.",
        "home_blurb": "Serbian for kids and families, 10 minutes a day. Follow Milena's summer at her grandparents' in Serbia over 100 lessons, speak from day one, and learn to read both alphabets.",
        "home_pills": ["100 lessons · A1 → B1", "Latin & Cyrillic", "Up to 5 profiles", "No ads"],
        "price_note": "First 7 lessons free · English & French",
        "updated": "14 October 2026",
        "icloud": False,
        "lifetime": True,
        "family_sharing": True,
        "kids": True,
        "languages": ["en", "fr"],
        "highlights": [
            ("100 lessons", "One story, from A1 to B1"),
            ("10 min", "A day: one short, complete session"),
            ("2 alphabets", "Latin first, then Cyrillic"),
            ("5 profiles", "Children aged 6–14 and adults"),
        ],
        "features": [
            ("A real story, 100 lessons", "Milena is 10, half French, half Serbian. This summer she visits her grandparents in Serbia with Ježko, a garden hedgehog who woke up in her backpack. From A1 to B1, children learn the words they actually need: the market, the slava, the village.", '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M9 8h7M9 12h5"/>'),
            ("Speak from day one", "Listen, repeat each line, record yourself and compare with the model, without judgement. In Challenge mode, stars for every word recognised, right on the iPhone. And a voice journal to send to baka.", '<path d="M12 3a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3z"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
            ("Play Milena", "Act out the story: the family gives you your cues, you answer with Milena's lines. From lesson 50, “Sad ti!” (your turn) asks you to say earlier sentences in Serbian, from memory.", '<path d="M4 5h11a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H9l-4 3v-3H4z"/><path d="M17 9h3v8h-1v3l-4-3h-4"/>'),
            ("Read both alphabets", "Latin first, then Cyrillic, one group of letters at a time. Lessons switch to Cyrillic as your child learns the letters, so reading grows with the story.", '<path d="M4 19l5-14 5 14M6 14h6"/><path d="M15 5h5M17.5 5v14M15 19h5"/>'),
            ("Grammar without memorising rules", "Words come first. Then 25 short “Behind the scenes” cards explain why we say “volim čokoladu”, each with a mini quiz, and games put the words to work: pairs, missing word, sentences in order.", '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>'),
            ("Made for the whole family", "Up to 5 profiles on one iPhone, for children aged 6 to 14 and for adults. Spaced repetition brings every word back at the right time, and a parent area shows progress, sentences said out loud and the week's activity.", '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9.5" r="2.3"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0M14.5 20a4 4 0 0 1 6.5-3.1"/>'),
        ],
        "steps": [
            ("Create the family's profiles", "Up to five learners, children and adults, each with their own path and pace."),
            ("Ten minutes a day", "A warm-up with the words that are due, a new scene of the story, your lines out loud, then a game."),
            ("Hear the progress", "Words come back at the right time. The parent area shows what was learned and said out loud this week."),
        ],
        "faq": [
            ("Is Ježko free?", "The first 7 lessons are free, with the Latin alphabet and the first group of Cyrillic letters, for one profile. Ježko Family unlocks all 100 lessons and up to 5 profiles: a monthly or yearly subscription with a 7-day free trial, or a one-time lifetime purchase. All three can be shared through Family Sharing."),
            ("What's a good app to teach my child Serbian?", "Ježko is an iPhone app made for children aged 6 to 14 and their parents, especially families of the Serbian diaspora. Instead of isolated words, it tells one story over 100 lessons (A1 to B1), gets children speaking out loud from the first lesson and teaches both the Latin and Cyrillic alphabets. It has no ads, no account and no tracking."),
            ("Does Ježko teach the Cyrillic alphabet?", "Yes. Ježko starts with the Latin alphabet, then introduces Cyrillic one group of letters at a time. Lessons gradually switch to Cyrillic as the letters are learned, and you can choose Latin, mixed or Cyrillic display."),
            ("Can adults learn Serbian with Ježko too?", "Yes. Ježko is designed for children, but each family member can have their own profile, adults included, and progress at their own pace. Parents learning alongside their children is exactly the idea."),
            ("Is Ježko safe for children?", "Ježko has no ads, no account, no chat and no tracking. Profile names, recordings and progress stay on your device. On a child profile, purchases, external links and sharing are behind a parental gate."),
            ("Does Ježko work offline?", "Yes. The lessons and their audio are built into the app, so Ježko works without a connection. A connection is only used to buy or restore Ježko Family."),
            ("Which languages does Ježko support?", "Ježko teaches Serbian, with the app and every translation available in English and in French."),
        ],
        "permissions": [
            ("Microphone (optional)", "Used only when the learner taps the microphone button, to record a line and compare it with the model, or to say a sentence in Challenge mode. Recordings are stored on your device and are never uploaded. You can refuse and keep using the app: any spoken step can be skipped."),
            ("Speech recognition (optional)", "In Challenge mode, Ježko recognises the words you say to award stars. Recognition uses Apple's on-device speech framework: your voice is not sent to SuiteForge."),
            ("Notifications (optional)", "A daily reminder for the lesson, if you turn it on. It is scheduled locally on your iPhone."),
        ],
        "privacy_extra": [
            ("Profiles and recordings", "Profile names, progress, review cards and voice recordings are stored only on your device. They are never sent to SuiteForge. A recording leaves your device only if you choose to share it yourself, through the iOS share sheet (on a child profile, behind a parental gate)."),
        ],
        "hero_shot_alt": "Ježko Today screen: a Zdravo! greeting from the hedgehog, lesson 24 ready to start and a 12-day streak",
        "shots_type": "brut",
        "shots_w": 620, "shots_h": 1348,
        "shots": [
            ("shot-1.webp", "Ježko lesson 23, Hajde napolje!: the illustrated dialogue between Vuk and Tomi, in Serbian with translations"),
            ("shot-2.webp", "Ježko Repeat screen: say the line like Milena, then compare your voice with the model"),
            ("shot-3.webp", "Ježko Play Milena: your turn to say Milena's line out loud"),
            ("shot-4.webp", "Ježko alphabet screen: Cyrillic letters learned group by group"),
            ("shot-5.webp", "Ježko journey map: completed lessons and the next stop, lesson 24"),
            ("shot-6.webp", "Ježko Pairs game: match each Serbian word with its meaning"),
            ("shot-7.webp", "Ježko Behind the scenes card explaining masculine, feminine and neuter nouns"),
            ("shot-8.webp", "Ježko profiles screen: Who's learning today? with four family profiles"),
        ],
    },
}

# Page order of the apps (footer, sitemap, "more apps") and the home page bento.
ORDER = ["jezko", "keepcontact", "fastclear", "routineflow", "walkquest"]
HOME_LAYOUT = [("jezko", "feature"), ("keepcontact", "half"), ("fastclear", "half"), ("routineflow", "half"), ("walkquest", "half")]
HOME_FAN = ["keepcontact", "jezko", "fastclear"]   # the three screens in the home hero

TODAY = datetime.date.today().isoformat()
CONTACT = "suiteforgeops@gmail.com"
ORG_ID = f"{DOMAIN}/#organization"

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(s, quote=True)

def jsonstr(s):
    return json.dumps(s, ensure_ascii=False)

def released(slug):
    return bool(APPS[slug].get("appstore_id")) and APPS[slug].get("status") != "soon"

def appstore_url(slug):
    return f"https://apps.apple.com/app/id{APPS[slug]['appstore_id']}"

def theme(a):
    return f"--accent:{a['accent']};--accent-deep:{a['accent_deep']};--accent-tint:{a['accent_tint']};"

def ver(path):
    """Cache-busting URL for a local file: /path?v=<content hash>, so browsers
    pick up a new screenshot or icon right after a deploy."""
    with open(os.path.join(ROOT, path.lstrip("/")), "rb") as f:
        return f"{path}?v={hashlib.md5(f.read()).hexdigest()[:8]}"

def has(path):
    return os.path.isfile(os.path.join(ROOT, path.lstrip("/")))

def og_image(slug=None):
    """Per-app share image (<slug>/og.png, made by make_og.py) if present."""
    if slug and has(f"/{slug}/og.png"):
        return DOMAIN + ver(f"/{slug}/og.png")
    return DOMAIN + ver("/assets/og-suiteforge.png")

ICON = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "left": '<path d="M15 18l-6-6 6-6"/>',
    "right": '<path d="M9 18l6-6-6-6"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3z"/>',
    "noeye": '<path d="M3 3l18 18"/><path d="M10.6 5.1A9 9 0 0 1 21 12c-.5 1-1.1 1.9-1.9 2.6M6.6 6.6A9 9 0 0 0 3 12a9 9 0 0 0 12.5 4.3"/>',
    "check": '<path d="M5 13l4 4L19 7"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/><path d="M3 3l18 18"/>',
    "device": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
}

def svg(name, sw="2"):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON.get(name, name)}</svg>'

MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="sfg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#5d8270"/><stop offset="1" stop-color="#3c5648"/></linearGradient></defs>'
        '<rect width="32" height="32" rx="9" fill="url(#sfg)"/>'
        '<path d="M21 11.6c-.5-1.9-2.3-3.1-4.6-3.1h-1.1a3.9 3.9 0 0 0 0 7.8h1.4a3.9 3.9 0 0 1 0 7.8h-1.1c-2.3 0-4.1-1.2-4.6-3.1" '
        'fill="none" stroke="#fbf9f4" stroke-width="2.8" stroke-linecap="round"/></svg>')

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.5 1.6c.1 1-.3 2-1 2.8-.7.8-1.8 1.4-2.8 1.3-.1-1 .4-2 1-2.7.7-.8 1.9-1.4 2.8-1.4zM19 17c-.4 1-.6 1.4-1.1 2.3-.8 1.3-1.9 2.9-3.3 2.9-1.2 0-1.5-.8-3.2-.8s-2 .8-3.2.8c-1.4 0-2.4-1.4-3.2-2.7-2.2-3.5-2.5-7.6-1.1-9.8 1-1.6 2.6-2.5 4.1-2.5 1.5 0 2.4.8 3.6.8 1.1 0 1.8-.8 3.5-.8 1.3 0 2.7.7 3.7 2-3.2 1.8-2.7 6.4.5 7.8z"/></svg>'

# ---------------------------------------------------------------------------
# SHARED PARTIALS
# ---------------------------------------------------------------------------
def appstore_badge(slug):
    a = APPS[slug]
    if not released(slug):
        return f'''<span class="appstore appstore--soon" role="note">{APPLE}<span><small>Coming soon</small><strong>App Store</strong></span></span>'''
    return f'''<a class="appstore" href="{appstore_url(slug)}" aria-label="Download {esc(a['name'])} on the App Store">{APPLE}<span><small>Download on the</small><strong>App Store</strong></span></a>'''

def icon_img(slug, size, cls="", lazy=True):
    a = APPS[slug]
    return (f'<img class="{cls}" src="{ver(f"/{slug}/icon.webp")}" alt="{esc(a["name"])} app icon" width="{size}" height="{size}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async">')

def icon_block(slug, size=56, lazy=True):
    """The real App Store icon (<slug>/icon.webp) if present, else the SVG placeholder."""
    a = APPS[slug]
    r = int(size * 0.27)
    if has(f"/{slug}/icon.webp"):
        return (f'<div class="app-icon app-icon--real" style="width:{size}px;height:{size}px;border-radius:{r}px;">'
                f'{icon_img(slug, size, lazy=lazy)}</div>')
    return (f'<div class="app-icon" style="width:{size}px;height:{size}px;border-radius:{r}px;">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{a["icon_svg"]}</svg></div>')

def phone(slug, alt=None, cls="", eager=False):
    """Phone frame around the app's hero screenshot."""
    a = APPS[slug]
    alt = alt if alt is not None else (a.get("hero_shot_alt") or f"{a['name']} home screen")
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="phone phone--shot {cls}"><div class="phone-screen">'
            f'<img src="{ver(f"/{slug}/screenshots/hero-home.webp")}" alt="{esc(alt)}" width="680" height="1478" {load} decoding="async">'
            f'</div></div>')

def head(title, desc, canonical, *, body_style="", jsonld=(), extra_head="", og=None, og_alt="", favicon=None, robots="index, follow, max-image-preview:large"):
    og = og or og_image()
    blocks = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False, separators=(",", ":"))}</script>' for j in jsonld)
    fav = favicon or '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#f7f3ec" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#13110e" media="(prefers-color-scheme: dark)">
<meta name="author" content="SuiteForge">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SuiteForge">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(og_alt or title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
{fav}
<link rel="apple-touch-icon" href="{ver('/assets/apple-touch-icon.png')}">
<link rel="preload" href="/assets/fonts/fraunces-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/hanken-grotesk-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ver('/assets/styles.css')}">
<script>document.documentElement.classList.add("js")</script>
{extra_head}
{blocks}
</head>
<body{f' style="{body_style}"' if body_style else ''}>
<a class="skip" href="#main">Skip to content</a>'''

def site_header(slug=None):
    cta = ""
    if slug:
        a = APPS[slug]
        if released(slug):
            cta = f'<a class="btn btn-primary btn-sm" href="{appstore_url(slug)}">Get {esc(a["name"])}</a>'
        else:
            cta = f'<a class="btn btn-ghost btn-sm" href="#get">Coming soon</a>'
    home = "" if slug else ' aria-current="page"'
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/"{home}>{MARK} SuiteForge</a>
    <nav class="nav" aria-label="Main">
      <a href="/#apps">Apps</a>
      <a href="/#privacy" class="hide-sm">Privacy</a>
      <a href="/#faq" class="hide-sm">FAQ</a>
      {cta}
    </nav>
  </div>
</header>'''

def site_footer(slug=None):
    apps = "".join(
        f'<li><a href="/{s}/">{icon_img(s, 20)}{esc(APPS[s]["name"])}{"" if released(s) else " <span class=\"tag-soon\">Soon</span>"}</a></li>'
        for s in ORDER)
    if slug:
        col = f'''<h4>{esc(APPS[slug]["name"])}</h4>
        <ul>
          <li><a href="/{slug}/privacy/">Privacy Policy</a></li>
          <li><a href="/{slug}/terms/">Terms of Use</a></li>
          <li><a href="mailto:{CONTACT}?subject={esc(APPS[slug]["name"])}">Support</a></li>
        </ul>'''
    else:
        col = f'''<h4>SuiteForge</h4>
        <ul>
          <li><a href="/#privacy">Our privacy approach</a></li>
          <li><a href="/#faq">FAQ</a></li>
          <li><a href="mailto:{CONTACT}">Contact</a></li>
        </ul>'''
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/">{MARK} SuiteForge</a>
        <p class="muted" style="margin-top:16px;max-width:36ch;font-size:.97rem;">Privacy-first iPhone apps for a calmer life. An independent studio, one focused tool at a time.</p>
      </div>
      <div>
        <h4>Apps</h4>
        <ul>{apps}</ul>
      </div>
      <div>
        {col}
      </div>
    </div>
    <div class="foot-base">
      <span>© {datetime.date.today().year} SuiteForge. All rights reserved.</span>
      <span>Made in France · No accounts · No tracking</span>
    </div>
  </div>
</footer>'''

def scripts():
    return f'<script src="{ver("/assets/reveal.js")}" defer></script>\n</body>\n</html>'

def org_jsonld():
    return {
        "@context": "https://schema.org", "@type": "Organization", "@id": ORG_ID,
        "name": "SuiteForge", "url": f"{DOMAIN}/",
        "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/assets/logo.png", "width": 512, "height": 512},
        "email": CONTACT,
        "description": "Independent studio making privacy-first iPhone apps for health, wellness, productivity and education. No accounts, no tracking, data stored on-device.",
        "foundingLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressCountry": "FR"}},
        "sameAs": [appstore_url(s) for s in ORDER if released(s)],
    }

def app_jsonld(slug):
    a = APPS[slug]
    canonical = f"{DOMAIN}/{slug}/"
    d = {
        "@context": "https://schema.org", "@type": "MobileApplication",
        "@id": f"{canonical}#app",
        "name": a["name"], "alternateName": a["full_name"],
        "operatingSystem": "iOS", "applicationCategory": a["schema_category"],
        "description": a["seo_desc"], "url": canonical,
        "image": DOMAIN + ver(f"/{slug}/icon.webp"),
        "screenshot": [DOMAIN + ver(f"/{slug}/screenshots/{fn}") for fn, _ in a["shots"] if has(f"/{slug}/screenshots/{fn}")],
        "inLanguage": a.get("languages", ["en"]),
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "category": "free"},
        "publisher": {"@id": ORG_ID}, "author": {"@id": ORG_ID},
    }
    if released(slug):
        d["installUrl"] = d["downloadUrl"] = appstore_url(slug)
        d["offers"]["url"] = appstore_url(slug)
        d["offers"]["availability"] = "https://schema.org/InStock"
    else:
        d["offers"]["availability"] = "https://schema.org/PreOrder"
    if a.get("kids"):
        d["audience"] = {"@type": "PeopleAudience", "suggestedMinAge": 6}
        d["educationalLevel"] = "Beginner (CEFR A1 to B1)"
        d["teaches"] = "Serbian language, Latin and Cyrillic alphabets"
    return d

def faq_jsonld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]}

def crumbs_jsonld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def faq_html(faq):
    return "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in faq)

# ---------------------------------------------------------------------------
# LANDING PAGE
# ---------------------------------------------------------------------------
def build_shots(slug):
    a = APPS[slug]
    available = [(fn, alt) for fn, alt in a.get("shots") or [] if has(f"/{slug}/screenshots/{fn}")]
    if not available:
        return ""
    w, h = a.get("shots_w", 620), a.get("shots_h", 1347)
    imgs = "".join(
        f'<figure class="shot"><img src="{ver(f"/{slug}/screenshots/{fn}")}" alt="{esc(alt)}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async"></figure>'
        for fn, alt in available)
    return f'''
<section class="shots-section" data-shots aria-labelledby="shots-title">
  <div class="shots-head">
    <div>
      <p class="eyebrow reveal">See it in action</p>
      <h2 class="reveal" id="shots-title">Real screens from {esc(a['name'])}.</h2>
    </div>
    <div class="shots-nav">
      <button type="button" data-prev aria-label="Previous screenshots">{svg("left")}</button>
      <button type="button" data-next aria-label="Next screenshots">{svg("right")}</button>
    </div>
  </div>
  <div class="shots" role="list" aria-label="{esc(a['name'])} screenshots" tabindex="0">{imgs}</div>
</section>'''

def more_apps(slug):
    cards = "".join(f'''<a class="card reveal themed" href="/{s}/" style="{theme(APPS[s])}display:flex;gap:16px;align-items:center;padding:20px 22px;">
        {icon_block(s, 52)}
        <div><div class="app-card-cat">{esc(APPS[s]['category_label'])}</div><h3 style="font-size:1.18rem;margin-top:2px;">{esc(APPS[s]['name'])}</h3></div>
      </a>''' for s in ORDER if s != slug)
    return f'''<section class="section-sm">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow reveal">More from SuiteForge</p><h2 class="reveal" style="font-size:clamp(1.6rem,3vw,2.2rem);">Same principles, other corners of life.</h2></div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;">{cards}</div>
  </div>
</section>'''

def build_landing(slug):
    a = APPS[slug]
    canonical = f"{DOMAIN}/{slug}/"
    name = esc(a["name"])

    extra_head = ""
    if has(f"/{slug}/screenshots/hero-home.webp"):
        extra_head += f'<link rel="preload" as="image" href="{ver(f"/{slug}/screenshots/hero-home.webp")}" fetchpriority="high">\n'
        back = next((fn for fn, _ in a["shots"] if has(f"/{slug}/screenshots/{fn}")), None)
        visual = f'''<div class="hero-visual reveal" style="--d:.1s">
          <span class="ring"></span><span class="ring"></span>
          <div class="duo">
            {phone(slug, eager=True)}
            {f'<div class="phone phone--shot back" aria-hidden="true"><div class="phone-screen"><img src="{ver(f"/{slug}/screenshots/{back}")}" alt="" width="620" height="1347" loading="lazy" decoding="async"></div></div>' if back else ''}
          </div>
        </div>'''
    else:
        visual = f'<div class="hero-visual"><div class="phone"><div class="phone-screen"><div class="phone-notch"></div>{a.get("mock", "")}</div></div></div>'
    if released(slug):
        extra_head += f'<meta name="apple-itunes-app" content="app-id={a["appstore_id"]}">\n'
    favicon = f'<link rel="icon" type="image/webp" href="{ver(f"/{slug}/icon.webp")}">' if has(f"/{slug}/icon.webp") else None

    highlights = ""
    if a.get("highlights"):
        highlights = '<section class="section-sm" style="padding-top:0;"><div class="wrap"><div class="highlights reveal">' + "".join(
            f'<div class="highlight"><b>{esc(b)}</b><span>{esc(t)}</span></div>' for b, t in a["highlights"]) + '</div></div></section>'

    n = len(a["features"])
    features = "".join(
        f'''<div class="card reveal{' wide' if (n % 2 and i == n - 1) else ''}" style="--d:{(i % 2) * .08:.2f}s">
          <div class="feature-ico">{svg(ico, "1.8")}</div>
          <h3>{esc(t)}</h3><p>{esc(d)}</p>
        </div>''' for i, (t, d, ico) in enumerate(a["features"]))
    steps = "".join(
        f'<div class="step reveal" style="--d:{i * .1:.1f}s"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for i, (t, d) in enumerate(a["steps"]))
    perms = "".join(
        f'<div class="perm reveal"><h3>{svg("lock")}{esc(p)}</h3><p>{esc(d)}</p></div>' for p, d in a["permissions"])

    if released(slug):
        getbar = f'''<div class="getbar" role="complementary" aria-label="Get {name}">
  {icon_img(slug, 40)}<div><strong>{name}</strong><span>{esc(a["price_note"])}</span></div>
  <a class="btn btn-primary btn-sm" href="{appstore_url(slug)}">Get</a>
</div>'''
        cta_title, cta_text = f"Start with {name} today.", "Free to download. No account. Your data stays yours."
    else:
        getbar = ""
        cta_title, cta_text = f"{name} is coming to the App Store.", "Very soon on iPhone. No account, no ads, and your family's data stays at home."

    jsonld = [app_jsonld(slug), faq_jsonld(a["faq"]),
              crumbs_jsonld([("SuiteForge", f"{DOMAIN}/"), (a["name"], canonical)])]

    return f'''{head(a['seo_title'], a['seo_desc'], canonical, body_style=theme(a), jsonld=jsonld, extra_head=extra_head, og=og_image(slug), og_alt=f"{a['name']}: {a['tagline']}", favicon=favicon)}
{site_header(slug)}
<main id="main">
<section class="app-hero">
  <div class="wrap">
    <div class="app-hero-grid">
      <div>
        <div class="app-id reveal">
          {icon_block(slug, 76, lazy=False)}
          <div>
            <div class="app-cat">{esc(a['category_label'])} · iPhone{'' if released(slug) else ' · <span class="tag-soon" style="vertical-align:1px;">Coming soon</span>'}</div>
            <div class="app-name">{name}</div>
          </div>
        </div>
        <h1 class="reveal">{esc(a['tagline'])}</h1>
        <p class="lede reveal">{esc(a['hero_sub'])}</p>
        <div class="cta-row reveal" data-hero>{appstore_badge(slug)}<span class="price-note">{esc(a.get('price_note', ''))}</span></div>
        <div class="trust reveal">
          <span>{svg("shield")} No account</span>
          <span>{svg("noeye")} No tracking</span>
          <span>{svg("device")} Data stays on your iPhone</span>
        </div>
      </div>
      {visual}
    </div>
  </div>
</section>
{highlights}
{build_shots(slug)}
<section class="section band">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow reveal">What it does</p><h2 class="reveal">Everything you need, nothing you don't.</h2></div>
    <div class="bento">{features}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow reveal">How it works</p><h2 class="reveal">Three steps, then it's a habit.</h2></div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section ink-band">
  <div class="wrap">
    <div class="privacy-grid">
      <div>
        <p class="eyebrow reveal">Privacy</p>
        <h2 class="reveal" style="margin-top:12px;">{name} keeps your data on your device.</h2>
        <p class="reveal" style="margin-top:16px;max-width:46ch;">No SuiteForge account. No analytics. No advertising trackers. Here is exactly what {name} can access, and why.</p>
        <ul class="checks reveal">
          <li>{svg("check", "3")} No ads, no analytics, no trackers</li>
          <li>{svg("check", "3")} Every permission is optional</li>
          <li>{svg("check", "3")} Nothing stored on our servers</li>
        </ul>
        <p class="faint reveal" style="margin-top:26px;">Full details in the <a class="link" href="/{slug}/privacy/">{name} Privacy Policy</a>.</p>
      </div>
      <div class="perm-list">{perms}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <div class="section-head"><p class="eyebrow reveal">Questions</p><h2 class="reveal">Frequently asked</h2></div>
    <div class="faq reveal">{faq_html(a['faq'])}</div>
  </div>
</section>

<section class="section-sm" id="get">
  <div class="wrap">
    <div class="cta-card reveal">
      {icon_block(slug, 76)}
      <h2>{cta_title}</h2>
      <p>{cta_text}</p>
      <div style="display:flex;justify-content:center;">{appstore_badge(slug)}</div>
    </div>
  </div>
</section>
{more_apps(slug)}
</main>
{site_footer(slug)}
{getbar}
{scripts()}'''

# ---------------------------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------------------------
HOME_FAQ = [
    ("Does SuiteForge collect my personal data?", "No. SuiteForge apps store everything on your device (some can also sync through your own private iCloud). There are no SuiteForge accounts, no analytics SDKs and no third-party trackers. The only data that leaves your device is the anonymous purchase information Apple and our subscription provider need to manage a subscription."),
    ("Do I need an account?", "No. SuiteForge apps work immediately on first launch: no sign-up, no email, no password."),
    ("What kinds of apps does SuiteForge make?", "Focused, single-purpose iPhone apps: Health & Wellness (intermittent fasting, morning routines, step tracking), Productivity (KeepContact, a private personal CRM) and Education (Ježko, Serbian for kids and families). Each app does one thing well and runs on-device."),
    ("Are the apps free?", "Each app is free to download, with an optional subscription that unlocks advanced features; some also offer a one-time lifetime purchase. You can use the core of every app without paying."),
    ("Do you make apps for children?", "Yes: Ježko teaches Serbian to children aged 6 to 14 and their families. Like every SuiteForge app, it has no ads, no account and no tracking, and purchases and external links sit behind a parental gate on a child profile."),
    ("How do I get help or suggest a feature?", f"Every app has a feedback option in its settings, or you can email {CONTACT} directly. We read everything."),
]

def home_card(slug, layout, i):
    a = APPS[slug]
    soon = "" if released(slug) else ' <span class="tag-soon">Coming soon</span>'
    pills = ""
    if layout == "feature" and a.get("home_pills"):
        pills = '<div class="pill-list">' + "".join(f'<span class="pill">{esc(p)}</span>' for p in a["home_pills"]) + "</div>"
    label = "New · " if layout == "feature" and not released(slug) else ""
    shot = ""
    if has(f"/{slug}/screenshots/hero-home.webp"):
        shot = f'<div class="app-card-shot" aria-hidden="true">{phone(slug, alt="")}</div>'
    return f'''<a class="app-card app-card--{layout} themed reveal" href="/{slug}/" style="{theme(a)}--d:{(i % 2) * .08:.2f}s">
        <div class="app-card-body">
          <div class="app-card-top">{icon_block(slug, 56 if layout != "feature" else 64)}<div><div class="app-card-cat">{label}{esc(a['category_label'])}</div><h3>{esc(a['name'])}{soon}</h3></div></div>
          <p class="app-card-text">{esc(a['home_blurb'])}</p>
          {pills}
          <span class="app-card-more">Discover {esc(a['name'])} {svg("arrow")}</span>
        </div>
        {shot}
      </a>'''

def build_home():
    title = "SuiteForge — Privacy-first iPhone apps for a calmer life"
    desc = "Privacy-first iPhone apps for health, habits, relationships and learning: FastClear, RoutineFlow, WalkQuest, KeepContact and Ježko. No accounts, no tracking."
    canonical = f"{DOMAIN}/"
    new = next((s for s in ORDER if APPS[s].get("status") == "soon"), None)
    announce = ""
    if new:
        a = APPS[new]
        announce = f'''<a class="announce reveal" href="/{new}/">{icon_img(new, 26, lazy=False)}<span><b>New: {esc(a['name'])}</b> · {esc(a['category_label'])}, coming soon</span><span class="arrow" aria-hidden="true">→</span></a>'''
    fan = "".join(phone(s, alt=APPS[s].get("hero_shot_alt"), eager=(k == 1)) for k, s in enumerate(HOME_FAN))
    stack = "".join(icon_img(s, 34, lazy=False) for s in ORDER)
    cards = "".join(home_card(s, layout, i) for i, (s, layout) in enumerate(HOME_LAYOUT))

    jsonld = [
        org_jsonld(),
        {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{DOMAIN}/#website", "name": "SuiteForge", "url": canonical, "publisher": {"@id": ORG_ID}, "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "ItemList", "name": "SuiteForge apps", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{DOMAIN}/{s}/", "name": APPS[s]["name"]} for i, s in enumerate(ORDER)]},
        faq_jsonld(HOME_FAQ),
    ]
    principles = [
        ("One job, done well", "Each app solves one problem and stops there. No feature bloat, no endless settings, no feed."),
        ("Calm by design", "No streak shaming, no red badges, no guilt. Miss a day and nothing breaks: you simply begin again."),
        ("Fair, honest pricing", "Free to download, a useful free core, an optional subscription, and often a lifetime option. Never ads."),
    ]
    principles_html = "".join(
        f'<div class="card reveal" style="--d:{i * .08:.2f}s"><div class="feature-ico">{svg(ic, "1.8")}</div><h3 style="font-size:1.3rem;margin-bottom:8px;">{esc(t)}</h3><p class="muted" style="font-size:1rem;">{esc(d)}</p></div>'
        for i, ((t, d), ic) in enumerate(zip(principles, [
            '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.2"/>',
            '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
            '<path d="M20 12V7l-8-4-8 4v5c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9z"/><path d="M9 12l2 2 4-4"/>'])))

    return f'''{head(title, desc, canonical, jsonld=jsonld, extra_head=f'<link rel="preload" as="image" href="{ver(f"/{HOME_FAN[1]}/screenshots/hero-home.webp")}" fetchpriority="high">', og_alt="SuiteForge: privacy-first iPhone apps")}
{site_header()}
<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        {announce}
        <h1 class="display reveal">Apps for a calmer, <em>quieter</em> life.</h1>
        <p class="lede reveal">SuiteForge makes small, focused iPhone apps that help you take care of yourself: your health, your habits, your relationships, your family's language. Each one runs on your device. Nothing to sign up for. Nothing watching over your shoulder.</p>
        <div class="hero-cta reveal">
          <a class="btn btn-primary" href="#apps">Explore the apps {svg("arrow")}</a>
          <a class="btn btn-ghost" href="#privacy">Why privacy-first</a>
        </div>
        <div class="hero-proof reveal"><span class="icon-stack">{stack}</span><span>{len(ORDER)} apps · Made in France · Zero trackers</span></div>
      </div>
      <div class="fan reveal" style="--d:.1s" aria-label="Screens from SuiteForge apps">{fan}</div>
    </div>
  </div>
</section>

<section class="section band" id="apps">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow reveal">The apps</p><h2 class="reveal">Small tools for the things that matter.</h2><p class="lede reveal">Health, habits, relationships, learning. Different corners of life, the same promise: your data stays yours.</p></div>
    <div class="apps-grid">{cards}</div>
  </div>
</section>

<section class="section ink-band" id="privacy">
  <div class="wrap">
    <p class="eyebrow reveal">Why privacy-first</p>
    <h2 class="reveal" style="margin-top:12px;max-width:18ch;">Your life is yours. Not a dataset.</h2>
    <div class="stats">
      <div class="stat reveal"><div class="num">0</div><h3>Accounts</h3><p>No sign-up, no email, no password. There is no SuiteForge login because there is nothing for us to log in to.</p></div>
      <div class="stat reveal" style="--d:.08s"><div class="num">0</div><h3>Trackers</h3><p>No analytics SDKs, no advertising IDs, no third-party trackers. We don't measure you because we don't need to.</p></div>
      <div class="stat reveal" style="--d:.16s"><div class="num">100%</div><h3>On your device</h3><p>Your fasts, routines, steps, contacts and lessons live on your iPhone, or in your own private iCloud. Never on our servers.</p></div>
    </div>
    <p class="faint reveal" style="margin-top:34px;max-width:72ch;">The one exception: to manage an optional subscription, Apple and our payment provider process an anonymous purchase identifier. It is never linked to your personal content, and each app's privacy policy spells this out in plain language.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow reveal">How we build</p><h2 class="reveal">Fewer features. More care.</h2></div>
    <div class="grid grid-3">{principles_html}</div>
  </div>
</section>

<section class="section band" id="faq">
  <div class="wrap narrow">
    <div class="section-head"><p class="eyebrow reveal">Questions</p><h2 class="reveal">Good to know</h2></div>
    <div class="faq reveal">{faq_html(HOME_FAQ)}</div>
  </div>
</section>
</main>
{site_footer()}
{scripts()}'''

# ---------------------------------------------------------------------------
# LEGAL PAGES
# ---------------------------------------------------------------------------
UPDATED = "29 May 2026"

def legal_page(slug, kind, title, desc, sections, intro=""):
    a = APPS[slug]
    canonical = f"{DOMAIN}/{slug}/{kind}/"
    body = "".join(f"\n  <h2>{i}. {t}</h2>\n  {c}" for i, (t, c) in enumerate(sections, 1))
    jsonld = [crumbs_jsonld([("SuiteForge", f"{DOMAIN}/"), (a["name"], f"{DOMAIN}/{slug}/"), (title, canonical)])]
    return f'''{head(f"{title} — {a['name']}", desc, canonical, body_style=theme(a), jsonld=jsonld, og=og_image(slug))}
{site_header(slug)}
<main class="legal" id="main">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">SuiteForge</a><span>/</span><a href="/{slug}/">{esc(a['name'])}</a><span>/</span><span>{title}</span></nav>
  <h1>{title}</h1>
  <p class="updated">{esc(a['name'])} · Last updated {a.get('updated', UPDATED)}</p>
  {intro}{body}

  <p style="margin-top:40px;"><a href="/{slug}/">← Back to {esc(a['name'])}</a></p>
</main>
{site_footer(slug)}
{scripts()}'''

def build_privacy(slug):
    a = APPS[slug]
    name = esc(a["name"])
    mail = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'
    if a.get("icloud", True):
        short_storage = f"{name} stores your data on your device, optionally synced through your own private iCloud."
        storage = f"Everything you create in {name} is stored locally on your device using Apple's on-device frameworks. If you enable iCloud, this data may sync through your own private Apple iCloud account, which SuiteForge cannot access. We do not operate any server that stores your personal content."
    else:
        short_storage = f"{name} stores your data on your device only. It does not sync to any cloud."
        storage = f"Everything you create in {name} is stored locally on your device using Apple's on-device frameworks. {name} does not sync your data to iCloud or to any other cloud service, and we do not operate any server that stores your personal content."
        if slug == "keepcontact":
            storage += " If you create a backup or an export, it is a file you choose where to save; backups can be encrypted with a password only you know."
    extra = "".join(f"\n  <h3>{esc(t)}</h3>\n  <p>{esc(d.format(name=a['name']))}</p>" for t, d in a.get("privacy_extra", []))
    perms = "".join(f"<h3>{esc(p)}</h3><p>{esc(d)}</p>" for p, d in a["permissions"])
    if a.get("kids"):
        children = (f"<p>{name} is designed to be used by children together with their parents. We do not collect personal data from anyone, including children: "
                    f"profile names, recordings and progress are stored only on your device and are never sent to SuiteForge. {name} contains no advertising, "
                    "no third-party analytics, no chat and no social features.</p>"
                    "<p>On a child profile, purchases, links that leave the app and sharing are protected by a parental gate. Purchases are made by the adult who "
                    "holds the Apple Account; the anonymous purchase data described in section 4 relates to that account, not to the child. "
                    f"If you have any question about your child's use of {name}, contact us at {mail}.</p>")
    else:
        children = f"<p>{name} is not directed to children under 13, and we do not knowingly collect personal data from children.</p>"
    lifetime = " and an optional one-time lifetime purchase" if a.get("lifetime") else ""
    sections = [
        ("Who we are", f"<p>{name} is an iPhone app published by SuiteForge. For any privacy question, contact us at {mail}.</p>"),
        ("Data stored on your device", f"<p>{storage}</p>{extra}"),
        (f"Permissions {name} may request", f"{perms}<p>Each permission is optional, is requested only when relevant, and can be changed at any time in the iOS Settings app.</p>"),
        ("Subscriptions and purchases", f'<p>{name} offers an optional auto-renewing subscription{lifetime}. Purchases are processed by Apple. To deliver and restore purchases across your devices, we use RevenueCat, Inc. as a service provider. For this purpose only, an anonymous app-user identifier together with purchase and receipt information is processed by Apple and RevenueCat. This information is not linked to your personal content in the app and is not used for advertising. See <a href="https://www.apple.com/legal/privacy/" target="_blank" rel="noopener">Apple\'s Privacy Policy</a> and <a href="https://www.revenuecat.com/privacy" target="_blank" rel="noopener">RevenueCat\'s Privacy Policy</a>.</p>'),
        ("What we do not do", "<ul><li>We do not require or create an account.</li><li>We do not use third-party analytics or advertising SDKs.</li><li>We do not track you across apps or websites.</li><li>We do not sell, rent or trade your personal data.</li></ul>"),
        ("Your rights", f"<p>Because your content is stored on your own device, you remain in control of it at all times: you can edit or delete it within the app, and removing the app removes its local data. As {name} is published from France, the EU General Data Protection Regulation (GDPR) applies to the limited purchase-related processing described above; you may exercise your applicable rights of access, rectification, erasure and objection by contacting {mail}.</p>"),
        ("Children", children),
        ("Changes to this policy", "<p>We may update this policy as the app evolves. Material changes will be reflected here with a new \"last updated\" date.</p>"),
        ("Contact", f"<p>Questions about this policy? Email {mail}.</p>"),
    ]
    intro = f'<div class="callout"><p><strong>The short version.</strong> {short_storage} There is no {name} account. We do not use analytics or advertising trackers, and we never sell your data. The only information that leaves your device is the anonymous purchase data needed to manage an optional subscription.</p></div>'
    return legal_page(slug, "privacy", "Privacy Policy",
                      f"How {a['name']} handles your data. Short version: it stays on your device. No accounts, no tracking.", sections, intro)

def build_terms(slug):
    a = APPS[slug]
    name = esc(a["name"])
    lifetime = " A one-time lifetime purchase is also available: it is charged once, does not renew, and unlocks the same features for as long as the app is offered." if a.get("lifetime") else ""
    family = " Purchases can be shared with your family through Apple's Family Sharing." if a.get("family_sharing") else ""
    trial = " If a free trial is offered and you do not cancel at least 24 hours before it ends, the subscription starts automatically at the price shown."
    sections = [
        ("Acceptance", f"<p>By downloading or using {name} (\"the app\"), you agree to these Terms of Use. If you do not agree, please do not use the app. The app is published by SuiteForge.</p>"),
        ("Licence", f"<p>SuiteForge grants you a personal, non-transferable, non-exclusive licence to use {name} on Apple devices that you own or control, in accordance with the Apple Media Services Terms and these Terms.</p>"),
        ("Subscriptions", f"<p>{name} is free to download and includes optional auto-renewing subscriptions. Payment is charged to your Apple Account at confirmation of purchase. A subscription renews automatically unless cancelled at least 24 hours before the end of the current period. You can manage or cancel your subscription in your Apple Account settings. Prices are shown in the app before purchase and may vary by region.{trial}{lifetime}{family}</p>"),
    ]
    if a["schema_category"] == "HealthApplication":
        sections.append(("Not medical advice", f"<p>{name} is provided for general informational and wellness purposes only. It is not a medical device and does not provide medical advice, diagnosis or treatment. Always consult a qualified healthcare professional before making changes to your diet, fasting, exercise or health routine, and especially if you are pregnant, nursing, under 18, or have any medical condition. Never disregard professional medical advice because of something in this app.</p>"))
    if a.get("kids"):
        sections.append(("Use by children", f"<p>{name} is designed for children to use with the involvement of a parent or guardian, who accepts these Terms on their behalf. Purchases must be made by an adult; on a child profile, purchases and links that leave the app are protected by a parental gate.</p>"))
        sections.append(("Educational content", f"<p>{name} is a learning aid. We take care to make its content accurate and suitable for children, but we do not guarantee any particular level of language proficiency. Voices in the app may be synthesised.</p>"))
    sections += [
        ("Acceptable use", "<p>You agree to use the app only for lawful purposes and not to attempt to disrupt, reverse-engineer or misuse it beyond what applicable law permits.</p>"),
        ("Intellectual property", f"<p>The app, its design, its stories, characters, illustrations and audio, and the SuiteForge and {name} names and logos are the property of SuiteForge and are protected by intellectual-property law. The content you create within the app belongs to you.</p>"),
        ("Disclaimer and limitation of liability", "<p>The app is provided \"as is\" and \"as available\" without warranties of any kind, to the fullest extent permitted by law. SuiteForge is not liable for any indirect or consequential loss arising from your use of the app. Nothing in these Terms limits liability that cannot be limited under applicable law.</p>"),
        ("Governing law", "<p>These Terms are governed by French law. Mandatory consumer-protection rules of your country of residence continue to apply.</p>"),
        ("Contact", f'<p>Questions about these Terms? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>'),
    ]
    return legal_page(slug, "terms", "Terms of Use", f"The terms that apply when you use {a['name']}.", sections)

# ---------------------------------------------------------------------------
# WRITE FILES
# ---------------------------------------------------------------------------
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓", path)

if __name__ == "__main__":
    print("Generating SuiteForge site...")
    write("index.html", build_home())
    for slug in ORDER:
        write(f"{slug}/index.html", build_landing(slug))
        write(f"{slug}/privacy/index.html", build_privacy(slug))
        write(f"{slug}/terms/index.html", build_terms(slug))

    urls = [(f"{DOMAIN}/", "1.0")]
    for slug in ORDER:
        urls += [(f"{DOMAIN}/{slug}/", "0.8"), (f"{DOMAIN}/{slug}/privacy/", "0.3"), (f"{DOMAIN}/{slug}/terms/", "0.3")]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, pr in urls:
        sitemap += f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n"
    sitemap += "</urlset>\n"
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write("CNAME", "suiteforge.app\n")
    print("Done.")
