import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
print("Select the folder with your .txt files:")
folder = askdirectory()

if not folder:
    print("No folder selected, exiting")
    exit()

files = [f for f in os.listdir(folder) if f.endswith(".txt") and f != "Report.txt"]

if not files:
    print("No text files found here.")
    exit()

word_counts = {}
total_words = 0

for f in files:
    try:
        with open(os.path.join(folder, f), "r", encoding="utf-8") as file:
            text = file.read()
            count = len(text.split())
            word_counts[f] = count
            total_words += count
    except:
        print(f"Couldn't read {f}, skipping.")

report_file = os.path.join(folder, "Report.txt")
with open(report_file, "w", encoding="utf-8") as report:
    report.write("Word Count Report\n")
    report.write("~~~~~~~~~~~~~~~~~~\n\n")
    for f, c in word_counts.items():
        report.write(f"{f}: {c} words\n")
    report.write(f"\nTotal words in all files: {total_words}\n")

print(f"Report saved as {report_file}.")

try:
    if os.name == 'nt':
        os.startfile(report_file)
except Exception as e:
    print("Couldn't open the report automatically. Open it manually.")
