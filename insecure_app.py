import urllib.request

def fetch_data():
    # Insecure HTTP request (CodeQL should flag non-HTTPS traffic)
    url = "http://example.com/api/data"
    response = urllib.request.urlopen(url)
    return response.read()

fetch_data()
