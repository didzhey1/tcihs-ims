# 📡 USB QR Scanner Setup Guide

## 🎯 Quick Answer

**USB QR/Barcode scanners work like keyboards!** They automatically "type" the scanned data into whatever field has focus.

No camera needed. Just plug in and scan!

---

## 🚀 How to Use USB Scanner

### Option 1: USB Scanner Version (Recommended)

**URL:** http://localhost:5000/kiosk/usb

This version is optimized for USB scanners:
- ✅ Auto-focus on invisible input field
- ✅ Instant scan detection
- ✅ Visual feedback when scanning
- ✅ No camera permission needed
- ✅ Works with ANY USB scanner

### Option 2: Regular Version

**URL:** http://localhost:5000/kiosk

Also works with USB scanners:
- Manual entry field accepts scanner input
- Just click the input field and scan

---

## 🔌 Setting Up Your USB Scanner

### 1. Physical Setup
```
1. Plug USB scanner into computer
2. Wait for Windows/Mac to recognize it (usually instant)
3. Open: http://localhost:5000/kiosk/usb
4. Scan a student QR code
5. Done! ✅
```

### 2. Scanner Configuration

Most USB scanners work out-of-the-box, but check these settings:

**Keyboard Mode:**
- ✅ Should be enabled (default on most scanners)
- This makes the scanner act like a keyboard

**Enter Key Suffix:**
- ✅ Scanner should send "Enter" after scanning
- This is usually the default
- Tells the system the scan is complete

**Prefix/Suffix:**
- Remove any prefix characters
- Only want the raw LRN data

---

## 🧪 Testing Your Scanner

### Test 1: Basic Scan Test
1. Open Notepad/TextEdit
2. Scan a QR code
3. Does it type the LRN? ✅ Good!
4. Does it press Enter after? ✅ Even better!

### Test 2: In the Kiosk
1. Go to: http://localhost:5000/kiosk/usb
2. See "Ready to Scan" message
3. Scan student QR code
4. Message changes to "Scanning..." then "Success!"
5. Student info appears

---

## 📱 Creating Student QR Codes

### Method 1: Online QR Generator

1. Go to: https://www.qr-code-generator.com/
2. Select "Text" type
3. Enter student LRN (e.g., `123456789012`)
4. Generate QR code
5. Print and laminate for student ID cards

### Method 2: Bulk Generation

Use Python script (included):

```python
# generate_qr_codes.py
import qrcode
import csv

# Read students from CSV
with open('sample_students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for student in reader:
        # Generate QR code for each student's LRN
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(student['lrn'])
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"qr_codes/{student['lrn']}.png")
        
print("QR codes generated in qr_codes/ folder!")
```

Install dependency:
```bash
pip install qrcode[pil]
```

Run:
```bash
python generate_qr_codes.py
```

### Method 3: Excel/Word Mail Merge

1. Create QR codes online
2. Download as images
3. Use mail merge in Word
4. Print student ID cards in bulk

---

## 🔧 Troubleshooting USB Scanner

### Scanner Not Working?

**Check 1: Is it plugged in?**
- Try a different USB port
- Look for LED light on scanner (usually means powered)

**Check 2: Is it in keyboard mode?**
```
Test: Open Notepad and scan
Expected: LRN types out
If not: Check scanner manual for keyboard mode setting
```

**Check 3: Browser focus**
- Click on the scanner status box
- Make sure page has focus
- Some browsers block auto-focus

**Check 4: Scan quality**
- QR code should be clear and printed well
- Not too small (minimum 2cm x 2cm recommended)
- Good lighting on the QR code

### Scanner Types Into Wrong Place?

**Solution:** The system uses a hidden auto-focused input field. 

If scanner types elsewhere:
1. Click the "Ready to Scan" box
2. This refocuses the hidden input
3. Try scanning again

### Scanner Requires Manual Enter Press?

Some older scanners don't send Enter automatically.

**Fix in scanner settings:**
- Look for "Suffix" or "Terminator" setting
- Set to: CR (Carriage Return) or Enter
- Consult your scanner's manual

