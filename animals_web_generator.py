import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal['name']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    if 'type' in animal['characteristics']:
        type_ = animal["characteristics"]['type']
    else:
        type_ = False

    print("Name:", name)
    print("Diet:", diet)
    print("First location:", location)
    if type_:
        print("Type:", type_)
    print('\n')