# src/preprocess.py
import re
from typing import List, Dict

def normalize_text(text: str) -> str:
    # basic normalization
    text = text.replace("\r\n", "\n").strip()
    text = re.sub(r"\s+\n", "\n", text)
    return text

def split_speakers(text: str) -> List[Dict]:
    """
    Returns list of dicts: [{'speaker': 'Physician', 'text': '...'}, ...]
    Works with common prefixes like 'Physician:' 'Doctor:' 'Patient:'
    """
    lines = [l.strip() for l in normalize_text(text).split("\n") if l.strip()]
    out = []
    current = None
    for line in lines:
        m = re.match(r'^(Physician|Doctor|Patient|Patient:|Physician:|Doctor:)\s*[:\-]?\s*(.*)$', line, re.I)
        if m:
            sp = m.group(1).capitalize()
            content = m.group(2).strip()
            out.append({'speaker': 'Physician' if 'doc' in sp.lower() or 'phys' in sp.lower() else 'Patient', 'text': content})
        else:
            # continuation of previous utterance
            if out:
                out[-1]['text'] += ' ' + line
            else:
                out.append({'speaker': 'Unknown', 'text': line})
    return out

if __name__ == "__main__":
    sample = open("data/sample_transcript.txt").read()
    print(split_speakers(sample))
