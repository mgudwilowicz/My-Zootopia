import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''  # define an empty string
for animal_data in animals_data:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
    output += f"Location: {animal_data['locations'][0]}\n"
    if 'type' in animal_data['characteristics']:
        output += f"Type: {animal_data['characteristics']['type']}\n"
    output += f"\n"

print(output)
with open("animals_template.html", "r") as f:
    html_template = f.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(html_output)