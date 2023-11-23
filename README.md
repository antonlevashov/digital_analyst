To create a web scraper, we will need to use libraries such as `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML and XML, and `lxml` for processing XML and HTML in Python. 

We will create two Python files: `main.py` and `scraper.py`. 

The `scraper.py` will contain two functions: `parse_sitemap` and `extract_text`. The `parse_sitemap` function will take a sitemap URL as input, download the XML file, parse it, and return a list of URLs. The `extract_text` function will take a URL as input, download the HTML, parse it, and return the text content.

The `main.py` will import the functions from `scraper.py`, take a sitemap URL as input, use `parse_sitemap` to get the URLs, use `extract_text` to get the text from each URL, and print the text.