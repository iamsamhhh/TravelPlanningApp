from sqlitedict import SqliteDict

# Save data using a key to a SQLite database
def save(key, value, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value # Store the value using the key
            mydict.commit() # Commit to flush the data to disk
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)

# Retrieve stored data using the key from the SQLite database
def load(key, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key] # Retrieve the value using the key
        return value
    except Exception as ex:
        print("Error during loading data:", ex)

def UserExist(key):
    try:
        with SqliteDict("data.sqlite3") as mydict:
            for i in mydict.keys():
                if i == key:
                    return True
            return False
    except Exception as ex:
        print("Error during searching data:", ex)