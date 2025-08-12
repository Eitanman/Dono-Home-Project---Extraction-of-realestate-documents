# Dono-Home-Project---Extraction-of-realestate-documents
As part of a home assignment preceeding an interview for a data engineering role with Dono, I developed a Python tool that retrieves and processes real estate documents from a Florida property records API. The tool extracts detailed record information, including parties, document types, dates, and associated images.

The Access to the API and retreiving all the relevant information happens in a couple of stages:
  1. With the user's input (first name, last name, start date, thru date), we retreive the relevant documents' serial number/code (called gin). The relevant API: https://recording.seminoleclerk.org/DuProcessWebInquiry/Home/CriteriaSearch
  2. We decode the gin (turn the digits into letters) and use it to gain access to the document itself. The relevant API: https://recording.seminoleclerk.org/DuProcessWebInquiry/Home/LoadInstrument
  3. After accessing the document we retreive all the relevant information in JSON form, extract it and print in format.

Note: The API returns an HTTP 200 status even when rate-limited, but includes an error message in the response. To handle this, I implemented a custom check in the code to detect these cases and raise an error manually.
