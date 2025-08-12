import json
from typing import List, Dict
from records_extraction import Records_Extraction_Funcs



def get_records(first_name: str, last_name: str, from_date: str, thru_date: str,
                ) -> List[Dict]:
    record_nums = Records_Extraction_Funcs.get_record_number(first_name, last_name, from_date, thru_date)
    # keep each instrument once
    seen = set()
    records = []
    for raw_record in record_nums:
        gin = raw_record.get("gin")
        if not gin or gin in seen:
            continue
        seen.add(gin)
        details = Records_Extraction_Funcs.get_record_details(gin)
        records.append(Records_Extraction_Funcs.record_finalized(details))
    return records


def runner():
    # Greta
    greta = get_records("greta", "smith", "01/10/2023", "01/06/2024")
    print(json.dumps(greta, indent=2, ensure_ascii=False))

    # Kelly - has multiple records under her name
    # kelly = get_records("kelly", "smith", "01/10/2023", "01/06/2024")
    # print(json.dumps(kelly, indent=2, ensure_ascii=False))

    # Only a last name
    # smith = get_records("", "smith", "01/16/2023", "01/19/2023")
    # print(json.dumps(smith, indent=2, ensure_ascii=False))

    # Greta - but with an open finish date
    # greta = get_records("greta", "smith", "01/10/2023", "")
    # print(json.dumps(greta, indent=2, ensure_ascii=False))

    # Greta - but with an open start date
    # greta = get_records("greta", "smith", "", "01/06/2024")
    # print(json.dumps(greta, indent=2, ensure_ascii=False))

    # One that'll come up empty
    # greta = get_records("jibrish", "nonsense", "01/10/2023", "01/06/2024")
    # print(json.dumps(greta, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    runner()
