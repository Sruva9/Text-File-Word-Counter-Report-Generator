# Word Count Report Generator

## Project Title
Word Count Report Generator

## Objective
This project scans a folder for `.txt` files, counts the total words in each file, and generates a summary report called `report.txt` listing each file and its word count. It also automatically opens the report for easy viewing.

## Tech Stack
- Python 3.x
- Tkinter (for folder selection)
- Standard Python libraries (`os`, `sys`)

## Features
- Select a folder containing `.txt` files via a simple GUI dialog.
- Counts words in all text files except `report.txt`.
- Generates a nicely formatted summary report with total words.
- Automatically opens the generated report.
- Simple, human-readable script for easy modification.

## How to Run
1. Make sure Python 3 is installed on your system.
2. Download or clone the project folder.
3. Run the script in a terminal or Python IDE:
4. A folder selection dialog will appear—choose the folder with your .txt files.
5. After processing, the report will be saved as report.txt in the same folder and opened automatically.

```bash
python word_count.py
