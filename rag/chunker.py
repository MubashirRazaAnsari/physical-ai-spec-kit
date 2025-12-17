import re
from pathlib import Path

MIN_CHARS = 800   # ~200 tokens
MAX_CHARS = 2400  # ~600 tokens

def chunk_markdown(md_text, source_file):
    sections = re.split(r'\n## ', md_text)
    chunks = []

    for idx, sec in enumerate(sections):
        if idx == 0:
            continue

        header, *body = sec.split('\n', 1)
        content = body[0].strip() if body else ""

        if len(content) < MIN_CHARS:
            continue

        while len(content) > MAX_CHARS:
            split = content[:MAX_CHARS].rsplit('.', 1)[0]
            chunks.append(make_chunk(split, source_file, header, idx))
            content = content[len(split):]

        chunks.append(make_chunk(content, source_file, header, idx))

    return chunks


def make_chunk(text, source, header, idx):
    return {
        "text": text.strip(),
        "metadata": {
            "source_file": source,
            "section_title": header.strip(),
            "chunk_index": idx,
            "doc_type": "book_section"
        }
    }
