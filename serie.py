#dmesg | grep "tty" to find port name
import serial,time,json,os
if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyUSB0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command (data): ")
                    arduino.write(cmd.encode())
                    #time.sleep(0.1) #wait for arduino to answer

                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0:
                        answer=str(arduino.readline())
                        print("---> {}".format(answer))
                        if cmd=="data":
                            dataList=answer.split("x")
                            print("Température : {} °C".format(dataList[1]))
                            temp = {
                                'température': dataList[1]
                            }
                            out_file = open("/home/user/temperature.json", "w")
                            json.dump(temp, out_file, indent = 6)
                            out_file.close()

                            isempty = os.stat('/home/user/temperature.json').st_size == 0
                            if isempty == False:
                                print("Température non écrite dans le fichier temperature.json")
                            else:
                                print("Température écrite dans le fichier temperature.json")
                            arduino.flushInput() #remove data after reading

            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
