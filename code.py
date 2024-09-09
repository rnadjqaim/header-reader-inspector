import argparse
import requests

HEADER_EXPLANATIONS = {
    "Content-Type": "Indicates the media type of the resource (e.g., text/html, application/json).",
    "Cache-Control": "Directs caching mechanisms on how to handle the content (e.g., no-cache, max-age).",
    "Strict-Transport-Security": "Enforces secure (HTTPS) connections to the server.",
    "X-Frame-Options": "Indicates whether the page can be displayed in a frame or iframe (to prevent clickjacking attacks).",
    "X-XSS-Protection": "Enables the Cross-site scripting (XSS) filter in browsers to prevent XSS attacks.",
    "Set-Cookie": "Stores data in the user's browser to maintain session state across requests."
}

def explain_header(header, value):
    explanation = HEADER_EXPLANATIONS.get(header, "No explanation found. Refer to header documentation.")
    return f"{header}: {value}\nExplanation: {explanation}\n"

def analyze_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print(f"\nAnalyzing headers for {url}:\n")
        for header, value in headers.items():
            print(explain_header(header, value))
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

def main():
    parser = argparse.ArgumentParser(description="Analyze HTTP headers of a given URL.")
    parser.add_argument("url", help="URL to fetch and analyze headers from.")
    args = parser.parse_args()
    analyze_headers(args.url)

if __name__ == "__main__":
    main()
