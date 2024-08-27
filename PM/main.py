#START OF MAIN:

import configparser
from moxa_com import *
from mysql_write import *


def main():
    
    # Import PM gonfiguration values from pm.cfg file in etc directory
    config = configparser.ConfigParser()
    config.read('/usr/local/pump-monitor/etc/pm.cfg') # Location of config file

    # Parse values into the main function.

    # Communication settings to connect to the Moxa E1242 module.
    SNMP_Host = config.get('COMMUNICATION SETTINGS','SNMP_Host')  # IP Address of the Moxa Module
    SNMP_Version = config.get('COMMUNICATION SETTINGS','SNMP_Version')  # SNMP Version
    SNMP_Community = config.get('COMMUNICATION SETTINGS','SNMP_Community') # SNMP Community String
    SNMP_Port = config.get('COMMUNICATION SETTINGS','SNMP_Port') # SNMP Port

    # General settings for pump monitor program
    Cadance = config.getint('GENERAL MONITOR SETTINGS','Cadance')  # Monitor refresh rate in seconds
    Display = config.getboolean('GENERAL MONITOR SETTINGS','Display') # Enable Terminal Print
    SQL_Log = config.getboolean('GENERAL MONITOR SETTINGS','SQL_Log') # Enable BMS logging into SQL

    # Specific variables for the SQL database writer

    SQL_Host = config.get('MySQL SPECIFIC SETTINGS','SQL_Host')  # MySQL server address
    SQL_Auth = config.get('MySQL SPECIFIC SETTINGS','SQL_Auth')  # MySQL authentication method
    SQL_User = config.get('MySQL SPECIFIC SETTINGS','SQL_User')  # MySQl username
    SQL_Password = config.get('MySQL SPECIFIC SETTINGS','SQL_Password')  # MySQl user password
    SQL_Database = config.get('MySQL SPECIFIC SETTINGS','SQL_Database')  # MySQL database


    ################################################################################################################


    print('\n Current Configuration of Pump Monitor Program \n')
    print('Monitor Cadance: ' + str(Cadance))
    print('\n')
    print('Control- Display:' +str(Display))
    print('Control- SQL Data Log:' + str(SQL_Log))

    query_community(version=SNMP_Version,community=SNMP_Community,host=SNMP_Host,port=SNMP_Port)

#   control(Serial_Port=Serial_Port, Modbus_Host=Modbus_Host, Modbus_Address_XW=Modbus_Address_XW, Modbus_Address_MPPT_West=Modbus_Address_MPPT_West,\
#         Modbus_Address_MPPT_East=Modbus_Address_MPPT_East, Battery_Modules=Battery_Modules, Cadance=Cadance,\
#         Display=Display, CSV_Log=CSV_Log,SQL_Log=SQL_Log, Control=Control, SoC_high=SoC_high, SoC_low=SoC_low,\
#         Battery_low=Battery_low, Battery_hysteresis=Battery_hysteresis,Default_battery_low=Default_battery_low,\
#         Default_battery_hysteresis=Default_battery_hysteresis, Log_file_path=Log_File_Path,\
#         SQL_Host=SQL_Host,SQL_Auth=SQL_Auth, SQL_User=SQL_User,SQL_Password=SQL_Password,SQL_Database=SQL_Database)


if __name__ == '__main__':

    main()


