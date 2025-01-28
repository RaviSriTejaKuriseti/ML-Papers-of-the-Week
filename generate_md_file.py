import re

# Read the content from the input file
with open("input.md", "r") as file:
    content = file.read()

# Use a regex to split only at valid section headers
# This ensures we split on patterns like "1) Section text" at the start of a line
sections = re.split(r'(\n\d+\)\s+)', content)

# Combine the headers with their corresponding content
final_sections = []
for i in range(1, len(sections), 2):
    header = sections[i].strip()
    body = sections[i + 1].strip() if i + 1 < len(sections) else ""
    final_sections.append(f"{header} {body}")

# print(len(final_sections))

with open("output.md", "w") as output_file:
    for idx, section in enumerate(final_sections):
        section = section.replace("\n", " ")
        splitters=["[Paper]", "[Tweet]","[GitHub]","[Code]","[App]","[Dataset]"]
        pattern = "(" + "|".join(map(re.escape, splitters)) + ")"
        result=re.split(pattern,section)
        sections=result[::2]
        splits=result[1::2]
        section="| "+sections[0].replace("|", "").strip()+" | "
        for i,e in enumerate(splits):
            section+=e+sections[i+1].replace("|","").strip()+", "
        section=section.rstrip(", ")+" |"
        output_file.write(section.strip()+"\n")
