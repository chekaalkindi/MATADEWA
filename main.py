import argparse

from modules.github_search import github_search
from modules.reddit_search import reddit_search
from modules.analyzer import analyze_results
from modules.holehe_search import holehe_search
from modules.sherlock_search import sherlock_search


def banner():

    print(r"""

███╗   ███╗ █████╗ ████████╗ █████╗ ██████╗ ███████╗██╗    ██╗ █████╗
████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║    ██║██╔══██╗
██╔████╔██║███████║   ██║   ███████║██║  ██║█████╗  ██║ █╗ ██║███████║
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║██║  ██║██╔══╝  ██║███╗██║██╔══██║
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██████╔╝███████╗╚███╔███╔╝██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝

        MATADEWA OSINT CLI by chekaalkindi
""")

def main():

    banner()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="Target username / email / name"
    )

    args = parser.parse_args()

    query = args.query

    print(f"[+] Searching target: {query}\n")

    findings = []

    github_results = github_search(query)
    reddit_results = reddit_search(query)

    findings.extend(github_results)
    findings.extend(reddit_results)

    print("[+] Findings:\n")

    for item in findings:
        print(item)

    print("\n[+] AI Analysis:\n")

    summary = analyze_results(query, findings)

    print(summary)

if __name__ == "__main__":
    main()
