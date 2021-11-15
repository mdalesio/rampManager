#!../../bin/linux-x86_64/iocexample

#- You may have to change iocexample to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/iocexample.dbd"
iocexample_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords "db/dbAmplifier.db"

#- Set this to see messages from mySub
#var mySubDebug 1

#- Run this to trace the stages of iocInit
#traceIocInit

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncExample, "user=user"
