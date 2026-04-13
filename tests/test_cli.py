from unittest.mock import patch
from cli.input_handler import get_workshop_details

def test_get_workshop_details():
    inputs = ["Workshop Name", "20 April 2026", "10:00 AM", "Summary", "Description"]
    with patch("builtins.input", side_effect=inputs):
        details = get_workshop_details()

    assert details["name"] == "Workshop Name"
    assert details["date"] == "20 April 2026"
    assert details["time"] == "10:00 AM"
    assert details["summary"] == "Summary"
    assert details["description"] == "Description"