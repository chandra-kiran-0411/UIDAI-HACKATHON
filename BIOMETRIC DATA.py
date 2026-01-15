import csv
from collections import defaultdict

# 1. Ask for 5 file paths
print("--- UIDAI Accurate Data Aggregator ---")
file_paths = []
for i in range(4):
    path = input(f"Enter path for file {i+1}: ").strip().strip('"')
    file_paths.append(path)

# 2. Setup Variables
data_summary = defaultdict(lambda: {'5-17': 0, '>18': 0})
grand_5_17 = 0
grand_gt_18 = 0
total_rows_processed = 0  # <--- THE REAL COUNTER

print("\n🚀 Starting analysis. I will count every single row...")

for path in file_paths:
    if not path: continue
    print(f"Reading: {path}...")
    
    file_row_count = 0 # Counter for this specific file
    try:
        with open(path, mode='r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header
            
            for row in reader:
                if not row or len(row) < 6:
                    continue
                
                state = row[1].strip().upper()
                
                try:
                    c1 = int(row[4]) if row[4] else 0
                    c2 = int(row[5]) if row[5] else 0
                    
                    data_summary[state]['5-17'] += c1
                    data_summary[state]['>18'] += c2
                    
                    grand_5_17 += c1
                    grand_gt_18 += c2
                    
                    # Increment row counters
                    file_row_count += 1
                    total_rows_processed += 1
                    
                except ValueError:
                    continue

        print(f"✅ Finished {path}: Found {file_row_count:,} valid data rows.")

    except FileNotFoundError:
        print(f"❌ Error: Could not find {path}")

# 3. Final Results
print("\n" + "="*70)
print(f"{'STATE':<25} | {'AGE 5-17':<15} | {'AGE >18':<15}")
print("-" * 70)

for state, counts in sorted(data_summary.items()):
    print(f"{state[:25]:<25} | {counts['5-17']:<15,} | {counts['>18']:<15,}")

total_people = grand_5_17 + grand_gt_18
print("-" * 70)
print(f"{'GRAND TOTALS':<25} | {grand_5_17:<15,} | {grand_gt_18:<15,}")
print("="*70)
print(f"📊 ACTUAL ROWS ANALYZED: {total_rows_processed:,}")
print(f"✨ TOTAL PEOPLE APPLIED: {total_people:,}")
print("="*70)
