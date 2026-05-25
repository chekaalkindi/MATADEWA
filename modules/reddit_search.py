import requests

def reddit_search(query):

    headers = {
        "User-Agent": "MATADEWA"
    }

    url = f"https://www.reddit.com/search.json?q={query}"

    response = requests.get(url, headers=headers)

    results = []

    if response.status_code == 200:

        posts = response.json()["data"]["children"]

        for post in posts[:10]:

            pdata = post["data"]

            results.append({
                "platform": "reddit",
                "title": pdata.get("title"),
                "author": pdata.get("author")
            })

    return results
