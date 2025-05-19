# 🔍 Regex Data Extraction Tool  

**A Python tool to extract special  data patterns (emails, URLs, phone numbers, etc.) using optimized regex.**  

---

## 🚀 Project Overview  
This Python tool identifies and extracts structured data from text using **highly optimized regular expressions**. Perfect for onboarding hackathons or data preprocessing tasks!  

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
   ```bash  
   git clone https://github.com/Emmanuella00/alu_regex-data-extraction-Emmanuella00.git  
Navigate to the project directory:

cd alu_regex-data-extraction-Emmanuella00  
Ensure Python 3.x is installed:

bash
python3 --version  
📂 File Structure
alu_regex-data-extraction-Emmanuella00/  
├── data-extractor.py  # Main extraction script  
└── README.md          # Documentation  
🏃 Usage
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

🛡️ Handling Edge Cases
Pattern	Handled Cases	Ignored Cases
Emails	Subdomains, aliases	Missing @
URLs	HTTP/HTTPS, subdomains	Invalid schemes/domains
Phone Numbers	International, multiple formats	Non-standard digit counts
Credit Cards	Hyphenated/spaced formats	Non-matching patterns
Time Formats	24-hour, 12-hour (AM/PM)	Invalid times (e.g., 25:61)
HTML Tags	Standard tags (<div>, <a>)	Malformed tags
Hashtags	Alphanumeric with underscores	Non-hashtag words
Currency	Dollar amounts with commas/decimals	Non-currency values
👏 Credits
Developed by Emmanuella Ikirezi
