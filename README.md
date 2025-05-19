Regex Onboarding Hackathon 

Welcome to the Regex - Onboarding Hackathon tool, a tool that will help us extract critical data like emails, URLs, Phone numbers, Credit card numbers, Hashtags, Html tags, time formats and currency values.

Project Overview
This project is a python Project designed to identify and extract key patterns from text using highly optimized regex patterns. 

Features
Extracts the following patterns:

Email addresses (e.g., user@example.com, firstname.lastname@company.co.uk)

URLs (e.g., https://www.example.com, http://subdomain.example.org/page)

Phone numbers (e.g., (123) 456-7890, 123-456-7890, 123.456.7890)

Credit card numbers (e.g., 1234 5678 9012 3456, 1234-5678-9012-3456)

Time formats (e.g., 14:30, 2:30 PM)

HTML tags

Hashtags (e.g., #example, #ThisIsAHashtag)

Currency amounts (e.g., $19.99, $1,234.56)

Prerequisites
Python 3.x

Installation
1.Clone the repository:

git clone https://github.com/Emmanuella00/alu_regex-data-extraction-Emmanuella00.git
2.Navigate to the project directory:

cd alu_regex-data-extraction-Emmanuella00
Ensure Python 3.x is installed:

python3 --version
File Structure
alu_regex-data-extraction-Emmanuella00/
│
├── data-extractor.py        
└── README.md           
Usage
Run the extraction script:

To run the script and see the data extraction in action, simply run the extractor.py file:

python3 data-extractor.py
This will output the extracted data, such as email addresses, URLs, phone numbers, etc., based on the sample text in the script.

How It Works
Extractor Script (data-extractor.py)
Regex Patterns: The script uses Python's re library to define regex patterns for each data type. Each pattern is designed to match specific formats (e.g., email, URL, phone number).

Text Processing: The script processes a sample string (sample_text) that contains various data examples. It applies the regex patterns to find all matches and stores the results in corresponding variables.

Output: The extracted data is printed in a labeled format for easy reading.

Handling Edge Cases
Emails:

Handles different valid email formats (e.g., with subdomains, aliases).
Ignores invalid email formats (e.g., missing "@" symbol).
URLs:

Supports both HTTP and HTTPS URLs.
Ignores invalid URLs without a valid scheme or domain.
Phone Numbers:

Supports various formats like (123) 456-7890, 123-456-7890, and 123.456.7890.
Handles international numbers and non-standard formats.
Credit Cards:

Recognizes both spaced and hyphenated formats for credit card numbers.
Ignores numbers that don't match typical credit card patterns.
Times:

Supports 24-hour and 12-hour ( AM/PM) formats.
Ignores invalid times.
HTML Tags:

Matches standard HTML tags.
Ignores malformed or unrecognized tags.
Hashtags:

Correctly identifies hashtags in text.
Ignores non-hashtag words.
Currency Amounts:

Recognizes dollar amounts with or without commas and decimal places.
Ignores non-currency values

Credit:
Developed by Emmanuella Ikirezi
