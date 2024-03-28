import re
import sys

file_path = sys.argv

def print_matching_lines(file_path, regex_pattern):
    with open(file_path, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
            match = re.search(regex_pattern, line)
            if match:
                print(f"Line {line_number}: {line.strip()}")

file_path = '../TxEIS-Project/registration/WebRoot/report/viewReportDialog.jsp'  # Replace with your file path
regex_pattern = r'\.(js|css)(?![p])\b'  # Replace with your regex pattern
print_matching_lines(file_path, regex_pattern)
