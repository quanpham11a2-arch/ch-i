import os
import csv
import re
from datetime import datetime
from urllib.parse import urlparse
import time

def extract_emails(text):
    # regex tìm email
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def process_csv(input_file, output_file):
    results = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        for row in reader:
            row_text = " ".join(row)
            emails = extract_emails(row_text)
            
            for email in emails:
                results.append([email])

    # ghi ra file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["email"])
        writer.writerows(results)

def main():
    input_file = "input.csv"
    output_file = "output_emails.csv"

    print("Loading student roster...")
    time.sleep(1)

    process_csv(input_file, output_file)

    print("Done! Emails extracted.")

if __name__ == "__main__":
    main()
