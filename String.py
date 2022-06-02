#app.py
def stringToList(string):
    listRes = list(string.split(""))
    return listRes

strA = "Bryan Adams Brown"
print(stringToList(strA))