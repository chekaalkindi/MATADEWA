import requests

def github_search(query):

    url = f"https://api.github.com/search/users?q={query}"

    response = requests.get(url)

    results = []

    if response.status_code == 200:

        data = response.json()

        for item in data.get("items", []):

            results.append({
                "platform": "github",
                "username": item.get("login"),
                "profile": item.get("html_url")
            })

    return results
