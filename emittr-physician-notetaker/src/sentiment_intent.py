from transformers import pipeline

def sentiment_intent_analysis(utterances):
    """
    utterances: list of dicts [{'speaker':..., 'text':...}]
    returns: list of dicts with sentiment and intent
    """
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    sentiment_labels = ["Anxious", "Neutral", "Reassured"]
    intent_labels = ["Seeking reassurance", "Reporting symptoms", "Expressing concern"]

    results = []
    for u in utterances:
        if u["speaker"] != "Patient":
            continue
        sentiment = classifier(u["text"], sentiment_labels)
        intent = classifier(u["text"], intent_labels)
        results.append({
            "utterance": u["text"],
            "Sentiment": sentiment["labels"][0],
            "Intent": intent["labels"][0],
            "confidence": max(sentiment["scores"][0], intent["scores"][0])
        })
    return results

if __name__ == "__main__":
    import json
    with open("data/sample_transcript.json", "r") as f:
        utterances = json.load(f)
    output = sentiment_intent_analysis(utterances)
    with open("outputs/sentiment_intent.json", "w") as f:
        json.dump(output, f, indent=2)
    print(json.dumps(output, indent=2))
