import json
from typing import List, Dict
from typing import Union
from helper_functions import Helper_Functions

class Records_Extraction_Funcs:
    def get_record_number(first_name: str, last_name: str, from_date: str, thru_date: str) -> List[Dict]:
        full_name = f"{last_name}, {first_name}"
        criteria = [{
            "full_name": full_name,
            "file_date_start": from_date,
            "file_date_end": thru_date,
        }]
        params = {"criteria_array": json.dumps(criteria)}
        try:
            data = Helper_Functions.API_call(url_suffix="CriteriaSearch",params=params)
            return [data] if isinstance(data, dict) else data
        except Exception as e:
            print(f"{e}")
        # default
        return []


    def get_record_details(gin: Union[str, int]) -> Dict:
        try:
            access_key = f"{Helper_Functions.gin_to_access_key(gin)}!0-0-0"
            return Helper_Functions.API_call(url_suffix="LoadInstrument",params={"access_key": access_key})
        except Exception as e:
            print(f"{e}")
        # default
        return {}




    def record_finalized(record_dict: Dict) -> Dict:
        parties_to_contract = record_dict.get("PartyCollection", [])
        side_A_to_contract,side_B_to_contract = Helper_Functions.get_sides_to_contract(parties_to_contract)
        instance_number = record_dict.get("InstrumentNumber")
        record_timestamp = Helper_Functions.date_to_timestamp(record_dict.get("FileDate") or record_dict.get("CreateDate"))
        instrument_type = record_dict.get("InstrumentType") or {}
        doc_type = instrument_type.get("Description") or instrument_type.get("ShortDescription")
        gin = record_dict.get("Gin") or ""
        img_prefix = Helper_Functions.gin_to_access_key(gin) if gin else ""
        num_pages = record_dict.get("NumberOfPages") or 1
        image_links = Helper_Functions.get_image_links(gin, img_prefix, num_pages)
        organized_record_dict = {
            "instrument_number": instance_number,
            "from": side_A_to_contract,
            "to": side_B_to_contract,
            "record_date": record_timestamp,
            "doc_type": doc_type,
            "image_links": image_links,
        }
        return organized_record_dict


