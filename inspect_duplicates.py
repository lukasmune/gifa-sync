from collections import defaultdict

from normalizer import normalize_company_name
from scraper import fetch_gifa_2023_exhibitors


exhibitors = fetch_gifa_2023_exhibitors()

groups = defaultdict(list)

for record in exhibitors:
    key = normalize_company_name(record.get("name"))
    groups[key].append(record)


for normalized_name, records in groups.items():
    if len(records) <= 1:
        continue

    print(f"\n{'=' * 80}")
    print(normalized_name)

    for record in records:
        print(
            {
                "type": record.get("type"),
                "id": record.get("id"),
                "exh": record.get("exh"),
                "exhSeoId": record.get("exhSeoId"),
                "name": record.get("name"),
                "country": record.get("country"),
                "city": record.get("city"),
                "location": record.get("location"),
            }
        )