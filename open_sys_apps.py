import os

def open_apps(query):
    if "notepad" or "नोटपॅड"in query:
        os.system("start notepad")
    elif "calculator" or "कॅल्कुलेटर"in query:
        os.system("start calc")
    elif "browser" or "ब्राऊजर"in query:
        os.system("start brave")
    else:
        print("Sorry, I don't know how to open that application.")

# open_apps("browser ughad")