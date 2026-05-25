"""
QR Code Generator for Student IDs
==================================
This script generates QR codes for all students in your CSV file.

Usage:
1. pip install qrcode[pil]
2. python generate_qr_codes.py
3. QR codes saved to qr_codes/ folder
"""

import qrcode
import csv
import os

def generate_qr_codes_from_csv(csv_file='sample_students.csv', output_dir='qr_codes'):
    """
    Generate QR codes for all students in a CSV file.
    
    Args:
        csv_file: Path to CSV file with student data
        output_dir: Directory to save QR code images
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✓ Created directory: {output_dir}/")
    
    # Read students from CSV
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            students = list(reader)
    except FileNotFoundError:
        print(f"❌ Error: {csv_file} not found!")
        print("Make sure the CSV file is in the same directory as this script.")
        return
    
    if not students:
        print("❌ No students found in CSV file!")
        return
    
    print(f"\n📋 Found {len(students)} students in {csv_file}")
    print("Generating QR codes...\n")
    
    generated = 0
    
    for student in students:
        lrn = student.get('lrn', '')
        first_name = student.get('first_name', 'Unknown')
        last_name = student.get('last_name', 'Unknown')
        
        if not lrn:
            print(f"⚠️  Skipping student with no LRN: {first_name} {last_name}")
            continue
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,  # Size of QR code (1-40, 1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size
        )
        
        # Add LRN data to QR code
        qr.add_data(lrn)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save with filename: LRN_FirstName_LastName.png
        filename = f"{lrn}_{first_name}_{last_name}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        
        print(f"✓ {filename}")
        generated += 1
    
    print(f"\n🎉 Successfully generated {generated} QR codes!")
    print(f"📁 Saved to: {os.path.abspath(output_dir)}/")
    print("\nNext steps:")
    print("1. Print the QR codes")
    print("2. Attach to student ID cards (recommend 3cm x 3cm minimum size)")
    print("3. Laminate for durability")
    print("4. Test scanning with USB scanner")


def generate_single_qr(lrn, output_file='test_qr.png'):
    """
    Generate a single QR code for testing.
    
    Args:
        lrn: Student LRN number
        output_file: Filename to save QR code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(lrn)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    
    print(f"✓ Generated QR code: {output_file}")
    print(f"  LRN: {lrn}")


if __name__ == '__main__':
    print("="*60)
    print("QR CODE GENERATOR FOR STUDENT IDS")
    print("="*60)
    
    # Check if qrcode library is installed
    try:
        import PIL
    except ImportError:
        print("\n❌ Error: Required library not installed!")
        print("\nPlease run:")
        print("  pip install qrcode[pil]")
        print("\nThen run this script again.")
        exit(1)
    
    print("\nOptions:")
    print("1. Generate QR codes from sample_students.csv")
    print("2. Generate QR codes from custom CSV file")
    print("3. Generate single test QR code")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '1':
        generate_qr_codes_from_csv()
    
    elif choice == '2':
        csv_file = input("Enter CSV filename: ").strip()
        output_dir = input("Enter output directory (default: qr_codes): ").strip() or 'qr_codes'
        generate_qr_codes_from_csv(csv_file, output_dir)
    
    elif choice == '3':
        lrn = input("Enter LRN number: ").strip()
        output_file = input("Enter output filename (default: test_qr.png): ").strip() or 'test_qr.png'
        generate_single_qr(lrn, output_file)
    
    else:
        print("Invalid choice!")
