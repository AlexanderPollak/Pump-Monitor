""" This script converts a plain text MIB for E1242 Moxa into a mib.py for pysnmp.

**Description:**
    This script takes the plain text mib and uses pysmi to create a python mib file that pysnmp can
    use to read registers for specific devices. In this case MOXA E1242.

"""

from pysnmp.smi import builder, view, compiler, error
from pysnmp import debug

debug.setLogger(debug.Debug('dsp'))

# Create MIB loader/builder
mibBuilder = builder.MibBuilder()

# Optionally attach PySMI MIB compiler (if installed)
print('Attaching MIB compiler...'),
compiler.addMibCompiler(mibBuilder, sources=['/usr/local/lib/python3.10/dist-packages/pysnmp/smi/mibs', 'http://mibs.snmplabs.com/asn1/'])
print('done')

# Optionally set an alternative path to compiled MIBs
print('Setting MIB sources...')
mibBuilder.addMibSources(builder.DirMibSource('/usr/local/lib/python3.10/dist-packages/pysnmp/smi/mibs'))
print(mibBuilder.getMibSources())
print('done')

print('Loading MIB modules...'),
mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-FRAMEWORK-MIB', 'SNMP-COMMUNITY-MIB', 'IP-MIB')
print('done')

print('Indexing MIB objects...'),
mibView = view.MibViewController(mibBuilder)
print('done')

print('MIB symbol name lookup by OID: '),
oid, label, suffix = mibView.getNodeName((1,3,6,1,4,1))
print(oid, label, suffix)

print('MIB symbol name lookup by label: '),
oid, label, suffix = mibView.getNodeName((1,3,6,1,4,1,'mib-2',1,'sysDescr'))
print(oid, label, suffix)

print('MIB symbol name lookup by symbol description: '),
oid, label, suffix = mibView.getNodeName(('sysDescr',))
oid, label, suffix = mibView.getNodeName(('snmpEngineID',), 'SNMP-FRAMEWORK-MIB')
print(oid, label, suffix)

print('MIB object value pretty print: '),
mibNode, = mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB', 'snmpEngineID')
print(mibNode.syntax.prettyPrint())

print('MIB symbol location lookup by name: '),
modName, symName, suffix = mibView.getNodeLocation(('snmpCommunityEntry',))
print(symName, modName)

print('MIB node lookup by location: '),
rowNode, = mibBuilder.importSymbols(modName, symName)
print(rowNode)

print('Conceptual table index value to oid convertion: '),
oid = rowNode.getInstIdFromIndices('router')
print(oid)
print('Conceptual table index oid to value convertion: '),
print(rowNode.getIndicesFromInstId(oid))

print('MIB tree traversal')
oid, label, suffix = mibView.getFirstNodeName()
while 1:
    try:
        modName, nodeDesc, suffix = mibView.getNodeLocation(oid)
        print('%s::%s == %s' % (modName, nodeDesc, oid))
        oid, label, suffix = mibView.getNextNodeName(oid)
    except error.NoSuchObjectError:
        break

print('Modules traversal')
modName = mibView.getFirstModuleName()
while 1:
    if modName: print(modName)
    try:
        modName = mibView.getNextModuleName(modName)
    except error.SmiError:
        break
