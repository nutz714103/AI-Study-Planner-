import re
from typing import List, Dict

def semantic_chunk (text: str, source_type: str = "pdf") -> List[Dict]:
    if source_type = "pptx":
        raw_chunks = text.split("\n\n")
    else:
        #split on heading-like pattern or double line breaks
      raw_chunks = re.split(r"\n(?=[A-Z][^\n]{0,80}\n)|\n{2,}", text)
      hunks = []
    for i, chunk in enumerate(raw_chunks):
        chunk = chunk.strip()
        if len(chunk) < 20:  # skip noise/empty fragments
            continue
        chunks.append({
            "chunk_id": i,
            "text": chunk,
            "char_len": len(chunk)
        })

    return chunks