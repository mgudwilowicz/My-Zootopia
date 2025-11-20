import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''  # define an empty string
for animal_data in animals_data:
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>  {animal_data['name']}</div>"
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_data['characteristics']['diet']}<br/>"
    output += f"<strong>Location</strong>: {animal_data['locations'][0]}<br/>"
    if 'type' in animal_data['characteristics']:
        output += f"<strong>Type:</strong> {animal_data['characteristics']['type']}<br/>"
    output += '</p>'
    output += '</li>'

print(output)

with open("animals_template.html", "r", encoding="utf-8") as f:
    html_template = f.read()
html_template = html_template.replace(
    "<head>",
    "<head>\n    <meta charset=\"UTF-8\">"
)

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(html_output)