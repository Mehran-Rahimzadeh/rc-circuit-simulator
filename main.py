# RC Cercuite simulator
import os
os.system("cls" if os.name =="nt" else "clear")


resistance = 1000     #resistance(ohm)
capacitance = 0.0001    #capacitor (Faraday)

time = resistance * capacitance     #equation to calculate 


print("RC Circuit Simulator \n")
print ("The capacitor value: " + str(capacitance * 10**6) + " μF")
print ("The Resistant value: " + str(resistance) + " Ωn\n")
print ("The caculated time_constant is: " + str(time)+ " s\n")
