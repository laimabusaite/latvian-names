#!/usr/bin/env python3
"""
Script to process name days CSV and create JSON with individual name entries.
"""

import csv
import json
from typing import Dict, Any, Optional


def date_sort_key(date_str: str) -> tuple:
    """
    Convert date string (DD.MM format) to a tuple for proper sorting.

    Args:
        date_str: Date string in format "DD.MM"

    Returns:
        Tuple (month, day) for sorting
    """
    try:
        day, month = date_str.split(".")
        return (int(month), int(day))
    except (ValueError, AttributeError):
        # If parsing fails, return (0, 0) to put invalid dates first
        return (0, 0)


def load_gender_data(gender_file: str) -> Dict[str, Dict[str, Any]]:
    """
    Load gender data from CSV and create a lookup dictionary.

    Args:
        gender_file: Path to the gender data CSV file

    Returns:
        Dictionary mapping names to dicts with 'gender' and 'count'
    """
    gender_lookup = {}

    try:
        with open(gender_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                vardi = row.get("Vardi", "").strip()
                dzimums = row.get("Dzimums", "").strip()
                skaits = row.get("Skaits", "").strip()

                # Skip empty entries and "-"
                if not vardi or vardi == "-":
                    continue

                if dzimums:
                    # Parse count, default to 0 if invalid
                    try:
                        count = int(skaits) if skaits else 0
                    except (ValueError, TypeError):
                        count = 0

                    # Normalize gender values
                    if dzimums.upper() == "SIEVIETE":
                        normalized_gender = "Sieviete"
                    elif dzimums.upper() == "VĪRIETIS":
                        normalized_gender = "Vīrietis"
                    else:
                        normalized_gender = dzimums

                    # Split multiple names separated by spaces
                    # names = [name.strip() for name in vardi.split() if name.strip()]
                    names = vardi.strip()
                    # Store the gender and count for each individual name
                    # If a name appears multiple times, keep the entry with the highest count
                    # for name in names:
                    if names not in gender_lookup:
                        gender_lookup[names] = {
                            "gender": normalized_gender,
                            "count": count,
                        }
                    else:
                        # If name already exists, keep the entry with the higher count
                        if count > gender_lookup[names]["count"]:
                            gender_lookup[names] = {
                                "gender": normalized_gender,
                                "count": count,
                            }

        return gender_lookup

    except FileNotFoundError:
        print(
            f"⚠ Warning: Gender data file '{gender_file}' not found. Using rules only."
        )
        return {}
    except Exception as e:
        print(f"⚠ Warning: Error loading gender data: {e}. Using rules only.")
        return {}


def clean_name(name: str) -> str:
    """
    Clean name by removing unwanted symbols and text.

    Args:
        name: The name to clean

    Returns:
        Cleaned name string
    """
    if not name:
        return ""

    # Remove specific symbols: . ( ) :
    cleaned = name.replace(".", "").replace("(", "").replace(")", "").replace(":", "")

    # Remove "LTG" (case-insensitive)
    cleaned = cleaned.replace("LTG", "")

    # Remove any extra whitespace
    cleaned = cleaned.strip()

    return cleaned


def determine_gender_by_rules(name: str) -> str:
    """
    Determine gender based on name ending rules.

    Args:
        name: The name to check

    Returns:
        'Vīrietis', 'Sieviete', or 'Nedefinēts'
    """
    if not name:
        return "Nedefinēts"

    name_lower = name.lower().strip()

    # Female names end with "a" or "e"
    if name_lower.endswith("a") or name_lower.endswith("e"):
        return "Sieviete"

    # Male names end with "s", "š", or "o"
    if name_lower.endswith("s") or name_lower.endswith("š") or name_lower.endswith("o"):
        return "Vīrietis"

    # Other names are undetermined
    return "Nedefinēts"


def get_gender(name: str, gender_lookup: Dict[str, Dict[str, Any]]) -> str:
    """
    Get gender for a name, using lookup first, then fallback rules.

    Args:
        name: The name to look up
        gender_lookup: Dictionary from gender data CSV

    Returns:
        Gender string ('Vīrietis', 'Sieviete', or 'Nedefinēts')
    """
    # First try exact match
    if name in gender_lookup:
        return gender_lookup[name]["gender"]

    # Try case-insensitive match
    name_upper = name.upper()
    for key in gender_lookup:
        if key.upper() == name_upper:
            return gender_lookup[key]["gender"]

    # If not found, use fallback rules
    return determine_gender_by_rules(name)


def get_count(name: str, gender_lookup: Dict[str, Dict[str, Any]]) -> int:
    """
    Get count for a name from the gender data.

    Args:
        name: The name to look up
        gender_lookup: Dictionary from gender data CSV

    Returns:
        Count (0 if name not found in gender data)
    """
    # First try exact match
    if name in gender_lookup:
        return gender_lookup[name]["count"]

    # Try case-insensitive match
    name_upper = name.upper()
    for key in gender_lookup:
        if key.upper() == name_upper:
            return gender_lookup[key]["count"]

    return 0


def load_popularity_data(popularity_file: str) -> Dict[str, Dict[str, Optional[int]]]:
    """
    Load newborn name popularity data from CSV file.

    Args:
        popularity_file: Path to the popularity data CSV file (tab-separated)

    Returns:
        Dictionary mapping names to dictionaries of year -> count
    """
    popularity_lookup = {}
    years = []

    try:
        with open(popularity_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter="\t")

            # Extract year columns (numeric columns)
            all_columns = reader.fieldnames
            years = [col for col in all_columns if col.isdigit()]

            for row in reader:
                vards = row.get("vārds", "").strip()
                if not vards:
                    continue

                # Create year -> count dictionary for this name
                year_data = {}
                for year in years:
                    try:
                        count_str = row.get(year, "").strip()
                        if count_str:
                            count = int(count_str)
                            year_data[year] = count
                        else:
                            year_data[year] = 0
                    except (ValueError, TypeError):
                        year_data[year] = 0

                # Store with case-insensitive key for lookup
                vards_upper = vards.upper()
                if vards_upper not in popularity_lookup:
                    popularity_lookup[vards_upper] = {
                        "original_name": vards,
                        "years": year_data,
                    }

        return popularity_lookup, years

    except FileNotFoundError:
        print(f"⚠ Warning: Popularity data file '{popularity_file}' not found.")
        return {}, []
    except Exception as e:
        print(f"⚠ Warning: Error loading popularity data: {e}")
        return {}, []


def get_popularity(
    name: str, popularity_lookup: Dict[str, Dict[str, Any]], years: list
) -> Dict[str, Optional[int]]:
    """
    Get popularity data for a name across all years.

    Args:
        name: The name to look up
        popularity_lookup: Dictionary from popularity data CSV
        years: List of year strings

    Returns:
        Dictionary mapping year -> count (or 0 if not found)
    """
    name_upper = name.upper()

    # Try exact match
    if name_upper in popularity_lookup:
        return popularity_lookup[name_upper]["years"]

    # If not found, return 0 for all years
    return {year: 0 for year in years}


def load_traditional_names(traditional_file: str) -> set:
    """
    Load traditional names from CSV and create a set for lookup.

    Args:
        traditional_file: Path to the traditional name days CSV file

    Returns:
        Set of traditional names (case-insensitive, stored as uppercase)
    """
    traditional_names = set()

    try:
        with open(traditional_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                vardadienas = row.get("vardadienas", "").strip()

                if vardadienas:
                    # Split names by comma and space, then by space
                    # Handle both comma-separated and space-separated names
                    names = []
                    for part in vardadienas.split(","):
                        # Split each comma-separated part by space
                        names.extend(
                            [name.strip() for name in part.split() if name.strip()]
                        )

                    # Add all names to the set (case-insensitive)
                    for name in names:
                        if name:
                            traditional_names.add(name.upper())

        return traditional_names

    except FileNotFoundError:
        print(
            f"⚠ Warning: Traditional name days file '{traditional_file}' not found. All names will be marked as 'paplašinātais'."
        )
        return set()
    except Exception as e:
        print(
            f"⚠ Warning: Error loading traditional names: {e}. All names will be marked as 'paplašinātais'."
        )
        return set()


def process_name_days(
    input_file: str,
    output_file: str,
    gender_file: str = None,
    popularity_file_0: str = None,
    popularity_file_1: str = None,
    traditional_file: str = None,
) -> None:
    """
    Read name days from CSV, split names by space, and create JSON entries with gender.

    Args:
        input_file: Path to the input CSV file (name_days.csv)
        output_file: Path to the output JSON file
        gender_file: Path to the gender data CSV file (gender_data.csv)
        popularity_file_0: Path to first popularity data CSV file
        popularity_file_1: Path to second popularity data CSV file
        traditional_file: Path to the traditional name days CSV file
    """
    entries = []

    # Load gender data if provided
    gender_lookup = {}
    if gender_file:
        print(f"Loading gender data from {gender_file}...")
        gender_lookup = load_gender_data(gender_file)
        print(f"✓ Loaded gender data for {len(gender_lookup)} names\n")

    # Load traditional names if provided
    traditional_names = set()
    if traditional_file:
        print(f"Loading traditional names from {traditional_file}...")
        traditional_names = load_traditional_names(traditional_file)
        print(f"✓ Loaded {len(traditional_names)} traditional names\n")

    # Load popularity data if provided
    popularity_lookup = {}
    years = []
    if popularity_file_0:
        print(f"Loading popularity data from {popularity_file_0}...")
        lookup_0, years_0 = load_popularity_data(popularity_file_0)
        popularity_lookup.update(lookup_0)
        years = years_0 if years_0 else years
        print(f"✓ Loaded popularity data for {len(lookup_0)} names\n")

    if popularity_file_1:
        print(f"Loading popularity data from {popularity_file_1}...")
        lookup_1, years_1 = load_popularity_data(popularity_file_1)
        popularity_lookup.update(lookup_1)
        if years_1 and not years:
            years = years_1
        print(f"✓ Loaded popularity data for {len(lookup_1)} names\n")

    if popularity_lookup:
        print(
            f"✓ Total popularity entries: {len(popularity_lookup)}, Years: {len(years)}\n"
        )

    try:
        with open(input_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                datums = row.get("datums", "").strip()
                vardadienas = row.get("vardadienas", "").strip()

                if datums and vardadienas:
                    # Remove trailing dot from date if present (e.g., "01.01." -> "01.01")
                    date = datums.rstrip(".")

                    # Split names by space
                    names = [
                        name.strip() for name in vardadienas.split() if name.strip()
                    ]

                    # Create an entry for each name with gender, count, and popularity
                    for name in names:
                        # Clean name before processing
                        name = clean_name(name)

                        # Skip empty names after cleaning
                        if not name:
                            continue

                        gender = get_gender(name, gender_lookup)
                        count = get_count(name, gender_lookup)

                        # Get popularity data
                        popularity = {}
                        if popularity_lookup and years:
                            popularity = get_popularity(name, popularity_lookup, years)

                        # Check if name is in traditional names
                        kalendars = (
                            "tradicionālais"
                            if name.upper() in traditional_names
                            else "paplašinātais"
                        )

                        entry = {
                            "name": name,
                            "date": date,
                            "gender": gender,
                            "count": count,
                            "kalendārs": kalendars,
                        }

                        # Add popularity data if available
                        if popularity:
                            entry["popularity"] = popularity

                        entries.append(entry)

        # Sort by date (month, day), then by name for better organization
        entries_sorted = sorted(
            entries, key=lambda x: (date_sort_key(x["date"]), x["name"])
        )

        # Save to JSON file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(entries_sorted, f, ensure_ascii=False, indent=2)

        print(f"✓ Successfully processed {len(entries_sorted)} name entries")
        print(f"✓ Data saved to {output_file}")

        # Print some statistics
        unique_dates = len(set(entry["date"] for entry in entries_sorted))
        unique_names = len(set(entry["name"] for entry in entries_sorted))

        # Gender statistics
        gender_stats = {"Vīrietis": 0, "Sieviete": 0, "Nedefinēts": 0}
        for entry in entries_sorted:
            gender = entry.get("gender", "Nedefinēts")
            if gender in gender_stats:
                gender_stats[gender] += 1

        print("\nStatistics:")
        print(f"  Total entries: {len(entries_sorted)}")
        print(f"  Unique dates: {unique_dates}")
        print(f"  Unique names: {unique_names}")
        print("\nGender distribution:")
        print(f"  Male (Vīrietis): {gender_stats['Vīrietis']}")
        print(f"  Female (Sieviete): {gender_stats['Sieviete']}")
        print(f"  Undetermined (Nedefinēts): {gender_stats['Nedefinēts']}")

        # Show a sample of the data
        print("\nSample entries (first 5):")
        for entry in entries_sorted[:5]:
            print(f"  {entry}")

    except FileNotFoundError:
        print(f"✗ Error: File '{input_file}' not found")
        raise
    except Exception as e:
        print(f"✗ Error processing file: {e}")
        raise


def main():
    """Main function."""
    input_file = "data/name_days.csv"
    gender_file = "data/gender_data.csv"
    traditional_file = "data/traditional_name_days.csv"
    output_file = "docs/name_days_processed.json"

    print("=" * 60)
    print("Processing Name Days CSV with Gender and Popularity Information")
    print("=" * 60)
    print()

    popularity_file_0 = "data/0_0_1920_2020_all_data.csv"
    popularity_file_1 = "data/1_0_1920_2020_all_data.csv"

    process_name_days(
        input_file,
        output_file,
        gender_file,
        popularity_file_0,
        popularity_file_1,
        traditional_file,
    )

    print()
    print("=" * 60)
    print("Processing completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
