#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SuiteForge static site generator.
Generates: 4 landing pages, 8 legal pages (privacy + terms), sitemap.xml, robots.txt, CNAME.
Single source of truth = APPS config below. No external deps.
"""
import os, html

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
        "seo_title": "FastClear — Simple, private intermittent fasting timer for iPhone",
        "seo_desc": "FastClear is a privacy-first intermittent fasting timer for iPhone. Track 16:8, 18:6, OMAD and custom fasts. No account, no tracking, all data on your device.",
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
        "seo_title": "WalkQuest — Private step tracker & walking goals for iPhone",
        "seo_desc": "WalkQuest is a privacy-first step tracker for iPhone. Set daily walking goals, see honest progress, no account and no tracking. Reads steps from Apple Health on your device.",
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
        "seo_title": "KeepContact — Private personal CRM with on-device AI, for iPhone",
        "seo_desc": "KeepContact is a privacy-first personal CRM for iPhone. See who to reach out to each morning, remember what matters to each person, get message ideas from Apple's on-device AI. No account, no tracking, 100% offline.",
        "updated": "11 October 2026",
        "icloud": False,
        "lifetime": True,
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
}

ORDER = ["fastclear", "routineflow", "walkquest", "keepcontact"]

# ---------------------------------------------------------------------------
# SHARED PARTIALS
# ---------------------------------------------------------------------------
def appstore_badge(slug):
    a = APPS[slug]
    return f'''<a class="appstore" href="https://apps.apple.com/app/id{a['appstore_id']}" aria-label="Download {a['name']} on the App Store">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.5 1.6c.1 1-.3 2-1 2.8-.7.8-1.8 1.4-2.8 1.3-.1-1 .4-2 1-2.7.7-.8 1.9-1.4 2.8-1.4zM19 17c-.4 1-.6 1.4-1.1 2.3-.8 1.3-1.9 2.9-3.3 2.9-1.2 0-1.5-.8-3.2-.8s-2 .8-3.2.8c-1.4 0-2.4-1.4-3.2-2.7-2.2-3.5-2.5-7.6-1.1-9.8 1-1.6 2.6-2.5 4.1-2.5 1.5 0 2.4.8 3.6.8 1.1 0 1.8-.8 3.5-.8 1.3 0 2.7.7 3.7 2-3.2 1.8-2.7 6.4.5 7.8z"/></svg>
      <span><small>Download on the</small><strong>App Store</strong></span>
    </a>'''

def ver(path):
    """Cache-busting URL for a local file: /path?v=<content hash>, so browsers
    pick up a new screenshot or icon right after a deploy."""
    import hashlib
    with open(os.path.join(ROOT, path.lstrip("/")), "rb") as f:
        return f"{path}?v={hashlib.md5(f.read()).hexdigest()[:8]}"

def og_image(slug=None):
    """Per-app share image (<slug>/og.png, made by make_og.py) if present."""
    if slug and os.path.isfile(os.path.join(ROOT, slug, "og.png")):
        return DOMAIN + ver(f"/{slug}/og.png")
    return DOMAIN + ver("/assets/og-suiteforge.png")

def head(title, desc, canonical, theme, extra_jsonld="", extra_head="", og=None):
    og = og or og_image()
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#f7f3ec">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SuiteForge">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
<link rel="preload" href="/assets/fonts/fraunces-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/hanken-grotesk-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">
{extra_head}
{extra_jsonld}
</head>
<body style="{theme}">'''

def site_header():
    return '''<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/"><span class="mark">S</span> SuiteForge</a>
    <nav class="nav">
      <a href="/#apps">Apps</a>
      <a href="/#privacy" class="hide-sm">Privacy</a>
    </nav>
  </div>
</header>'''

def site_footer(slug=None):
    legal = ""
    if slug:
        legal = f'''<li><a href="/{slug}/privacy/">Privacy Policy</a></li>
          <li><a href="/{slug}/terms/">Terms of Use</a></li>'''
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/"><span class="mark">S</span> SuiteForge</a>
        <p class="muted" style="margin-top:14px;max-width:34ch;font-size:.96rem;">Privacy-first iPhone apps for a calmer life. Built with care, one focused tool at a time.</p>
      </div>
      <div>
        <h4>Apps</h4>
        <ul>
          <li><a href="/fastclear/">FastClear</a></li>
          <li><a href="/routineflow/">RoutineFlow</a></li>
          <li><a href="/walkquest/">WalkQuest</a></li>
          <li><a href="/keepcontact/">KeepContact</a></li>
        </ul>
      </div>
      <div>
        <h4>{'This app' if slug else 'Company'}</h4>
        <ul>
          {legal if slug else '<li><a href="/#privacy">Privacy approach</a></li><li><a href="/#faq">FAQ</a></li>'}
          <li><a href="mailto:suiteforgeops@gmail.com">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>© 2026 SuiteForge. All rights reserved.</span>
      <span>Made in France · No accounts · No tracking</span>
    </div>
  </div>
</footer>
<script src="/assets/reveal.js"></script>
</body>
</html>'''

def build_shots(slug):
    """Render the App Store screenshots gallery, or '' if none configured /
    no optimized files on disk. Files must exist at <slug>/screenshots/<file>."""
    a = APPS[slug]
    shots = a.get("shots") or []
    if not shots:
        return ""
    # Skip silently any file that hasn't been optimized yet
    available = [
        (fn, alt) for fn, alt in shots
        if os.path.isfile(os.path.join(ROOT, slug, "screenshots", fn))
    ]
    if not available:
        return ""
    variant = a.get("shots_type", "brut")
    w = a.get("shots_w", 620)
    h = a.get("shots_h", 1344)
    imgs = "".join(
        f'<figure class="shot reveal">'
        f'<img src="{ver(f"/{slug}/screenshots/{fn}")}" alt="{html.escape(alt)}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async">'
        f'</figure>'
        for fn, alt in available
    )
    return f'''
<section class="shots-section">
  <div class="shots-head">
    <p class="eyebrow reveal">See it in action</p>
    <h2 class="reveal" style="margin:10px 0 0;">Real screens from {a['name']}.</h2>
  </div>
  <div class="shots shots--{variant}" role="list" aria-label="{html.escape(a['name'])} screenshots">{imgs}</div>
</section>'''

def icon_block(slug, size=56):
    """Render an app icon. Uses the real App Store icon (<slug>/icon.webp) if
    present; otherwise falls back to the hand-drawn SVG placeholder."""
    a = APPS[slug]
    r = int(size * 0.27)
    icon_path = os.path.join(ROOT, slug, "icon.webp")
    if os.path.isfile(icon_path):
        return (
            f'<div class="app-icon app-icon--real" '
            f'style="width:{size}px;height:{size}px;border-radius:{r}px;">'
            f'<img src="{ver(f"/{slug}/icon.webp")}" alt="{html.escape(a["name"])} app icon" '
            f'width="{size}" height="{size}" loading="lazy" decoding="async">'
            f'</div>'
        )
    return f'''<div class="app-icon" style="width:{size}px;height:{size}px;border-radius:{r}px;">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{a['icon_svg']}</svg>
    </div>'''

# ---------------------------------------------------------------------------
# LANDING PAGE
# ---------------------------------------------------------------------------
def build_landing(slug):
    a = APPS[slug]
    theme = f"--accent:{a['accent']};--accent-deep:{a['accent_deep']};--accent-tint:{a['accent_tint']};"
    canonical = f"{DOMAIN}/{slug}/"

    # Hero: real screenshot if available, else original HTML mock
    hero_path = os.path.join(ROOT, slug, "screenshots", "hero-home.webp")
    if os.path.isfile(hero_path):
        hero_alt = a.get("hero_shot_alt") or f"{a['name']} home screen"
        # Native dims of hero output are 680x1477 (we encode at 680 wide).
        hero_block = (
            f'<div class="phone phone--shot">'
            f'<div class="phone-screen">'
            f'<img src="{ver(f"/{slug}/screenshots/hero-home.webp")}" alt="{html.escape(hero_alt)}" '
            f'width="680" height="1477" loading="eager" fetchpriority="high" decoding="async">'
            f'</div></div>'
        )
        preload_link = (
            f'<link rel="preload" as="image" href="{ver(f"/{slug}/screenshots/hero-home.webp")}" '
            f'fetchpriority="high">'
        )
    else:
        hero_block = (
            f'<div class="phone"><div class="phone-screen">'
            f'<div class="phone-notch"></div>{a["mock"]}'
            f'</div></div>'
        )
        preload_link = ""

    # Per-landing favicon = the app's own icon (if optimized).
    favicon_link = ""
    if os.path.isfile(os.path.join(ROOT, slug, "icon.webp")):
        favicon_link = f'<link rel="icon" type="image/webp" href="{ver(f"/{slug}/icon.webp")}">'
    head_extra = preload_link + favicon_link

    faq_items = "".join(
        f"<details><summary>{html.escape(q)}</summary><p>{html.escape(ans)}</p></details>"
        for q, ans in a["faq"]
    )
    faq_jsonld_items = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (
            jsonstr(q), jsonstr(ans)) for q, ans in a["faq"]
    )
    features = "".join(
        f'''<div class="feature reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{svg}</svg></div>
          <div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>
        </div>''' for t, d, svg in a["features"]
    )
    steps = "".join(
        f'''<div class="card reveal" style="text-align:left;">
          <div style="font-family:var(--serif);font-weight:900;font-size:1.6rem;color:var(--accent);">{i+1}</div>
          <h3 style="font-family:var(--serif);font-weight:600;font-size:1.18rem;margin:8px 0 4px;">{html.escape(t)}</h3>
          <p class="muted" style="font-size:.97rem;">{html.escape(d)}</p>
        </div>''' for i, (t, d) in enumerate(a["steps"])
    )

    jsonld = f'''<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"SoftwareApplication",
  "name":{jsonstr(a['name'])},
  "operatingSystem":"iOS","applicationCategory":{jsonstr(a['schema_category'])},
  "description":{jsonstr(a['seo_desc'])},
  "url":"{canonical}",
  "offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},
  "publisher":{{"@type":"Organization","name":"SuiteForge","url":"{DOMAIN}/"}}
}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_jsonld_items}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"SuiteForge","item":"{DOMAIN}/"}},
{{"@type":"ListItem","position":2,"name":{jsonstr(a['name'])},"item":"{canonical}"}}]}}
</script>'''

    return f'''{head(a['seo_title'], a['seo_desc'], canonical, theme, jsonld, head_extra, og_image(slug))}
{site_header()}

<section class="app-hero">
  <div class="wrap">
    <div class="app-hero-grid">
      <div>
        <div class="app-id reveal">
          {icon_block(slug, 84)}
          <div>
            <div class="app-cat">{a['category_label']}</div>
            <div class="app-name">{a['name']}</div>
          </div>
        </div>
        <h1 class="display reveal" style="font-size:clamp(2.2rem,4.6vw,3.4rem);margin:6px 0 18px;">{html.escape(a['tagline'])}</h1>
        <p class="lede reveal">{html.escape(a['hero_sub'])}</p>
        <div class="reveal" style="margin-top:26px;">{appstore_badge(slug)}</div>
        <div class="trust reveal" style="margin-top:24px;">
          <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3z"/></svg> No account</span>
          <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3l18 18M10.6 5.1A9 9 0 0 1 21 12"/></svg> No tracking</span>
          <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg> Works offline</span>
        </div>
      </div>
      <div class="reveal">
        {hero_block}
      </div>
    </div>
  </div>
</section>
{build_shots(slug)}
<section class="section band">
  <div class="wrap">
    <p class="eyebrow reveal">What it does</p>
    <h2 class="reveal" style="margin:10px 0 30px;">Everything you need, nothing you don't.</h2>
    <div class="grid grid-2">{features}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow reveal">How it works</p>
    <h2 class="reveal" style="margin:10px 0 30px;">Three steps, then it's a habit.</h2>
    <div class="grid grid-3">{steps}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap" style="max-width:840px;">
    <p class="eyebrow reveal">Privacy</p>
    <h2 class="reveal" style="margin:10px 0 18px;">{a['name']} keeps your data on your device.</h2>
    <p class="muted reveal" style="max-width:60ch;">No SuiteForge account. No analytics. No advertising trackers. Here's exactly what {a['name']} can access, and why:</p>
    <div class="grid" style="margin-top:24px;gap:14px;">
      {"".join(f'<div class="card reveal"><h3 style="font-family:var(--sans);font-weight:700;font-size:1.02rem;">{html.escape(p)}</h3><p class="muted" style="font-size:.96rem;margin-top:4px;">{html.escape(d)}</p></div>' for p, d in a["permissions"])}
    </div>
    <p class="faint reveal" style="margin-top:20px;">Full details in the <a href="/{slug}/privacy/" style="color:var(--accent-deep);text-decoration:underline;text-underline-offset:2px;">{a['name']} Privacy Policy</a>.</p>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:840px;">
    <p class="eyebrow reveal">Questions</p>
    <h2 class="reveal" style="margin:10px 0 10px;">Frequently asked</h2>
    <div class="faq reveal" style="margin-top:18px;">{faq_items}</div>
  </div>
</section>

<section class="section-sm band">
  <div class="wrap" style="text-align:center;">
    <h2 class="reveal" style="margin-bottom:8px;">Start today, calmly.</h2>
    <p class="muted reveal" style="margin-bottom:22px;">Free to download. No account. Your data stays yours.</p>
    <div class="reveal" style="display:flex;justify-content:center;">{appstore_badge(slug)}</div>
  </div>
</section>

{site_footer(slug)}'''

# ---------------------------------------------------------------------------
# LEGAL PAGES
# ---------------------------------------------------------------------------
UPDATED = "29 May 2026"

def jsonstr(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def build_privacy(slug):
    a = APPS[slug]
    theme = f"--accent:{a['accent']};--accent-deep:{a['accent_deep']};--accent-tint:{a['accent_tint']};"
    canonical = f"{DOMAIN}/{slug}/privacy/"
    perms = "".join(
        f"<h3>{html.escape(p)}</h3><p>{html.escape(d)}</p>" for p, d in a["permissions"]
    )
    updated = a.get("updated", UPDATED)
    if a.get("icloud", True):
        short_storage = f"{a['name']} stores your data on your device, optionally synced through your own private iCloud."
        storage = f"Everything you create in {a['name']} is stored locally on your device using Apple's on-device frameworks. If you enable iCloud, this data may sync through your own private Apple iCloud account, which SuiteForge cannot access. We do not operate any server that stores your personal content."
    else:
        short_storage = f"{a['name']} stores your data on your device only. It does not sync to any cloud."
        storage = f"Everything you create in {a['name']} is stored locally on your device using Apple's on-device frameworks. {a['name']} does not sync your data to iCloud or to any other cloud service, and we do not operate any server that stores your personal content. If you create a backup or an export, it is a file you choose where to save; backups can be encrypted with a password only you know."
    ai = ""
    if slug == "keepcontact":
        ai = f"""
  <h3>On-device AI</h3>
  <p>On iPhones that support Apple Intelligence, {a['name']} uses Apple's on-device language model to summarise a contact, suggest message ideas and spot facts in your notes. Voice notes are transcribed on your device too. This processing happens entirely on your iPhone: your notes and recordings are not sent to SuiteForge, to Apple or to any third party.</p>"""
    return f'''{head(f"Privacy Policy — {a['name']}", f"How {a['name']} handles your data. Short version: it stays on your device. No accounts, no tracking.", canonical, theme, og=og_image(slug))}
{site_header()}
<main class="legal">
  <h1>Privacy Policy</h1>
  <p class="updated">{a['name']} · Last updated {updated}</p>

  <div class="callout"><p><strong>The short version.</strong> {short_storage} There is no {a['name']} account. We do not use analytics or advertising trackers, and we never sell your data. The only information that leaves your device is the anonymous purchase data needed to manage an optional subscription.</p></div>

  <h2>1. Who we are</h2>
  <p>{a['name']} is an iPhone app published by SuiteForge. For any privacy question, contact us at <a href="mailto:suiteforgeops@gmail.com">suiteforgeops@gmail.com</a>.</p>

  <h2>2. Data stored on your device</h2>
  <p>{storage}</p>{ai}

  <h2>3. Permissions {a['name']} may request</h2>
  {perms}
  <p>Each permission is optional, is requested only when relevant, and can be changed at any time in the iOS Settings app.</p>

  <h2>4. Subscriptions and purchases</h2>
  <p>{a['name']} offers an optional auto-renewing subscription{" and an optional one-time lifetime purchase" if a.get("lifetime") else ""}. Purchases are processed by Apple. To deliver and restore purchases across your devices, we use RevenueCat, Inc. as a service provider. For this purpose only, an anonymous app-user identifier together with purchase and receipt information is processed by Apple and RevenueCat. This information is not linked to your personal content in the app and is not used for advertising. See <a href="https://www.apple.com/legal/privacy/" target="_blank" rel="noopener">Apple's Privacy Policy</a> and <a href="https://www.revenuecat.com/privacy" target="_blank" rel="noopener">RevenueCat's Privacy Policy</a>.</p>

  <h2>5. What we do not do</h2>
  <ul>
    <li>We do not require or create an account.</li>
    <li>We do not use third-party analytics or advertising SDKs.</li>
    <li>We do not track you across apps or websites.</li>
    <li>We do not sell, rent or trade your personal data.</li>
  </ul>

  <h2>6. Your rights</h2>
  <p>Because your content is stored on your own device, you remain in control of it at all times: you can edit or delete it within the app, and removing the app removes its local data. As {a['name']} is published from France, the EU General Data Protection Regulation (GDPR) applies to the limited purchase-related processing described above; you may exercise your applicable rights of access, rectification, erasure and objection by contacting <a href="mailto:suiteforgeops@gmail.com">suiteforgeops@gmail.com</a>.</p>

  <h2>7. Children</h2>
  <p>{a['name']} is not directed to children under 13, and we do not knowingly collect personal data from children.</p>

  <h2>8. Changes to this policy</h2>
  <p>We may update this policy as the app evolves. Material changes will be reflected here with a new "last updated" date.</p>

  <h2>9. Contact</h2>
  <p>Questions about this policy? Email <a href="mailto:suiteforgeops@gmail.com">suiteforgeops@gmail.com</a>.</p>

  <p style="margin-top:36px;"><a href="/{slug}/">← Back to {a['name']}</a></p>
</main>
{site_footer(slug)}'''

