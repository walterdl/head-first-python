import pickle
from athletelist import AthleteList

def get_coach_data(filename):
  try:
    with open(filename) as f:
      data = f.readline()
      data = (data.strip().split(','))
      athlete = AthleteList(data.pop(0), data.pop(0), data)
      return athlete

  except IOError as ioerr:
    print('File error: ' + str(ioerr))

  return(None)

athletes_store_filename = 'athletes_store.txt'

def put_to_store(files_list):
  athletes = dict()

  for file_name in files_list:
    athlete = get_coach_data(file_name)
    athletes[athlete.name] = athlete

  with open(athletes_store_filename, mode='wb') as store_file:
    pickle.dump(athletes, file=store_file)

  return athletes

def get_from_store():
  all_athletes = dict()

  with open(athletes_store_filename, 'rb') as store_file:
    all_athletes = pickle.load(store_file)

  return all_athletes

returned = get_from_store()
print('returned', returned)