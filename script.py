import os
import re
import socket
from collections import Counter

# Define file paths
output_dir = "/home/data/output"
output_file = f"{output_dir}/result.txt"
input_files = ["/home/data/IF-1.txt", "/home/data/AlwaysRememberUsThisWay-1.txt"]

# Ensure output directory exists
try:
    os.makedirs(output_dir, exist_ok=True)
except Exception as e:
    print(f"Error creating directory: {e}")

def process_text(file_path):
    """Reads a file and returns word count and top 3 words."""
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found.")
        return 0, []
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    
    # Handle contractions by splitting words properly
    text = re.sub(r"'", "", text)
    words = re.findall(r"\b\w+\b", text)
    
    word_count = len(words)
    top_words = Counter(words).most_common(3)
    
    return word_count, top_words

# Process both files
results = {}
grand_total = 0
for file in input_files:
    count, top_words = process_text(file)
    results[file] = {"word_count": count, "top_words": top_words}
    grand_total += count

# Get IP address of the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
try:
    with open(output_file, "w", encoding="utf-8") as f:
        for file, data in results.items():
            f.write(f"File: {file}\n")
            f.write(f"Word Count: {data['word_count']}\n")
            f.write(f"Top 3 Words: {data['top_words']}\n\n")
        f.write(f"Grand Total Word Count: {grand_total}\n")
        f.write(f"Container IP Address: {ip_address}\n")
    print("Results written to result.txt successfully.")
except Exception as e:
    print(f"Error writing to file: {e}")

# Ensure result.txt is created before reading
if os.path.exists(output_file):
    with open(output_file, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Error: result.txt was not created.")


import time

print("Processing complete. Keeping container alive...")

while True:
    time.sleep(60)  