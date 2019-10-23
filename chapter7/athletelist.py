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