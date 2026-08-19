from urllib.parse import urljoin

import re
import requests


GIFA_URL = (
    "https://www.gifa.com/vis/v1/en/search"
    "?_sort=date_asc&f_type=profile"
)


def test_gifa_is_reachable():
    response = requests.get(
        GIFA_URL,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    assert response.status_code == 200


def test_gifa_response_contains_data():
    response = requests.get(
        GIFA_URL,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    assert response.status_code == 200
    assert len(response.text) > 0

    print("\n--- RESPONSE HEAD ---")
    print(response.text[:2000])
    print("--- RESPONSE HEAD END ---")

    print("\nContent-Type:", response.headers.get("Content-Type"))

    from urllib.parse import urljoin

import requests


GIFA_URL = (
    "https://www.gifa.com/vis/v1/en/search"
    "?_sort=date_asc&f_type=profile"
)

GIFA_BASE_URL = "https://www.gifa.com"


def get_gifa_headers():
    return {
        "User-Agent": "Mozilla/5.0"
    }


def test_gifa_is_reachable():
    response = requests.get(
        GIFA_URL,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert response.status_code == 200


def test_gifa_response_contains_data():
    response = requests.get(
        GIFA_URL,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert response.status_code == 200
    assert len(response.text) > 0

    print("\n--- RESPONSE HEAD ---")
    print(response.text[:2000])
    print("--- RESPONSE HEAD END ---")

    print("\nContent-Type:", response.headers.get("Content-Type"))


def test_finder_loader_is_reachable():
    response = requests.get(
        GIFA_URL,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert response.status_code == 200

    html = response.text

    loader_path = "/static/all/finder-frontend/assets/loader.js"

    assert loader_path in html

    loader_url = urljoin(GIFA_BASE_URL, loader_path)

    loader_response = requests.get(
        loader_url,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert loader_response.status_code == 200

    print("\n--- LOADER.JS HEAD ---")
    print(loader_response.text[:5000])
    print("--- LOADER.JS HEAD END ---")

    print("\nLoader URL:", loader_url)
    print("Content-Type:", loader_response.headers.get("Content-Type"))

def test_finder_application_is_reachable():
    loader_url = urljoin(
        GIFA_BASE_URL,
        "/static/all/finder-frontend/assets/loader.js"
    )

    response = requests.get(
        loader_url,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert response.status_code == 200

    loader_js = response.text

    import_match = "import('./index-fzFnGgbV.js')"

    assert import_match in loader_js

    app_path = "/static/all/finder-frontend/assets/index-fzFnGgbV.js"
    app_url = urljoin(GIFA_BASE_URL, app_path)

    app_response = requests.get(
        app_url,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert app_response.status_code == 200

    print("\n--- FINDER APPLICATION HEAD ---")
    print(app_response.text[:10000])
    print("--- FINDER APPLICATION HEAD END ---")

    print("\nApplication URL:", app_url)
    print("Content-Type:", app_response.headers.get("Content-Type"))
    print("Application size:", len(app_response.text))

def test_exhibitor_directory_module_is_reachable():
    module_path = (
        "/static/all/finder-frontend/assets/"
        "Directory-BwqopVKM.js"
    )

    module_url = urljoin(GIFA_BASE_URL, module_path)

    response = requests.get(
        module_url,
        timeout=30,
        headers=get_gifa_headers()
    )

    assert response.status_code == 200

    javascript = response.text

    print("\n--- DIRECTORY MODULE ---")
    print(javascript)
    print("--- DIRECTORY MODULE END ---")

    print("\nModule URL:", module_url)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Module size:", len(javascript))

    assert len(javascript) > 0