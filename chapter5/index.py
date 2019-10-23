from typing import IO, Any

def get_firstline_as_list(file: IO[Any]) -> [str]:
  return file.readline().strip().split(',')

def sanitize(time_string: str) -> str:
  if '.' in time_string:
    return time_string

  time_string = time_string.replace('-', '.')
  time_string = time_string.replace(':', '.')
  return time_string

sanitize_list = lambda items_to_sanitize: [sanitize(x) for x in items_to_sanitize]

sanitizeFileContent = lambda fileContent: sanitize_list(get_firstline_as_list(fileContent))

try:
  with open('james.txt') as james, open('julie.txt') as julie, open('mikey.txt') as mikey, open('sarah.txt') as sarah:
    jamesList = sanitizeFileContent(james)
    julieList = sanitizeFileContent(julie)
    mikeyList = sanitizeFileContent(mikey)
    sarahList = sanitizeFileContent(sarah)

    unique_james_list = sorted(set(jamesList))
    unique_julie_list = sorted(set(julieList))
    unique_mikey_list = sorted(set(mikeyList))
    unique_sarah_list = sorted(set(sarahList))

    print('jamesList:', unique_james_list[0:3])
    print('julieList:', unique_julie_list[0:3])
    print('mikeyList:', unique_mikey_list[0:3])
    print('sarahList:', unique_sarah_list[0:3])
except IOError as error:
  print(f'There as an error procesing athletes records. Details: {error}')
