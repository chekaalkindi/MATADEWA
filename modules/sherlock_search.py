import subprocess
import re

def sherlock_search(username):

    print(f"[+] Running Sherlock on: {username}")

    result = subprocess.run(
        [
            "python3",
            "sherlock/sherlock",
            username,
            "--print-found"
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout

    findings = []

    lines = output.splitlines()

    for line in lines:

        if "http" in line:

            urls = re.findall(r'(https?://\\S+)', line)

            for url in urls:

                findings.append({
                    "source": "sherlock",
                    "url": url
                })

    return findings
