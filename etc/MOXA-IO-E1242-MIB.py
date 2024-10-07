#
# This file is part of MOXA E1242 SNMP communication for pysnmp software.
#
# Copyright (c) 2024, Alexander Pollak <Alexander.pollak.87@gmail.com>
#
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, snmpModules, ModuleIdentity, Counter64, ObjectIdentity, Integer32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, IpAddress, Gauge32, Unsigned32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "snmpModules", "ModuleIdentity", "Counter64", "ObjectIdentity", ">
TextualConvention, TestAndIncr, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "TimeStamp", "DisplayString")
snmpMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 1))
if mibBuilder.loadTexts: snmpMIB.setRevisions(('2000-08-09 20:17', '1995-11-09 00:00', '1993-04-01 00:00',))
if mibBuilder.loadTexts: snmpMIB.setLastUpdated('200008092017Z')
if mibBuilder.loadTexts: snmpMIB.setOrganization('IETF SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpMIB.setContactInfo('WG-EMail: snmpv3@tis.com Subscribe: majordomo@tis.com In message body: subscribe snmpv3 Chair: Russ Mundy TIS Labs at Network Associates postal: 3060 Washington Rd Glenwood MD 21738 USA EMail: mundy@tislabs.com phone: +1 301 854-6889 Editor: Randy Presuhn BMC Software, Inc. postal: 2141>
if mibBuilder.loadTexts: snmpMIB.setDescription('The MIB module for SNMP entities.')
snmpMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1))
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
if mibBuilder.loadTexts: sysDescr.setDescription("A textual description of the entity. This value should include the full name and version identification of the system's hardware type, software operating-system, and networking software.")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('current')
if mibBuilder.loadTexts: sysObjectID.setDescription("The vendor's authoritative identification of the network management subsystem contained in the entity. This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed. For example>
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setStatus('current')
if mibBuilder.loadTexts: sysUpTime.setDescription('The time (in hundredths of a second) since the network management portion of the system was last re-initialized.')
sysContact = MibScalar((1, 3, 6, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysContact.setStatus('current')
if mibBuilder.loadTexts: sysContact.setDescription('The textual identification of the contact person for this managed node, together with information on how to contact this person. If no contact information is known, the value is the zero-length string.')
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysName.setStatus('current')
if mibBuilder.loadTexts: sysName.setDescription("An administratively-assigned name for this managed node. By convention, this is the node's fully-qualified domain name. If the name is unknown, the value is the zero-length string.")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLocation.setStatus('current')
if mibBuilder.loadTexts: sysLocation.setDescription("The physical location of this node (e.g., 'telephone closet, 3rd floor'). If the location is unknown, the value is the zero-length string.")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysServices.setStatus('current')
if mibBuilder.loadTexts: sysServices.setDescription('A value which indicates the set of services that this entity may potentially offer. The value is a sum. This sum initially takes the value zero. Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L - 1) is added to the sum. For >
sysORLastChange = MibScalar((1, 3, 6, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORLastChange.setStatus('current')
if mibBuilder.loadTexts: sysORLastChange.setDescription('The value of sysUpTime at the time of the most recent change in state or value of any instance of sysORID.')
sysORTable = MibTable((1, 3, 6, 1, 2, 1, 1, 9), )
if mibBuilder.loadTexts: sysORTable.setStatus('current')
if mibBuilder.loadTexts: sysORTable.setDescription('The (conceptual) table listing the capabilities of the local SNMP application acting as a command responder with respect to various MIB modules. SNMP entities having dynamically-configurable support of MIB modules will have a dynamically-varying number of conceptual rows.')
sysOREntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 9, 1), ).setIndexNames((0, "SNMPv2-MIB", "sysORIndex"))
if mibBuilder.loadTexts: snmpObsoleteGroup.setDescription('A collection of objects from RFC 1213 made obsolete by this MIB module.')
mibBuilder.exportSymbols("SNMPv2-MIB", snmpOutBadValues=snmpOutBadValues, coldStart=coldStart, snmpOutPkts=snmpOutPkts, snmpSilentDrops=snmpSilentDrops, snmpCommunityGroup=snmpCommunityGroup, sysORLastChange=sysORLastChange, sysName=sysName, snmpBasicNotificationsGroup=snmpBasicNotificationsGroup, systemGroup=systemGroup, snmpInNoSuch>

