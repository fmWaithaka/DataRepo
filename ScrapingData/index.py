import requests
from bs4 import BeautifulSoup
import pdfkit

# Specify the path to the wkhtmltopdf executable
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Make a request to the main page
main_url = "https://cs.dkut.ac.ke/staff-profiles/"
r = requests.get(main_url)

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')

# Find the links to the individual staff profile pages
link_elements = soup.select('a[href^="https://cs.dkut.ac.ke/"]')  # adjust this selector as needed

all_html = ''   # variable to store the combined HTML

# Loop over the links and scrape each page
for link_element in link_elements:
    # Get the URL of the staff profile page
    profile_url = link_element['href']

    # Make a request to the staff profile page
    r = requests.get(profile_url)

    # Parse the HTML content
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get the HTML of the webpage
    html = str(soup)

    # Add the HTML to the combined HTML
    all_html += html

# Specify the path where you want to save the PDF
output_path = r"C:\Users\Francis\Desktop\DataRepo\Data\Train\output.pdf"

# Save the HTML as a PDF
pdfkit.from_string(all_html, output_path, configuration=config)
