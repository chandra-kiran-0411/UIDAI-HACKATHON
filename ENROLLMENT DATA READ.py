import csv
from collections import defaultdict

# 1. Ask for file paths
file_paths = []
for i in range(3):
    path = input(f"Enter path for file {i+1}: ").strip().strip('"')
    file_paths.append(path)

data_summary = defaultdict(lambda: {'0-5': 0, '5-17': 0, '>18': 0})
grand_0_5 = grand_5_17 = grand_gt_18 = 0

print("\n🚀 Crunching numbers (Corrected for Pincode column)...")

for path in file_paths:
    print(f"Reading: {path}...")
    try:
        with open(path, mode='r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            header = next(reader) 
            
            for i, row in enumerate(reader):
                if not row or len(row) < 7: # We now need at least 7 columns (A to G)
                    continue
                
                state = row[1].strip().upper()
                
                try:
                    # UPDATED INDEXES BASED ON YOUR IMAGE:
                    # E=4, F=5, G=6
                    c1 = int(row[4]) if row[4] else 0
                    c2 = int(row[5]) if row[5] else 0
                    c3 = int(row[6]) if row[6] else 0
                    
                    data_summary[state]['0-5'] += c1
                    data_summary[state]['5-17'] += c2
                    data_summary[state]['>18'] += c3
                    
                    grand_0_5 += c1
                    grand_5_17 += c2
                    grand_gt_18 += c3
                    
                except ValueError:
                    continue

                if i % 2000000 == 0 and i > 0:
                    print(f"   Processed {i} rows...")

    except FileNotFoundError:
        print(f"❌ Error: File not found at {path}")

# 3. Final Printout
print("\n" + "="*70)
print(f"{'STATE':<25} | {'AGE 0-5':<10} | {'AGE 5-17':<10} | {'AGE >18':<10}")
print("-" * 70)

for state, counts in sorted(data_summary.items()):
    print(f"{state[:25]:<25} | {counts['0-5']:<10,} | {counts['5-17']:<10,} | {counts['>18']:<10,}")

print("-" * 70)
print(f"{'GRAND TOTALS':<25} | {grand_0_5:<10,} | {grand_5_17:<10,} | {grand_gt_18:<10,}")
print("="*70)
print(f"✨ TOTAL PEOPLE APPLIED: {grand_0_5 + grand_5_17 + grand_gt_18:,}")
print("="*70)
