def filter_lines(input_file, output_file, term="Fall 2025"):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("""
| Company | Role | Location | Terms | Application/Link | Date Posted |
| ------- | ---- | -------- | ----- | ---------------- | ----------- |\n""")
        for line in infile:
            if line.find(term) != -1:
                outfile.write(line)

if __name__ == "__main__":
    input_file = 'README-Off-Season.md'  # Replace with your input file path
    output_file = 'filtered.md'  # Replace with your output file path
    filter_lines(input_file, output_file)