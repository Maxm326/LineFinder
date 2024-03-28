import os
import re

def write_matching_lines_to_file(directory_path, regex_pattern, output_file):
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return

    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                if filename.endswith(".jsp"):
                    fileContent = ""
                    file_path = os.path.join(root, filename)
                    matches_found = False
                    with open(file_path, 'r') as file:
                        line_number = 0
                        for line in file:
                            line_number += 1
                            match = re.search(regex_pattern, line)
                            if match:
                                matches_found = True
                                fileContent += f"Line {line_number}: {line.strip()}\n"
                    if matches_found:
                        outfile.write(f'\n###################### File: {filename} ###################### \n' + fileContent)

directory_path = '../TxEIS-Project/registration'
regex_pattern = r'\.(js|css)(?![p(])\b'
output_file = 'output.txt'
write_matching_lines_to_file(directory_path, regex_pattern, output_file)
