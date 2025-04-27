//It is just a memory test

Termemorytesting = ["null"]
print ("Test Reeji the system")
while (0 == 0):
  Firsttest = str(input("Input anything so it'll be saved to memory"))
  if ("null" in Termemorytesting):
    Termemorytesting.remove(Termemorytesting[0])
  Termemorytesting.append(Firsttest)
  print (Termemorytesting)
