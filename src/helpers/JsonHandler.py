import json

def readJson(path):
    file = path.open()
    return list(json.load(file))

def updateJson(path, payload):
    try:
        print(json.dumps(payload))
        file = path.open('w')
        json.dump(payload, file, indent=2)
    except:
        raise
