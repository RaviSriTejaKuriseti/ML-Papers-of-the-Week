import re

SPLITTERS=["[Paper]","[Paper 1]","[Paper 2]", "[Tweet]","[GitHub]","[Code]","[Code & Data]","[App]","[Dataset]","[Models]","[System Card]","[Blog]","[Demo]","[Technical Report]"]

# Read the content from the input file
with open("1.md", "r") as file:
    content = "\n"+file.read()

content = content.replace("**", "")
content = content.replace("<u>", "")
content = content.replace("</u>", "")
content = content.replace("●","<br>●")
content = content.replace("> ", "")

# Use a regex to split only at valid section headers
# This ensures we split on patterns like "1) Section text" at the start of a line
sections = re.split(r'(\n\d+\.\s+)', content.replace("\\",""))

# Combine the headers with their corresponding content
final_sections = []
for i in range(1, len(sections), 2):
    header = sections[i].strip()
    body = sections[i + 1].strip() if i + 1 < len(sections) else ""
    final_sections.append(f"{header} {body}")

print(len(final_sections))

with open("output2.md", "w") as output_file:
    for idx, section in enumerate(final_sections):
        section = section.replace("\n", " ")
        splitters=SPLITTERS
        pattern = "(" + "|".join(map(re.escape, splitters)) + ")"
        result=re.split(pattern,section)
        sections=result[::2]
        splits=result[1::2]
        section="| "+sections[0].replace("|", "").strip()+" | "
        for i,e in enumerate(splits):
            section+=e+sections[i+1].replace("|","").strip()+", "
        section = re.sub(r'^(\|\s*)(\d+)\.', r'\1\2)', section.rstrip(", "))
        section=section+" |"
        output_file.write(section.strip()+"\n")
