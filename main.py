try:
   while True:
    kills = input("Enter kills:")
    print("kills are: " + str(kills)) 

    kd = input("Enter kd:")
    print("kd is: " + str(kd)) 

    deaths = float(kills)*(1/float(kd))
    print("deaths are " + str(deaths))       
except KeyboardInterrupt:
    print("\n -Program Ending- ")



