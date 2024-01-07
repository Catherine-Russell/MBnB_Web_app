from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_homepage_loads_correctly_when_logged_out(page, test_web_address, db_connection):
    db_connection.seed("seeds/MBnB.sql")
    page.goto(f"http://{test_web_address}/")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Mbnb")

    space_headers = page.locator(".space-card h2")
    print(space_headers)
    expect(space_headers).to_have_text([
        "Mediterranean Villa",
        "English Cottage",
        "Alpine lodge",
        "Studio Apartment",
        "Tent",
        "Bamboo Cabin"
    ])

    space_prices = page.locator(".space-card .space-price")
    print(space_prices)
    expect(space_prices).to_have_text([
        "From £281 per night",
        "From £150 per night",
        "From £105 per night",
        "From £197 per night",
        "From £75 per night",
        "From £230 per night"
    ])
