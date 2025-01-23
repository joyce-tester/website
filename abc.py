import re

def extract_blocks(file_content):
    # Regular expression to match entire blocks starting with <per> and ending with </rty>
    pattern = r"(<per>.*?</rty>)"
    # Find all matches using re.DOTALL to include newlines
    blocks = re.findall(pattern, file_content, re.DOTALL)
    return blocks

# Example content
file_content = """
<hjjhhjfdf> <ghfhgs>
<per>fgfg</per>
<fggf>d</fggf>
<d>ggg</d>
<rty>fr</rty>
<per>fg</per>
<fggf>d</fggf>
<d>ggg</d>
<rty>fr</rty>
<per>ffg</per>
<fggf>d</fggf>
<d>ggg</d>
<rty>fr</rty>
<gfgfgfhh>gffgfg<gfg>
"""

# Extract blocks and print them
blocks = extract_blocks(file_content)
for i, block in enumerate(blocks, start=1):
    print(f"Block {i}:\n{block}\n")
