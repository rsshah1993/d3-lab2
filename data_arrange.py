import json

f = open("movies_lab5.json", 'r')
f_read = f.read()
python_obj = json.loads(f_read)
