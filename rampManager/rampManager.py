from p4p.client.thread import Context
import pandas as pd
import time

ctxt = Context('pva')
infile = "gauss.xlsx"
cols = [x for x in range(0,11)]

df = pd.read_excel(infile, header=1, index_col="EVENT", usecols=cols)
# print (df)

def ramp(event):
    print("Event: {0}".format(event))
    for pv in df:
        print("{0}: {1}".format(pv, df.loc[event][pv]))
        ctxt.put(pv, df.loc[event][pv])

sub = ctxt.monitor('eventcount', ramp)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	sub.close()
	("Keyboard Interrupted")
	pass
