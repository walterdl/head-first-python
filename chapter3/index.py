from os.path import exists

if not exists('sketch.txt'):
  print("The file doesn't exists. Terminating process")
  exit(1)

data = open('sketch.txt')

for each_line in data:
  try:
    role, line_spoken = each_line.split(':', 1)
    print(role, 'says', line_spoken)
  except:
    pass

data.close()