import re
from typing import List, Dict

class DataExtraction:
    def extract_emails(self, text: str) -> List[str]:
        # Handles multiple emails in a string
        pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
        return re.findall(pattern, text)

    def extract_urls(self, text: str) -> List[str]:
        # Handles  urls
        pattern = r"https?://[^\s,;]+"
        return re.findall(pattern, text)

    def extract_phones(self, text: str) -> List[str]:
        # Handles (123) 456-7890, 123-456-7890, 123.456.7890, 123 456 7890
        pattern = r"(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4})"
        matches = re.findall(pattern, text)
        return [m for m in matches if m]

    def extract_credit_cards(self, text: str) -> List[str]:
        # Handles 1234 5678 9012 3456 and 1234-5678-9012-3456
        pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
        return re.findall(pattern, text)

    def extract_times(self, text: str) -> List[str]:
        # Handles 14:30, 2:30 PM, 2:30am, 14:30:00
        pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][mM])?\b"
        return re.findall(pattern, text)



    def extract_all(self, strings: List[str]) -> List[Dict[str, str]]:
        results = []
        for s in strings:
            for email in self.extract_emails(s):
                results.append({"type": "email", "value": email})
            for url in self.extract_urls(s):
                results.append({"type": "url", "value": url})
            for phone in self.extract_phones(s):
                results.append({"type": "phone", "value": phone})
            for card in self.extract_credit_cards(s):
                results.append({"type": "credit_card", "value": card})
            for time in self.extract_times(s):
                results.append({"type": "time", "value": time})
        return results

if __name__ == "__main__":
    # Sample test cases including edge cases
    test_data = [
        "Contact: user@example.com or firstname.lastname@company.co.uk, not-an-email@, @missingusername.com",
        "Visit https://www.example.com, https://subdomain.example.org/page, and malformed://url.com",
        "Call (123) 456-7890, 123-456-7890, 123.456.7890, 123 456 7890, 1234567890, (123)-456-7890",
        "Card: 1234 5678 9012 3456, 1234-5678-9012-3456, 1234567890123456, 1234-5678-9012-345",
        "Meeting at 14:30, lunch at 2:30 PM, and invalid time 25:99.",
        "Random text with no matches.",
    ]
    extractor = DataExtraction()
    extracted = extractor.extract_all(test_data)
    print("Extracted Data:")
    for item in extracted:
        print(f"{item['type']}: {item['value']}")
