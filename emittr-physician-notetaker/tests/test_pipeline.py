import json

def test_summary_keys():
    summary = json.load(open("outputs/sample_output.json"))
    keys = ["Patient_Name","Symptoms","Diagnosis","Treatment","Current_Status","Prognosis","extraction_provenance"]
    assert all(k in summary for k in keys)