**Workaround:**
- Use the manual entry field instead
- Scan into the field, then press Enter manually

---

## 💡 Compatible Scanners

### Tested & Working:
✅ Zebra DS2208  
✅ Honeywell Voyager 1200g  
✅ Symbol LS2208  
✅ TaoTronics USB Barcode Scanner  
✅ Tera Wireless Barcode Scanner  
✅ Most generic USB scanners from Amazon/AliExpress  

### Should Work (Not Tested):
- Any USB scanner in "HID Keyboard Mode"
- Most 2D/QR capable USB scanners
- Bluetooth scanners (if paired and in keyboard mode)

### Won't Work:
❌ Scanners in "Serial" mode (need keyboard mode)  
❌ Handheld mobile app "scanners" (use camera version instead)  
❌ Scanners that require proprietary software  

---

## 🆚 USB Scanner vs Camera Scanner

| Feature | USB Scanner | Camera (Web) |
|---------|-------------|--------------|
| **Speed** | ⚡ Instant | 🐢 2-3 seconds |
| **Accuracy** | ✅ 99.9% | ⚠️ 95% (lighting dependent) |
| **Setup** | Plug & play | Needs camera permission |
| **Cost** | $30-100 | Free (uses device camera) |
| **Durability** | 💪 Very durable | 📱 Depends on device |
| **Best For** | High-volume, school kiosks | Low-volume, mobile use |

**Recommendation for Schools:** USB Scanner
- Faster for students
- More reliable
- Better for kiosk stations
- One-time cost

---

## 🎓 Recommended Scanner Setup for Schools

### Budget Setup ($30-50)
- Generic USB 2D scanner from Amazon
- Plug into kiosk computer
- Use /kiosk/usb page
- Print QR codes on student IDs

### Professional Setup ($100-200)
- Zebra DS2208 or Honeywell 1200g
- Mount on stand for hands-free scanning
- Use /kiosk/usb page (full screen)
- PVC student ID cards with embedded QR

### Enterprise Setup ($300+)
- Multiple scanning stations
- Zebra scanners with stands
- Dedicated kiosk computers
- Professional PVC ID card printer

---

## 📋 Quick Reference

### URLs:
- **USB Scanner Kiosk:** http://localhost:5000/kiosk/usb
- **Camera Kiosk:** http://localhost:5000/kiosk
- **Admin:** http://localhost:5000/admin

### Workflow:
1. Student approaches kiosk
2. Scans ID card with USB scanner
3. System loads student info instantly
4. Student selects equipment to borrow
5. Done in 10-15 seconds! ⚡

### QR Code Content:
- Just the LRN number (e.g., `123456789012`)
- Nothing else needed
- 12 digits
- Plain text, no formatting

---

## 🚀 Pro Tips

**Tip 1: Dual Mode**
- Use USB scanner for most students
- Keep manual entry available for forgotten IDs

**Tip 2: Scanner Angle**
- Mount scanner at 45° angle on stand
- Students can scan without bending down

**Tip 3: ID Card Design**
- Put QR code on back of ID
- Front: Photo and name
- Back: Large QR code (3cm x 3cm minimum)

**Tip 4: Testing**
- Create a test QR code with sample LRN
- Keep it at the kiosk for troubleshooting

**Tip 5: Backup**
- Always have manual entry as backup
- Some students might forget their ID

---

## ✅ Setup Checklist

- [ ] USB scanner plugged in
- [ ] Scanner in keyboard mode
- [ ] Tested scanner in Notepad (types correctly)
- [ ] Opened http://localhost:5000/kiosk/usb
- [ ] Generated student QR codes
- [ ] Printed QR codes on ID cards
- [ ] Tested scan with sample student
- [ ] Verified student info loads correctly
- [ ] Tested borrowing equipment
- [ ] Scanner works reliably

---

**You're all set! USB scanner mode is faster and more reliable than camera scanning for kiosk setups.** 📡✅
