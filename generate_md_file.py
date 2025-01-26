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
        sections=[]
        if "[Tweet]" in section:
            sections = section.split("[Paper]")
            footer = sections.pop()
            sections += footer.split("[Tweet]")
            section = "| "+sections[0].replace("|", "").strip()+" | "+"[Paper]"+sections[1].replace("|", "").strip()+", "+"[Tweet]"+sections[2]+" |"
        else:
            sections = section.split("[Paper]")
            section = "| "+sections[0].replace("|", "").strip()+" | "+"[Paper]"+sections[1].replace("|", "").strip()+" |"



        output_file.write(section.strip()+"\n")
