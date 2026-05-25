import subprocess

def holehe_search(email):

    print(f"[+] Running Holehe on: {email}")

    result = subprocess.run(
        [
            "holehe",
            email
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout

    findings = []

    lines = output.splitlines()

    for line in lines:

        if "[+]" in line:

            findings.append({
                "source": "holehe",
                "platform": line.replace("[+]", "").strip()
            })

    return findings
