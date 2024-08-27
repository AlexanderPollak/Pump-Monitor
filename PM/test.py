
from pysnmp.hlapi.v3arch.asyncio import *
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

with Slim(1) as slim:
    errorIndication, errorStatus, errorIndex, varBinds = await
    slim.get('public', '192.168.0.216', '161', ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)), )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "{} at {}".format(
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            print(" = ".join([x.prettyPrint() for x in varBind]))