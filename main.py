options = ["colorMap", "normalMap", "specColorMap"]
name = input("Nombre del fichero:\n")
prefix = input("Prefijo a añadir:\n")
file = open(name, "r")
text = ""
for line in file:
  if line.count("\"xmodel.gdf\"") or line.count("\"image.gdf\""):
    line = line[:line.index("\"")] + "\"" + prefix + "_" + line[1 + line.index("\""):]
  if line.count("\"filename\""):
    line = line[:14] + prefix + "\\\\" + line[14:]
  for opt in options:
    opt = "\"" + opt + "\""
    if line.count(opt) and line.index(opt) < 10:
      line = line[:len(opt) + 4] + prefix + "_" + line[len(opt) + 4:]
  if line.count("\"baseImage\" \"model_export"):
    index = line.index("model_export") + 14
    line = line[:index] + prefix + "\\\\" + line[index:]
  text += line
file.close()

with open(name, 'w') as file:
  file.write(text)