import requests, re

REPO = "Syphilum/Proyek-Kolaborasi-Python-AF141"
README_PATH = "README.md"

def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def generate_table(contributors):
    total = sum(user['contributions'] for user in contributors)
    rows = []
    for user in contributors:
        percent = round(100 * user['contributions'] / total) if total else 0
        display_name = user['login'].capitalize()
        rows.append(f"| {display_name} | {percent}% | {user['contributions']} | [{user['login']}](https://github.com/{user['login']}) | ![{user['login']}](https://avatars.githubusercontent.com/u/{user['id']}?v=4) |")
    header = "| Nama Kontributor | Persentase Kontribusi | Jumlah Kontribusi | Profil GitHub | Avatar |\n|------------------|-----------------------|-------------------|---------------|--------|"
    return header + "\n" + "\n".join(rows)

def replace_table(readme, new_table):
    # Ganti tabel contributors di README (pastikan anchor unik di README)
    pattern = r"(\| Nama Kontributor[\s\S]+?\|\n)(?=\n>|$)"
    return re.sub(pattern, new_table + "\n", readme, count=1)

if __name__ == "__main__":
    contributors = get_contributors(REPO)
    with open(README_PATH, "r") as f:
        readme = f.read()
    new_table = generate_table(contributors)
    updated = replace_table(readme, new_table)
    with open(README_PATH, "w") as f:
        f.write(updated)