def build_terms(slug):
    a = APPS[slug]
    theme = f"--accent:{a['accent']};--accent-deep:{a['accent_deep']};--accent-tint:{a['accent_tint']};"
    canonical = f"{DOMAIN}/{slug}/terms/"
    is_health = a["schema_category"] == "HealthApplication"
    health_clause = ""
    if is_health:
        health_clause = f'''<h2>4. Not medical advice</h2>
  <p>{a['name']} is provided for general informational and wellness purposes only. It is not a medical device and does not provide medical advice, diagnosis or treatment. Always consult a qualified healthcare professional before making changes to your diet, fasting, exercise or health routine, and especially if you are pregnant, nursing, under 18, or have any medical condition. Never disregard professional medical advice because of something in this app.</p>'''
    updated = a.get("updated", UPDATED)
    lifetime = ""
    if a.get("lifetime"):
        lifetime = " A one-time lifetime purchase is also available: it is charged once, does not renew, and unlocks the same features for as long as the app is offered."
    return f'''{head(f"Terms of Use — {a['name']}", f"The terms that apply when you use {a['name']}.", canonical, theme, og=og_image(slug))}
{site_header()}
<main class="legal">
  <h1>Terms of Use</h1>
  <p class="updated">{a['name']} · Last updated {updated}</p>

  <h2>1. Acceptance</h2>
  <p>By downloading or using {a['name']} ("the app"), you agree to these Terms of Use. If you do not agree, please do not use the app. The app is published by SuiteForge.</p>

  <h2>2. Licence</h2>
  <p>SuiteForge grants you a personal, non-transferable, non-exclusive licence to use {a['name']} on Apple devices that you own or control, in accordance with the Apple Media Services Terms and these Terms.</p>

  <h2>3. Subscriptions</h2>
  <p>{a['name']} is free to download and includes optional auto-renewing subscriptions. Payment is charged to your Apple Account at confirmation of purchase. A subscription renews automatically unless cancelled at least 24 hours before the end of the current period. You can manage or cancel your subscription in your Apple Account settings. Prices are shown in the app before purchase and may vary by region.{lifetime}</p>

  {health_clause}

  <h2>{5 if is_health else 4}. Acceptable use</h2>
  <p>You agree to use the app only for lawful purposes and not to attempt to disrupt, reverse-engineer or misuse it beyond what applicable law permits.</p>

  <h2>{6 if is_health else 5}. Intellectual property</h2>
  <p>The app, its design, and the SuiteForge and {a['name']} names and logos are the property of SuiteForge and are protected by intellectual-property law. The content you create within the app belongs to you.</p>

  <h2>{7 if is_health else 6}. Disclaimer and limitation of liability</h2>
  <p>The app is provided "as is" and "as available" without warranties of any kind, to the fullest extent permitted by law. SuiteForge is not liable for any indirect or consequential loss arising from your use of the app. Nothing in these Terms limits liability that cannot be limited under applicable law.</p>

  <h2>{8 if is_health else 7}. Governing law</h2>
  <p>These Terms are governed by French law. Mandatory consumer-protection rules of your country of residence continue to apply.</p>

  <h2>{9 if is_health else 8}. Contact</h2>
  <p>Questions about these Terms? Email <a href="mailto:suiteforgeops@gmail.com">suiteforgeops@gmail.com</a>.</p>

  <p style="margin-top:36px;"><a href="/{slug}/">← Back to {a['name']}</a></p>
</main>
{site_footer(slug)}'''

# ---------------------------------------------------------------------------
# WRITE FILES
# ---------------------------------------------------------------------------
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓", path)

print("Generating SuiteForge site...")
for slug in ORDER:
    write(f"{slug}/index.html", build_landing(slug))
    write(f"{slug}/privacy/index.html", build_privacy(slug))
    write(f"{slug}/terms/index.html", build_terms(slug))

# sitemap
urls = [f"{DOMAIN}/"]
for slug in ORDER:
    urls += [f"{DOMAIN}/{slug}/", f"{DOMAIN}/{slug}/privacy/", f"{DOMAIN}/{slug}/terms/"]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    pr = "1.0" if u == f"{DOMAIN}/" else ("0.8" if u.count("/") == 4 else "0.4")
    sitemap += f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n"
sitemap += "</urlset>\n"
write("sitemap.xml", sitemap)

write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
write("CNAME", "suiteforge.app\n")

print("Done.")
