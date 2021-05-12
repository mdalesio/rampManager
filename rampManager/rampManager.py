from p4p.client.thread import Context
import pandas as pd
import time, os, re

path = os.path.abspath(os.path.dirname(__file__))
ctxt = Context('pva')

cols = [x for x in range(0,12)]
lPVs = ["amplifier{0}".format(x) for x in range(1,11)]

xlsx_files = [f for f in os.listdir(path) if re.match('.*\.xls.*', f)]
print("Which schedule would you like to use?")
response = None
while response not in xlsx_files:
        response = input("Please choose from the following {0}: ".format(xlsx_files))
infile = path + "/" + response
df = pd.read_excel(infile, header=1, usecols=cols)
# print (df)

while True:
    for event in df.index:
        print("Event: {0}".format(event))
        for pv in lPVs:
            print("{0}: {1}".format(pv, df.loc[event][pv]))
            ctxt.put(pv, df.loc[event][pv])
        print("Sleep: {0}".format(df.loc[event]["TIME"]))
        time.sleep(df.loc[event]["TIME"])
