import re 
from typing import Dict, List
#normalize whitespace definition
def normalize_whitespace (text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

#boiler plate removal definition
def remove_boilerplate(text:str) -> str:
    text = re.sub(r"Page \d+ of \d+", "", text, flags= re.IGNORECASE)
    text = re.sub(r"^\s*[•▪●○]\s*", "- ", text, flags= re.MULTILINE)
    text = re.sub(r"x0c", "", text) #form feed characters from PDFs
    return text

def arrange_into_sections(text:str) -> List[Dict]:
    raw_blocks = re.split(r"\n{2,}", text)
    sections:List[Dict] = []

    for i, block in enumerate (raw_blocks):
        block = block.strip()
        if len(block) < 10:
            continue
        sections.append({
            "section_id": i,
            "text" : block
        })
    return sections

def clean_arrange(extracted :Dict) -> Dict:
    cleaned = normalize_whitespace(extracted["raw_text"])
    cleaned = remove_boilerplate(cleaned)
    sections = arrange_into_sections(removed)
    return {
        "source_type" : extracted["source_type"],
        "cleaned_text" :cleaned,
        "sections" : sections
    }
