**Physician Notetaker – AI Medical NLP Assignment**

This project is developed as part of the Emittr AI Engineer Internship Assignment.
It focuses on building an AI-powered NLP pipeline for medical conversations — converting raw physician-patient dialogues into structured medical summaries, sentiment insights, and SOAP notes.


**Project Overview**

The goal of this project is to demonstrate understanding of Natural Language Processing (NLP) techniques, transformer-based AI models, and data structuring for healthcare text.

The pipeline performs the following tasks:

1. Entity Extraction (NER): Detects medical entities like symptoms, diagnosis, treatment, and prognosis.

2. Structured Summarization: Converts transcripts into a clean, machine-readable JSON summary.

3. Sentiment & Intent Analysis: Detects the patient’s emotional tone and intent (e.g., Anxious, Reassured, Seeking reassurance).

4. SOAP Note Generation (Bonus): Automatically generates a structured SOAP (Subjective, Objective, Assessment, Plan) medical note.


**Project Structure**
                          
### 📂 Project Files Overview

- **src/**
  
  - `ner.py` – Named Entity Recognition (NER) and keyword extraction  

  - `summarizer.py` – Builds structured medical summary JSON  

  - `sentiment_intent.py` – Sentiment and intent detection  

  - `soap_generator.py` – Converts transcript into SOAP note format  

- **data/sample_transcript.txt** – Sample conversation  

- **outputs/** – Contains generated JSON outputs  

- **notebooks/01_pipeline_demo.py** – Runs the end-to-end pipeline  

- **tests/test_pipeline.py** – (Optional) Simple unit test  

- **requirements.txt**, **README.md**


**Setup Instructions**

1. Clone or download the project

   -> git clone https://github.com/taraka111/physician_notetaker_NLP.git
   
   -> cd emittr-physician-notetaker

3. Create a virtual Environment
   
   -> python -m venv venv
   
   -> venv\Scripts\activate     # On Windows
   
   -> source venv/bin/activate  # On Mac/Linux

5. pip install -r requirements.txt

   If there is no requirements.txt, install the essentials manually:
   
   -> pip install spacy transformers torch nltk
   
   -> python -m spacy download en_core_web_sm


**Run the Pipeline**
  
  -> python notebooks/01_pipeline_demo.py

You will see outputs printed in the terminal:

---- Transcript ----

---- Extracted Entities ----

---- Structured Summary ----

---- Sentiment & Intent ----

---- SOAP Note ----

---- All outputs saved in 'outputs/' folder ----


All results are also saved automatically in the outputs/ folder as JSON files:

entities.json

sample_output.json

sentiment_intent.json

soap_note.json


**How it works**

| Component                                    | Description                                                                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **NER (ner.py)**                             | Uses spaCy rules and patterns to extract key medical terms such as symptoms, diagnosis, treatments, and prognosis. |
| **Summarizer (summarizer.py)**               | Combines extracted entities into a structured JSON summary resembling a medical report.                            |
| **Sentiment & Intent (sentiment_intent.py)** | Uses transformer-based models (DistilBERT / zero-shot classification) to detect patient sentiment and intent.      |
| **SOAP Generator (soap_generator.py)**       | Organizes text into Subjective, Objective, Assessment, and Plan format, commonly used by physicians.               |



  
   
