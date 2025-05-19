#  Regex Data Extraction Hackathon

**Welcome to the Regex - Onboarding Hackathon tool, a tool that will help us extract critical data like emails, URLs, Phone numbers, Credit card numbers, Hashtags, Html tags, time formats and currency values by the use of Regex**  

---

##  Project Overview  
This Python Project for extracting data  from text using highly optimized regex patterns.   

---

## ✨ Features  
Extracts the following patterns:  
- **📧 Emails**  
  - `user@example.com`, `firstname.lastname@company.co.uk`  
- **🌐 URLs**  
  - `https://www.example.com`, `http://subdomain.example.org/page`  
- **📞 Phone Numbers**  
  - `(123) 456-7890`, `123-456-7890`, `123.456.7890`  
- **💳 Credit Card Numbers**  
  - `1234 5678 9012 3456`, `1234-5678-9012-3456`  
- **⏰ Time Formats**  
  - `14:30`, `2:30 PM`  
- **🖥️ HTML Tags**  
  - `<div>`, `<a href="...">`  
- **🏷️ Hashtags**  
  - `#example`, `#ThisIsAHashtag`  
- **💰 Currency Amounts**  
  - `$19.99`, `$1,234.56`  

---

## ⚙️ Prerequisites  
- Python 3.x  

---

## 🛠️ Installation  
1. Clone the repository:  
    
   git clone https://github.com/Emmanuella00/alu_regex-data-extraction-Emmanuella00.git  
2.Navigate to the project directory:

cd alu_regex-data-extraction-Emmanuella00  
3.Ensure Python 3.x is installed:


python3 --version  
📂 File Structure
alu_regex-data-extraction-Emmanuella00/  
├── data-extractor.py  # Main extraction script  
└── README.md          # Documentation
---  
 Usage

Run the extraction script:

bash
python3 data-extractor.py  
Example Output:
📧 Emails: ['user@example.com', 'firstname.lastname@company.co.uk']  
🌐 URLs: ['https://www.example.com', 'http://subdomain.example.org/page']  
📞 Phone Numbers: ['(123) 456-7890', '123-456-7890']  
...  
🧠 How It Works
1. Regex Patterns
Uses Python’s re library with optimized regex patterns for each data type.Each pattern is designed to match specific formats (e.g., email, URL, phone number).

2. Text Processing
The script processes a sample string (sample_text) that contains various data examples. It applies the regex patterns to find all matches and stores the results in corresponding variables.

3. Output 
The extracted data is printed in a labeled format for easy reading.
---
* Handling Edge Cases

-Emails
Handled: Subdomains, aliases (e.g., user@sub.example.com).

Ignored: Emails missing @ (e.g., userexample.com).

-URLs
Handled: HTTP/HTTPS URLs with subdomains (e.g., https://docs.example.org).

Ignored: Invalid schemes (e.g., ftp://example.com) or malformed domains.

-Phone Numbers
Handled: International formats, variations like (123) 456-7890 or 123.456.7890.

Ignored: Numbers with non-standard digit counts (e.g., 123-45).

-Credit Cards
Handled: Hyphenated (1234-5678-9012-3456) and spaced formats.

Ignored: Numbers that don’t match credit card patterns (e.g., 1234-ABCD).

-Time Formats
Handled: 24-hour (14:30), 12-hour with AM/PM (2:30 PM).

Ignored: Invalid times like 25:61 or 13:60 PM.
---
CREDITS:

Developed by Emmanuella Ikirezi
