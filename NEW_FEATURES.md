# 🆕 New Features Guide

## What's New:

### 1. 📊 Reports Tab with Export
### 2. ⏰ Borrow Time Display
### 3. 📥 Export to Excel/PDF
### 4. 🚫 One Item Per Student Limit

---

## 1. 📊 Reports Tab

**Location:** Admin Dashboard → Reports Tab

### Features:
- **Complete Transaction History** - All borrowing/return records
- **Detailed Information** - ID, borrow date & time, student info, equipment details
- **Filter & Search** - Find specific transactions easily
- **Transaction Count** - See total at bottom of page

### How to Access:
1. Login to admin dashboard
2. Click "📊 Reports" tab
3. View all transactions with full details

---

## 2. ⏰ Borrow Time Display

**Now shows:** Date AND Time of borrowing

### Where You'll See It:
- **Transactions Tab** - Shows borrow date + time separately
- **Reports Tab** - Shows borrow date + time in separate columns
- **Excel Export** - Separate columns for date and time
- **PDF Export** - Includes borrow time

### Format:
- **Date:** YYYY-MM-DD (e.g., 2026-02-15)
- **Time:** HH:MM AM/PM (e.g., 10:30 AM)

### Why It's Useful:
- Track peak borrowing hours
- Identify busy times of day
- Better audit trail
- Precise transaction records

---

## 3. 📥 Export to Excel/PDF

**Location:** Admin Dashboard → Reports Tab → Export Buttons

### Excel Export (.xlsx)

**Features:**
- ✅ **Complete Data** - ALL transactions included
- ✅ **Formatted Headers** - Blue background, white text
- ✅ **14 Columns** - Transaction ID, dates, times, student info, equipment details
- ✅ **Auto-sized Columns** - Easy to read
- ✅ **Alternating Row Colors** - Better readability

**Columns Included:**
1. Transaction ID
2. Borrow Date
3. Borrow Time
4. Due Date
5. Return Date
6. Status
7. Cooldown Days
8. Student Name
9. LRN
10. Grade
11. Section
12. Equipment
13. Asset Tag
14. Category

**How to Export:**
```
1. Admin → Reports tab
2. Click "📊 Export to Excel"
3. File downloads automatically
4. Open in Excel, Google Sheets, or LibreOffice
```

**File Name Format:** `transaction_history_YYYYMMDD_HHMMSS.xlsx`

### PDF Export (.pdf)

**Features:**
- ✅ **Print-Friendly** - Landscape format
- ✅ **First 100 Transactions** - Most recent (keeps file size manageable)
- ✅ **Report Header** - Title and generation date
- ✅ **Professional Table** - Formatted with alternating row colors
- ✅ **Transaction Count** - Shows total in report

**Perfect For:**
- Printing monthly reports
- Official documentation
- School records
- Quick overviews

**How to Export:**
```
1. Admin → Reports tab
2. Click "📄 Export to PDF"
3. File downloads automatically
4. Open in any PDF reader
```

**File Name Format:** `transaction_history_YYYYMMDD_HHMMSS.pdf`

### Installation:

First time setup - install export libraries:
```bash
pip install openpyxl reportlab
```

Or install all at once:
```bash
pip install -r requirements.txt
```

---

## 4. 🚫 One Item Per Student Limit

**New Rule:** Students can only borrow **ONE item at a time**

### How It Works:

**Scenario 1: Trying to Borrow Multiple Items**
```
Student selects 2 items in modal
→ Alert: "You can only borrow ONE item at a time"
→ Selection blocked
```

**Scenario 2: Already Has Borrowed Item**
```
Student tries to borrow when they have an item out
→ Message: "You already have an item borrowed"
→ Must return current item first
```

**Scenario 3: Successful Borrow**
```
Student has nothing borrowed
→ Selects 1 item
→ Borrows successfully ✅
```

### User Interface Changes:

**Kiosk - Borrow Tab:**
- ⚠️ Warning message at top: "You can only borrow ONE item at a time"
- Selection limited to 1 item in modal
- Button text changed to "Borrow Item" (not "Items")
- Alert if trying to select more than one

**Modal Selection:**
- Clicking second checkbox shows alert
- Must deselect first item before selecting another
- Clear feedback to user

### Why This Limit?

**Benefits:**
1. **Simpler Tracking** - Easier to manage returns
2. **Fair Access** - More students can borrow equipment
3. **Reduced Loss** - Students more careful with single items
4. **Faster Returns** - Less complexity in return process
5. **Better Responsibility** - Focus on one item at a time

### Workflow:

**Student wants 2 calculators:**
```
1. Borrow Calculator #1
2. Return Calculator #1
3. Borrow Calculator #2
```

**Multiple students need equipment:**
```
Before: Juan borrows 3 basketballs
After: Juan, Maria, and Carlos each borrow 1 basketball
Result: More fair distribution ✅
```

---

## 📊 Sample Excel Export Structure

```
+--------+-------------+------------+----------+--------+----------+
| Trans  | Borrow      | Borrow     | Status   | Student| Equipment|
| ID     | Date        | Time       |          | Name   |          |
+--------+-------------+------------+----------+--------+----------+
| 1      | 2026-02-15  | 10:30 AM   | returned | Juan   | Laptop #1|
| 2      | 2026-02-15  | 11:15 AM   | borrowed | Maria  | Ball #5  |
| 3      | 2026-02-15  | 02:45 PM   | overdue  | Pedro  | Proj #2  |
+--------+-------------+------------+----------+--------+----------+
```

---

## 🎯 Quick Start Guide

### Setup Export Features:
```bash
# Install libraries
pip install openpyxl reportlab

# Restart server
python app.py

# Test exports
1. Login to admin
2. Go to Reports tab
3. Click export buttons
```

### Test One-Item Limit:
```bash
# At kiosk
1. Scan student ID
2. Try to select multiple items
3. See alert preventing it
4. Select only 1 item
5. Borrow successfully
```

---

## 💡 Pro Tips

**Tip 1: Regular Exports**
- Export weekly to Excel for backup
- Keep monthly PDF reports for records

**Tip 2: Excel Analysis**
- Use Excel pivot tables for statistics
- Filter by date ranges
- Analyze busy times

**Tip 3: One-Item Workflow**
- Explain limit to students clearly
- Post signs at kiosk
- Train staff on new process

**Tip 4: Batch Returns**
- Have students return quickly
- Shorter transaction times
- Higher equipment availability

---

## ✅ Feature Checklist

- [ ] Installed openpyxl and reportlab
- [ ] Tested Excel export (opens correctly)
- [ ] Tested PDF export (displays correctly)
- [ ] Reports tab shows borrow time
- [ ] One-item limit works in kiosk
- [ ] Alert shows when trying multiple items
- [ ] Can't borrow if already have item out
- [ ] Return required before new borrow

---

## 🐛 Troubleshooting

### "Module not found: openpyxl"
```bash
pip install openpyxl reportlab
```

### "Excel file won't open"
- Make sure you have Excel, LibreOffice, or Google Sheets
- File might be blocked by antivirus - unblock it
- Try opening with Google Sheets online

### "One-item limit not working"
- Clear browser cache
- Refresh kiosk page (F5)
- Check browser console for errors (F12)

### "Export button does nothing"
- Check browser download settings
- Allow popups from localhost
- Check downloads folder

---

**All features are now active! 🎉**

Your system now has:
- ✅ Professional export capabilities
- ✅ Detailed time tracking
- ✅ Fair one-item-per-student policy
- ✅ Complete audit trail
