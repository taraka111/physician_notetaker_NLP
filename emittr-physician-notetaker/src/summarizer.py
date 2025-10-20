from ner import extract_entities
from typing import List, Dict

def build_summary(transcript: str) -> Dict:
    """
    Convert transcript text into structured summary JSON.
    """
    entities = extract_entities(transcript)
    
    summary = {
        "Patient_Name": None,
        "Symptoms": [],
        "Diagnosis": None,
        "Treatment": [],
        "Current_Status": None,
        "Prognosis": None,
        "extraction_provenance": {}
    }

    # Extract Patient Name (from transcript)
    import re
    m = re.search(r'Ms\.?\s(\w+)|Patient:\s*(\w+)', transcript)
    if m:
        summary["Patient_Name"] = m.group(1) if m.group(1) else m.group(2)
    else:
        summary["Patient_Name"] = "Unknown"

    # Map entities
    for e in entities:
        if e["label"] == "SYMPTOM" and e["text"] not in summary["Symptoms"]:
            summary["Symptoms"].append(e["text"])
        elif e["label"] == "DIAGNOSIS":
            summary["Diagnosis"] = e["text"]
        elif e["label"] == "TREATMENT" and e["text"] not in summary["Treatment"]:
            summary["Treatment"].append(e["text"])
        elif e["label"] == "PROGNOSIS":
            summary["Prognosis"] = e["text"]
    
    # Current Status (last symptom-related line)
    import re
    current_status_match = re.findall(r'(occasional|current|now).+pain|discomfort', transcript, flags=re.I)
    if current_status_match:
        summary["Current_Status"] = " ".join(current_status_match)
    else:
        summary["Current_Status"] = "Not specified"

    # Extraction provenance
    summary["extraction_provenance"] = {
        "Symptoms": {"method": "entity_ruler", "confidence": 1.0},
        "Diagnosis": {"method": "entity_ruler", "confidence": 1.0},
        "Treatment": {"method": "entity_ruler", "confidence": 1.0},
        "Prognosis": {"method": "entity_ruler", "confidence": 1.0}
    }

    return summary

if __name__ == "__main__":
    transcript_file = "data/sample_transcript.txt"
    with open(transcript_file, "r") as f:
        transcript = f.read()
    summary = build_summary(transcript)
    import json
    with open("outputs/sample_output.json", "w") as out_f:
        json.dump(summary, out_f, indent=2)
    print(json.dumps(summary, indent=2))
