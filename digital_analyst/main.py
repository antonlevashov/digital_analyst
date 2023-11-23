from scraper import parse_sitemap, extract_text

def main():
    sitemap_url = input("Enter the sitemap URL: ")
    urls = parse_sitemap(sitemap_url)
    for url in urls:
        text = extract_text(url)
        print(text)

if __name__ == "__main__":
    main()
