# ⏰ Timezone Fix Guide

## Problem: Borrow Time Shows 8 Hours Behind

This happens because the server stores times in UTC, but you're in Philippine Time (UTC+8).

---

## ✅ Solution: Install & Configure Timezone Support

### Step 1: Install pytz Library

```bash
pip install pytz
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### Step 2: Restart Server

```bash
# Stop the server (Ctrl+C)
# Then restart:
python app.py
```

### Step 3: Verify

```
✓ Server should show: "Using timezone: Asia/Manila"
✓ Borrow times should now be correct (Philippine Time)
```

---

## 🌍 Change Timezone (If Not in Philippines)

**File:** `app.py`  
**Line:** ~21

```python
TIMEZONE = pytz.timezone('Asia/Manila')  # Change this
```

### Common Timezones:

**Asia:**
- Philippines: `'Asia/Manila'`
- Singapore: `'Asia/Singapore'`
- Tokyo: `'Asia/Tokyo'`
- Hong Kong: `'Asia/Hong_Kong'`
- Bangkok: `'Asia/Bangkok'`

**Americas:**
- New York: `'America/New_York'`
- Los Angeles: `'America/Los_Angeles'`
- Chicago: `'America/Chicago'`

**Europe:**
- London: `'Europe/London'`
- Paris: `'Europe/Paris'`
- Berlin: `'Europe/Berlin'`

**Full list:** https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

---

## 🧪 Test the Fix

### Before Fix:
```
Borrow time: 02:30 AM (8 hours behind actual 10:30 AM)
```

### After Fix:
```
Borrow time: 10:30 AM (correct Philippine Time)
```

### To Test:
1. Borrow an item at the kiosk
2. Check Admin → Transactions tab
3. Verify borrow time matches your actual time
4. Check Admin → Reports tab → Export to Excel
5. Verify times in exported file

---

## ⚠️ If You Don't Install pytz

The system will still work, but:
- Times will be in server's local timezone (possibly UTC)
- You'll see a warning: "⚠️ Warning: pytz not installed"
- Times might be off by several hours

**Solution:** Just install pytz!

---

## 🔧 Technical Details

### What Changed:

**Before (UTC):**
```python
datetime.now()  # Always UTC
# 10:30 AM Philippine → Stores as 02:30 AM UTC
```

**After (Local Time):**
```python
get_local_time()  # Philippine Time
# 10:30 AM Philippine → Stores as 10:30 AM
```

### Functions Updated:
- `get_local_time()` - Gets current Philippine Time
- `ReturnPolicy.calculate_due_date()` - Uses local time for due dates
- `CooldownPenalty.calculate_cooldown()` - Uses local time for penalties
- `return_items()` - Uses local time for returns
- All database queries - Adjusted for local timezone

---

## ✅ Checklist

- [ ] Installed pytz (`pip install pytz`)
- [ ] Restarted server
- [ ] Checked server startup message (should say "Using timezone")
- [ ] Borrowed test item
- [ ] Verified borrow time is correct in Transactions tab
- [ ] Verified borrow time is correct in Reports tab
- [ ] Exported to Excel and checked times
- [ ] Times match Philippine Time (or your timezone)

---

## 💡 Pro Tip

**Server Timezone Setting:**

You can also check your server's timezone:
```bash
# On Linux/Mac:
date

# On Windows:
tzutil /g
```

But with pytz installed, the app will always use the configured timezone (Asia/Manila) regardless of server timezone!

---

**Your timezone is now fixed! All times will show correctly.** ⏰✅
