from p4p.client.thread import Context
import pandas as pd
import time

ctxt = Context('pva')
infile = "gauss.xlsx"
cols = [x for x in range(0,12)]
lPVs = ["amplifier{0}".format(x) for x in range(1,11)]

df = pd.read_excel(infile, header=1, usecols=cols)
# print (df)

for event in df["EVENT"]:
    print("Event: {0}".format(event))
    for pv in lPVs:
        print("{0}: {1}".format(pv, df.loc[event][pv]))
        ctxt.put(pv, df.loc[event][pv])
    print("Sleep: {0}".format(df.loc[event]["TIME"]))
    time.sleep(df.loc[event]["TIME"])
