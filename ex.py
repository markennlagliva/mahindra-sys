url = "http://127.0.0.1:8000/employee_dashboard/"
import re
# Define a regex pattern to match "employee_dashboard"
pattern = r'/([^/]+)/$'

# Use re.search() to find the pattern in the URL
match = re.search(pattern, url)

if match:
    employee_dashboard = match.group(1)
    print("Extracted: ", employee_dashboard)
else:
    print("Pattern not found in the URL.")