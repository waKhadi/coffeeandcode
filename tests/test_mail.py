from mail.sender import render_template

def test_render_template():
    details = {
        "name": "Python Rocks",
        "date": "20 April 2026",
        "time": "10:00 AM",
        "summary": "A summary",
        "description": "A description",
        "sender_email": "test@gmail.com"
    }
    html = render_template(details)

    assert "Python Rocks" in html
    assert "20 April 2026" in html
    assert "10:00 AM" in html
    assert "A summary" in html
    assert "A description" in html