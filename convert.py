import os
import json
import subprocess


def generate_srs_domains(domains: list[str]) -> bytes:
    data = {"version": 3, "rules": [{"domain_suffix": domains}]}
    srs_file_path = "domains.srs"
    json_file_path = "domains.json"
    try:
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        subprocess.run(
            ["sing-box", "rule-set", "compile", json_file_path, "-o", srs_file_path],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Compile error {json_file_path}: {e}")
    except Exception as e:
        print(f"Error while processing {domains}: {e}")


def main():
    domains = []
    with open("domains.txt") as f:
        for line in f.readlines():
            domain = line.strip()
            if domain and domain[0] not in ["/", "#"]:
                domains.append(domain)
    
    generate_srs_domains(domains)


if __name__ == "__main__":
    main()
