import re
import unicodedata


def normalize_text(value):
    """
    Normalize general text for comparison.

    Example:
        "  AAGM Aalener Gießereimaschinen GmbH  "
        -> "aagm aalener giessereimaschinen gmbh"
    """

    if not value:
        return ""

    value = str(value).strip().lower()

    # Normalize Unicode characters.
    value = unicodedata.normalize("NFKD", value)

    # Remove combining marks.
    value = "".join(
        character
        for character in value
        if not unicodedata.combining(character)
    )

    # Replace punctuation with spaces.
    value = re.sub(r"[^a-z0-9]+", " ", value)

    # Collapse whitespace.
    value = re.sub(r"\s+", " ", value).strip()

    return value


def normalize_company_name(name):
    """
    Normalize a company name for identity matching.
    """

    return normalize_text(name)


def normalize_country(country):
    return normalize_text(country)


def normalize_city(city):
    return normalize_text(city)


def company_identity_key(name, country=None, city=None):
    """
    Create a deterministic identity key.

    The name is the primary identity component.
    Country and city provide additional context.
    """

    normalized_name = normalize_company_name(name)
    normalized_country = normalize_country(country)
    normalized_city = normalize_city(city)

    return "|".join(
        [
            normalized_name,
            normalized_country,
            normalized_city,
        ]
    )