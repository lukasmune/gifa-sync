# Fields owned by our internal sales team
# GIFA synchronization must never create, modify, or delete these fields
PROTECTED_FIELDS = {
    "sales_status",
    "sales_owner",
    "sales_notes",
}


def merge_gifa_data(existing_company, gifa_data):
    updated_company = existing_company.copy()

    for key, value in gifa_data.items():
        if key not in PROTECTED_FIELDS:
            updated_company[key] = value

    return updated_company