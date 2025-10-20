import spacy
from spacy.pipeline import EntityRuler
import re
from typing import List, Dict

def build_ruler(nlp):
    """
    Build EntityRuler with medical entity patterns.
    """
    ruler = EntityRuler(nlp, overwrite_ents=True)
    patterns = [
        # Symptoms
        {"label": "SYMPTOM", "pattern": [{"LOWER": "neck"}, {"LOWER": "pain"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "back"}, {"LOWER": "pain"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "head"}, {"LOWER": "impact"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "discomfort"}]},
        
        # Diagnosis
        {"label": "DIAGNOSIS", "pattern": [{"LOWER": "whiplash"}]},
        
        # Treatments
        {"label": "TREATMENT", "pattern": [{"LOWER": "physiotherapy"}]},
        {"label": "TREATMENT", "pattern": [{"LOWER": "painkillers"}]},
        {"label": "TREATMENT", "pattern": [{"TEXT": {"REGEX": r"\d+\s?sessions"}}]},
        
        # Prognosis
        {"label": "PROGNOSIS", "pattern": [{"LOWER": "full"}, {"LOWER": "recovery"}]},
        {"label": "PROGNOSIS", "pattern": [{"TEXT": {"REGEX": r"\d+\s?months"}}]},
        
        # Dates
        {"label": "DATE", "pattern": [{"TEXT": {"REGEX": r"(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}"}}]}
    ]
    ruler.add_patterns(patterns)
    return ruler

def extract_entities(text: str) -> List[Dict]:
    """
    Extract entities from text using spaCy with EntityRuler.
    Returns list of dicts: [{'text':..., 'label':..., 'confidence':...}]
    """
    nlp = spacy.load("en_core_web_sm")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    patterns = [
        # Symptoms
        {"label": "SYMPTOM", "pattern": [{"LOWER": "neck"}, {"LOWER": "pain"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "back"}, {"LOWER": "pain"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "head"}, {"LOWER": "impact"}]},
        {"label": "SYMPTOM", "pattern": [{"LOWER": "discomfort"}]},
        
        # Diagnosis
        {"label": "DIAGNOSIS", "pattern": [{"LOWER": "whiplash"}]},
        
        # Treatments
        {"label": "TREATMENT", "pattern": [{"LOWER": "physiotherapy"}]},
        {"label": "TREATMENT", "pattern": [{"LOWER": "painkillers"}]},
        {"label": "TREATMENT", "pattern": [{"TEXT": {"REGEX": r"\d+\s?sessions"}}]},
        
        # Prognosis
        {"label": "PROGNOSIS", "pattern": [{"LOWER": "full"}, {"LOWER": "recovery"}]},
        {"label": "PROGNOSIS", "pattern": [{"TEXT": {"REGEX": r"\d+\s?months"}}]},
        
        # Dates
        {"label": "DATE", "pattern": [{"TEXT": {"REGEX": r"(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}"}}]}
    ]
    ruler.add_patterns(patterns)
    ruler.overwrite_ents = True
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "confidence": 1.0,  # deterministic pattern match
            "method": "entity_ruler"
        })
    return entities

if __name__ == "__main__":
    sample_text = "I had whiplash and 10 physiotherapy sessions for neck pain."
    ents = extract_entities(sample_text)
    print(ents)
