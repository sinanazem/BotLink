import json

def readjson(file_path):
    with open(file_path,'r') as f:
        return json.load(f)

def writejson(data, filename, indent=4):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=indent)

def writetxt(data, filename):
    with open(filename, 'a') as f:
        f.write(data)


def readtxt(filename):
    with open(filename) as f:
        data = f.read()
        return data