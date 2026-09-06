personas={12345678:"Juan",
          87654321: "Pepe",
          33333333: "Jose", 
          44444444: "Ale Marchena",
          55555555: "Jose"}
print(personas[12345678])
#claves: keys
#valores: values
#print(personas.keys())
#print(personas.values())
#print(personas.items())
#l1=[1,2,3,4]
#for n in l1:
#    print(n)
#for i in range(len(l1)):
#    print(l1[i])
dni_ale=44444444
for key in personas.keys():
    #print(key)
    if key==dni_ale:
        #print(personas[key])
        print("Marchena found")
    else:
        print("Marchena 404")
        
        