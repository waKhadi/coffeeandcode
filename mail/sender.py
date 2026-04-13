def render_template(details):
    with open('mail/templates/workshop.html', 'r') as f:
        template = f.read()

    for key, value in details.items():
        template = template.replace('{{' + key + '}}', value)

    return template