TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += iocexampleSupport

# Compile and add code to the support library
iocexampleSupport_SRCS += xxxRecord.c
iocexampleSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application, that
# causes problems on Windows DLL builds
iocexampleSupport_SRCS += dbSubExample.c
iocexampleSupport_SRCS += deviocexampleVersion.c
iocexampleSupport_SRCS += iocexampleHello.c
iocexampleSupport_SRCS += initTrace.c

iocexampleSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Auto-generate a header file containing a version string.
# Version comes from the VCS if available, else date+time.
GENVERSION = iocexampleVersion.h
# Macro name
GENVERSIONMACRO = iocexampleVERSION

# Build the IOC application
PROD_IOC = iocexample

# iocexample.dbd will be created and installed
DBD += iocexample.dbd

# iocexample.dbd will include these files:
iocexample_DBD += base.dbd
iocexample_DBD += xxxSupport.dbd
iocexample_DBD += dbSubExample.dbd
iocexample_DBD += deviocexampleVersion.dbd
iocexample_DBD += iocexampleHello.dbd
iocexample_DBD += initTrace.dbd

# iocexample_registerRecordDeviceDriver.cpp derives from iocexample.dbd
iocexample_SRCS += iocexample_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
iocexample_SRCS_DEFAULT += iocexampleMain.cpp
iocexample_SRCS_vxWorks += -nil-

# Link in the code from our support library
iocexample_LIBS += iocexampleSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into iocexampleSupport
    sncExample_SNCFLAGS += +r
    iocexample_DBD += sncExample.dbd
    # A .stt sequence program is *not* pre-processed:
    iocexampleSupport_SRCS += sncExample.stt
    iocexampleSupport_LIBS += seq pv
    iocexample_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    # A .st sequence program *is* pre-processed:
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    iocexample_LIBS += qsrv
    iocexample_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    iocexample_DBD += PVAServerRegister.dbd
    iocexample_DBD += qsrv.dbd
endif

# Finally link IOC to the EPICS Base libraries
iocexample_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

# Explicit dependency needed for generated header file
deviocexampleVersion$(DEP): $(COMMON_DIR)/$(GENVERSION)
