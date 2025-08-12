from constants import Headers
from constants import gin_conversion_table
import requests
from typing import List, Dict
from typing import Union

BASE_URL = "https://recording.seminoleclerk.org/DuProcessWebInquiry/Home"

class Helper_Functions:
    def gin_to_access_key(gin: Union[str, int]) -> str:
        table = gin_conversion_table.DIGIT_TO_LETTER.value
        return ''.join(table[digit] for digit in str(gin))


    def date_to_timestamp(date_string: Union[str, None]) -> Union[str, None]:
        if not date_string:
            return None
        digits = ''.join(digit for digit in date_string if digit.isdigit())
        return int(digits) if digits else None


    def API_call(url_suffix: str, params: Dict[str, str]) -> Dict:
        resp = requests.get(f"{BASE_URL}/{url_suffix}", params=params,
                            headers=Headers.COMMON_HEADERS.value,
                            timeout=15)
        resp.raise_for_status()
        data = resp.json()
        call_failed_but_returned_200 = (isinstance(data, str) and "Too many requests" in data) or \
                            (isinstance(data, dict) and "Error" in data)
        if call_failed_but_returned_200 == True:
            raise RuntimeError(f"Server error: {data}")

        return resp.json()

    def get_image_links(gin: Union[str,int,None],img_prefix: Union[str,None],num_pages: Union[int,None]) -> List[str]:
        image_links = []
        if gin and img_prefix:
            image_links = [
                f"https://recording.seminoleclerk.org/DuProcessWebInquiry/Home/GetDocumentPage/{gin},{img_prefix},{i}"
                for i in range(num_pages)
            ]
        return image_links

    def get_sides_to_contract(parties_to_contract:List[Dict]):
        side_a = [party.get("PartyName") for party in parties_to_contract if party.get("Direction") == 1 and party.get("PartyName")]
        side_b = [party.get("PartyName") for party in parties_to_contract if party.get("Direction") == 0 and party.get("PartyName")]
        return  side_a, side_b
