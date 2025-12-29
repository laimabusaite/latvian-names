#!/usr/bin/env python3
"""
Script to download CSV data from Latvian government data portal.
"""

import requests
import os


def download_csv(url: str, filename: str) -> None:
    """
    Download a CSV file from a URL and save it locally.

    Args:
        url: URL to the CSV file
        filename: Local filename to save the CSV (relative to repository root)
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    try:
        print(f"Downloading from: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Save the raw content
        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully downloaded and saved to: {filename}")
        print(f"  File size: {len(response.content)} bytes\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {url}: {e}\n")
        raise
    except Exception as e:
        print(f"✗ Error saving file {filename}: {e}\n")
        raise


def main():
    """Main function to download both CSV files."""
    # URLs from the data portal
    name_days_url = "https://data.gov.lv/dati/dataset/2a880497-a25b-4e59-990b-382ca155fb0c/resource/c6d6faaa-87bf-4960-b658-280f04a7ba05/download/paplaintais-kalendrvrdu-saraksts.csv"
    traditional_name_days_url = "https://data.gov.lv/dati/dataset/2a880497-a25b-4e59-990b-382ca155fb0c/resource/39d01c5b-6964-4e91-b05c-45e6fbf1b77a/download/latvieu-tradicionlo-vrdadienu-saraksts.csv"
    gender_url = "https://data.gov.lv/dati/dataset/ac246d11-d5d6-445e-a6c7-8f5013460335/resource/937d3c8c-c95f-4208-8dce-8dd76b77d94f/download/vardi-dz-20250701.csv"

    print("=" * 60)
    print("Downloading Latvian Name Days and Gender Data")
    print("=" * 60)
    print()

    # Download name days CSV (expanded list)
    print("1. Downloading expanded name days data...")
    download_csv(name_days_url, "data/name_days.csv")

    # Download traditional name days CSV
    print("2. Downloading traditional name days data...")
    download_csv(traditional_name_days_url, "data/traditional_name_days.csv")

    # Download gender data CSV
    print("3. Downloading gender data...")
    download_csv(gender_url, "data/gender_data.csv")

    print("=" * 60)
    print("All downloads completed!")
    print("=" * 60)
    print("\nFiles saved:")
    print("  - data/name_days.csv")
    print("  - data/traditional_name_days.csv")
    print("  - data/gender_data.csv")


if __name__ == "__main__":
    main()
