from enum import Enum

class Headers(Enum):
    COMMON_HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://recording.seminoleclerk.org/DuProcessWebInquiry/index.html",
    }

class gin_conversion_table(Enum):
    DIGIT_TO_LETTER = {
        '0': 'J', '1': 'A', '2': 'B', '3': 'C', '4': 'D',
        '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I'
    }
