import sys
import os
import json

# Step 1: Path setup
# Get absolute path to src/ and add to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "../src")
DATA_DIR = os.path.join(BASE_DIR, "../data")
OUTPUT_DIR = os.path.join(BASE_DIR, "../outputs")

sys.path.append(SRC_DIR)

# Import project modules
from ner import extract_entities
from summarizer import build_summary
from sentiment_intent import sentiment_intent_analysis
from soap_generator import generate_soap

# Ensure output/data folders exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Step 2: Load Transcript
transcript_file = os.path.join(DATA_DIR, "sample_transcript.txt")
with open(transcript_file, "r") as f:
    transcript = f.read()

print("---- Transcript ----")
print(transcript[:500], "...")  # Display first 500 chars

# Step 3: Extract Entities (NER)
entities = extract_entities(transcript)
print("\n---- Extracted Entities ----")
for e in entities:
    print(e)

# Save entities JSON
with open(os.path.join(OUTPUT_DIR, "entities.json"), "w") as f:
    json.dump(entities, f, indent=2)

# Step 4: Structured Summary
summary = build_summary(transcript)
print("\n---- Structured Summary ----")
print(json.dumps(summary, indent=2))

# Save summary JSON
with open(os.path.join(OUTPUT_DIR, "sample_output.json"), "w") as f:
    json.dump(summary, f, indent=2)

# Step 5: Preprocess Transcript
utterances = []
for line in transcript.split("\n"):
    line = line.strip()
    if line.startswith("Physician:") or line.startswith("Doctor:"):
        speaker = "Physician"
        text = line.split(":", 1)[1].strip()
    elif line.startswith("Patient:"):
        speaker = "Patient"
        text = line.split(":", 1)[1].strip()
    else:
        continue
    if text:
        utterances.append({"speaker": speaker, "text": text})

# Save utterances JSON
with open(os.path.join(DATA_DIR, "sample_transcript.json"), "w") as f:
    json.dump(utterances, f, indent=2)

# Step 6: Sentiment & Intent
sentiment_intent = sentiment_intent_analysis(utterances)
print("\n---- Sentiment & Intent ----")
for s in sentiment_intent:
    print(s)

# Save sentiment JSON
with open(os.path.join(OUTPUT_DIR, "sentiment_intent.json"), "w") as f:
    json.dump(sentiment_intent, f, indent=2)

# Step 7: SOAP Note
soap_note = generate_soap(utterances)
print("\n---- SOAP Note ----")
print(json.dumps(soap_note, indent=2))

# Save SOAP note JSON
with open(os.path.join(OUTPUT_DIR, "soap_note.json"), "w") as f:
    json.dump(soap_note, f, indent=2)

print("\n---- ✅ All outputs saved in 'outputs/' folder ----")
