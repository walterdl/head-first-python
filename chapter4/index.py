from os import chdir
from nester import print_recursively_lists
import pickle

chdir('../assets')

man = []
other = []
dataFileName = 'sketch.txt'

try:
  with open(dataFileName) as data:
    for each_line in data:
      if each_line.find(':') == -1: # The current line hasn't the separator
        continue

      role, line_spoken = each_line.split(':', 1)
      line_spoken = line_spoken.strip()
      _role = role.lower()

      if _role == 'man':
        man.append(line_spoken)
      elif _role == 'other man':
        other.append(line_spoken)

    print('The man', man)
    print('The others', other)
except IOError as err:
  print(f'IOError spotted while reading spoken lines. Terminating process. Details: {err}')

try:
  with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
    pickle.dump(man, file=man_file)
    pickle.dump(other, file=other_file)
except IOError as error:
  print('IOError spotted while writing spoken lines. Terminating process. Details', str(error))
except pickle.PickleError as error:
  print('PickleError spotted while writing spoken lines. Terminating process. Details', str(error))
# finally:
#   man_file.close()
#   other_file.close()