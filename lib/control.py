# This script connects to the Pylontech US2000B Plus
# and read the charge status, voltage, current, and temperature
# it stores the data in a .csv file with the actual date

from moxa_com import *
from mysql_write import *
import time




def control(SNMP_Host, SNMP_Version, SNMP_Community, SNMP_Port, SNMP_Device, Cadance, Display, SQL_Log, SQL_Host, SQL_Auth, SQL_User, SQL_Password, SQL_Database):




    try:

        print('PumpMonitor:1.0.0 ')

        # ---------------------------------------------------------------------------#
        # Establish communication to MOXA E1242
        MOXA = E1242()
        MOXA.open(SNMP_VERSION=SNMP_Version, SNMP_COMMUNITY=SNMP_Community, SNMP_HOST=SNMP_Host, SNMP_PORT=SNMP_Port, SNMP_DEVICE=SNMP_Device)
        tmp_b = MOXA.is_connected()
        print('MOXA Connection Established:' + str(tmp_b))
        # ---------------------------------------------------------------------------#

        # ---------------------------------------------------------------------------#
        # Connect to MySQL Server
        SQL= MySQL_com()
        SQL.open(HOST=SQL_Host,USER =SQL_User,PASSWORD=SQL_Password,DATABASE=SQL_Database,AUTH_PLUGIN=SQL_Auth)
        time.sleep(1)
        tmp_s = SQL.is_connected()
        print('SQL Server Connection Established:' + str(tmp_s))
        # ---------------------------------------------------------------------------#



        # ---------------------------------------------------------------------------#
        if not (tmp_b):  # Stopps program if connection has not been established.
            print('ERROR: No Connection to MOXA E1242')
            exit()
        if not (tmp_s):  # Stopps program if connection has not been established.
            print('ERROR: No Connection to SQL Server!')
            exit()
        # ---------------------------------------------------------------------------#



        # ---------------------------------------------------------------------------#
        try:  # Program Loop
            print('Start Monitoring Program!')
            time.sleep(1)
            while True:
                time.sleep(Cadance)

                if Control:  # Condition to Control Inverter Based on SoC
                    try:
                        Battery_SoC = PYLONTECH.read_SoC(N_MODULES=Battery_Modules)
                        Avg_SoC = 0
                        for i in range(len(Battery_SoC)):
                            Avg_SoC = Avg_SoC + Battery_SoC[i][0]
                        Avg_SoC = round(Avg_SoC / Battery_Modules)

                        if Avg_SoC >= SoC_high:  # Condition to enable Inverter Grid Support
                            if Inv.read_Load_Shave_Status() == 'Disable':
                                Inv.write_Load_Shave_Status('Enable')
                                print('Grid Support: ON')
                        if Avg_SoC <= SoC_low:  # Condition to disable Inverter Grid Support
                            if Inv.read_Load_Shave_Status() == 'Enable':
                                Inv.write_Load_Shave_Status('Disable')
                                print('Grid Support: OFF')
                    except:
                        error_counter_conext = error_counter_conext + 1
                        if runtime_error_conext(Inv, ERROR_COUNTER=error_counter_conext,
                                                MODBUS_ADDRESS=Modbus_Address_XW):
                            error_counter_conext = 0




                if SQL_Log:
                    try:
                        SQL.write_BMS(BMS_LIST=tmp_bms_log)
                        SQL.write_XW(XW_LIST=tmp_xw_log)
                        SQL.write_MPPT(MPPT_LIST=tmp_mppt_log)
                    except Exception as error:
                        print("SQL_Log error:", error)


                if Display:  # Condition to print the SoC in terminal
                    try:
                        tmp = PYLONTECH.read_SoC(N_MODULES=Battery_Modules)
                        print('A:' + str(tmp[0][0]) + '\t' + 'B:' + str(tmp[1][0]) + '\t' + 'C:' + str(tmp[2][0]) + '\t' + \
                              'D:' + str(tmp[3][0]) + '\t' + 'E:' + str(tmp[4][0]) + '\t' + 'F:' + str(tmp[5][0]) + '\t' \
                             +Inv.read_Inverter_Status())
                    except:
                        error_counter_conext=error_counter_conext+1
                        if runtime_error_conext(Inv,ERROR_COUNTER=error_counter_conext, MODBUS_ADDRESS=Modbus_Address_XW):
                            error_counter_conext=0





        except Exception as error:
            print("An error occurred:", error)




        except KeyboardInterrupt:
            try:
                del MOXA
                del SQL
                print('interrupted!')
            except:
                print('Monitoring Stop!')
            # ---------------------------------------------------------------------------#







    except KeyboardInterrupt:
        try:
            del MOXA
            del SQL
        except:
            print('Monitoring Stop!')

    except Exception as tmp_exeption:
        try:
            del MOXA

            del SQL
        except:
            print('Monitoring Stop! Exception'+tmp_exeption)