from database import (
    get_or_create_exhibition,
    initialize_database,
    sync_exhibitor,
)


def test_same_company_can_have_multiple_gifa_records(tmp_path, monkeypatch):
    import database

    database_path = tmp_path / "test.db"

    monkeypatch.setattr(database, "DATABASE_PATH", database_path)
    monkeypatch.setattr(database, "DATA_DIR", tmp_path)

    initialize_database()

    exhibition_id = get_or_create_exhibition(
        event_name="GIFA",
        edition=2023,
        event_code="GMTN2023.gifa",
    )

    record_1 = {
        "type": "profile",
        "exh": "GMTN2023.TEST001",
        "exhSeoId": "SEO001",
        "name": "Example Foundry GmbH",
        "country": "Germany",
        "city": "Düsseldorf",
        "location": "Hall 1 / A01",
        "premium": False,
        "tags": [],
        "eventIcons": [{"label": "GIFA 2023"}],
    }

    record_2 = {
        "type": "profile",
        "exh": "GMTN2023.TEST002",
        "exhSeoId": "SEO002",
        "name": "Example Foundry GmbH",
        "country": "Germany",
        "city": "Düsseldorf",
        "location": "Hall 1 / A02",
        "premium": False,
        "tags": [],
        "eventIcons": [{"label": "GIFA 2023"}],
    }

    result_1 = sync_exhibitor(record_1, exhibition_id)
    result_2 = sync_exhibitor(record_2, exhibition_id)

    assert result_1["created"] is True
    assert result_2["created"] is False
    assert result_1["company_id"] == result_2["company_id"]


def test_same_company_across_exhibitions_keeps_same_company_id(
    tmp_path,
    monkeypatch,
):
    import database

    database_path = tmp_path / "test.db"

    monkeypatch.setattr(database, "DATABASE_PATH", database_path)
    monkeypatch.setattr(database, "DATA_DIR", tmp_path)

    initialize_database()

    gifa_2023_id = get_or_create_exhibition(
        event_name="GIFA",
        edition=2023,
        event_code="GMTN2023.gifa",
    )

    gifa_2027_id = get_or_create_exhibition(
        event_name="GIFA",
        edition=2027,
        event_code="GMTN2027.gifa",
    )

    record_2023 = {
        "type": "profile",
        "exh": "GMTN2023.TEST001",
        "exhSeoId": "SEO2023",
        "name": "Example Foundry GmbH",
        "country": "Germany",
        "city": "Düsseldorf",
        "location": "Hall 1 / A01",
        "premium": False,
        "tags": [],
        "eventIcons": [{"label": "GIFA 2023"}],
    }

    record_2027 = {
        "type": "profile",
        "exh": "GMTN2027.TEST999",
        "exhSeoId": "SEO2027",
        "name": "Example Foundry GmbH",
        "country": "Germany",
        "city": "Düsseldorf",
        "location": "Hall 5 / B20",
        "premium": False,
        "tags": [],
        "eventIcons": [{"label": "GIFA 2027"}],
    }

    result_2023 = sync_exhibitor(record_2023, gifa_2023_id)
    result_2027 = sync_exhibitor(record_2027, gifa_2027_id)

    assert result_2023["created"] is True
    assert result_2027["created"] is False
    assert result_2023["company_id"] == result_2027["company_id"]

    with database.get_connection() as connection:
        company_count = connection.execute(
            "SELECT COUNT(*) FROM companies"
        ).fetchone()[0]

        exhibition_count = connection.execute(
            "SELECT COUNT(*) FROM exhibition_companies"
        ).fetchone()[0]

    assert company_count == 1
    assert exhibition_count == 2

def test_repeated_sync_does_not_create_duplicates(
    tmp_path,
    monkeypatch,
):
    import database

    database_path = tmp_path / "test.db"

    monkeypatch.setattr(database, "DATABASE_PATH", database_path)
    monkeypatch.setattr(database, "DATA_DIR", tmp_path)

    initialize_database()

    exhibition_id = get_or_create_exhibition(
        event_name="GIFA",
        edition=2023,
        event_code="GMTN2023.gifa",
    )

    record = {
        "type": "profile",
        "exh": "GMTN2023.TEST001",
        "exhSeoId": "SEO001",
        "name": "Example Foundry GmbH",
        "country": "Germany",
        "city": "Düsseldorf",
        "location": "Hall 1 / A01",
        "premium": False,
        "tags": [],
        "eventIcons": [{"label": "GIFA 2023"}],
    }

    first_result = sync_exhibitor(
        record,
        exhibition_id,
    )

    second_result = sync_exhibitor(
        record,
        exhibition_id,
    )

    assert first_result["created"] is True
    assert second_result["created"] is False
    assert first_result["company_id"] == second_result["company_id"]

    with database.get_connection() as connection:
        company_count = connection.execute(
            "SELECT COUNT(*) FROM companies"
        ).fetchone()[0]

        exhibition_record_count = connection.execute(
            "SELECT COUNT(*) FROM exhibition_companies"
        ).fetchone()[0]

    assert company_count == 1
    assert exhibition_record_count == 1