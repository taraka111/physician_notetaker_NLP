def classify_sentence(sentence, speaker):
    sentence = sentence.lower()
    if speaker == "Patient":
        return "S"  # Subjective
    elif "range of motion" in sentence or "physical" in sentence:
        return "O"  # Objective
    elif "whiplash" in sentence or "diagnos" in sentence:
        return "A"  # Assessment
    elif "follow up" in sentence or "treatment" in sentence or "return" in sentence:
        return "P"  # Plan
    else:
        return "S"

def generate_soap(utterances):
    sections = {"S": [], "O": [], "A": [], "P": []}
    for u in utterances:
        tag = classify_sentence(u['text'], u['speaker'])
        sections[tag].append(u['text'])
    soap_note = {
        "Subjective": {"Notes": sections["S"]},
        "Objective": {"Notes": sections["O"]},
        "Assessment": {"Notes": sections["A"]},
        "Plan": {"Notes": sections["P"]}
    }
    return soap_note
