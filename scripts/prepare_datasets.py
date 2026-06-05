import csv
import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]

CSV_PATH = ROOT_DIR / "data" / "raw" / "netflix_titles.csv"
OUTPUT_PATH = ROOT_DIR / "data" / "raw" / "datasets.json"


def clean_text(value: str) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def main():
    datasets = []

    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader):
            title = clean_text(row.get("title", ""))
            item_type = clean_text(row.get("type", ""))
            release_year = clean_text(row.get("release_year", ""))
            genres = clean_text(row.get("listed_in", ""))
            description = clean_text(row.get("description", ""))

            if not title or not description:
                continue

            text = (
                f"Title: {title}. "
                f"Type: {item_type}. "
                f"Release year: {release_year}. "
                f"Genres: {genres}. "
                f"Description: {description}"
            )

            datasets.append({
                "id": len(datasets),
                "name": title,
                "text": text
            })

    output = {"datasets": datasets}

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(datasets)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()