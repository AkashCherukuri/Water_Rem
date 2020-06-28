import pickle

def Default():
    saved = {"Alarm_Time": 30,"Tune": "Rick.wav"}
    return saved

def Load(name):
    try:
        saved = pickle.load(open("settings.pkl", "rb"))
    except (OSError, IOError) as e:
        print(f"No pickle found while loading.")
        saved = Default()

    return saved[name]

def Save(name, value):
    try:
        saved = pickle.load(open("settings.pkl", "rb"))
    except (OSError, IOError) as e:
        print(f"No Pickle found while saving.")
        saved = Default()
 
    saved[name] = value
    pickle.dump(saved, open("settings.pkl", "wb"))