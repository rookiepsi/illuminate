import commentjson

with open("themes/Illuminate-color-theme.json", "r") as file:
  data = commentjson.load(file)

with open("resources/colors.json", "r") as file:
  data_json = commentjson.load(file)

colors = []
colors_json = []
array = []

# Add color codes of the theme to colors[]
for value in data["colors"].values():
  if value not in colors:
    colors.append(value)

try:
  for i in range(0, len(data)):
    for value in data["tokenColors"][i]["settings"].values():
      if value[0] == "#":
        if value not in colors:
          colors.append(value)
except:
  pass

# Add color codes of colors.json to colors_json[]
for value in data_json:
  array.append(value)

for i in range(0, len(data_json)):
  for value in data_json[array[i]].values():
    if value[0] == "#":
      if value not in colors_json:
        colors_json.append(value)

# All elements of colors[] that are not present in colors_json[]
output = [x for x in colors if not x in colors_json or colors_json.remove(x)]
print("Missing colors in \033[33mcolors.json\033[0m:", output)

# All elements of colors_json[] that are not present in colors[]
output = [x for x in colors_json if not x in colors or colors.remove(x)]
print("Missing colors in the theme:", output)
