def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)

  (mins, secs) = time_string.split(splitter)
  return(mins + '.' + secs)

class AthleteList(list):
  def __init__(self, name: str, dob: str = None, times: [str] = []):
    list.__init__([])
    self.name = name
    self.dob = dob
    self.extend(times)

  def top3(self) -> [str]:
    return str(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename) -> AthleteList:
  try:
    with open(filename) as f:
      data = f.readline()
      data = (data.strip().split(','))
      athlete = AthleteList(data.pop(0), data.pop(0), data)
      return athlete

  except IOError as ioerr:
    print('File error: ' + str(ioerr))

  return(None)

for athlete_file_name in ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']:
  athlete = get_coach_data(athlete_file_name)
  print(f'{athlete.name}\'s fastest time are: {athlete.top3()}')
