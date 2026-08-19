from scraper import fetch_gifa_2023_exhibitors


def test_gifa_2023_dataset_contains_only_profile_records():
    exhibitors = fetch_gifa_2023_exhibitors()

    assert len(exhibitors) > 0
    assert all(
        record.get("type") == "profile"
        for record in exhibitors
    )