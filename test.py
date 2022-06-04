#range(5) ----> [0,1,2,3,4]
# n =int (input('How many times do you want to repet the message)) 

#for i in range(n):
#    print (f"Hello world! {i}")

elements= ["a","b","c","a"]

print(elements[0])

#range(4) ---> [0,1,2,3]
print("Slower form")
for i in range(4):
    print(elements[i])

print("Cooler form")
for e in elements: 
    print(e)

me= {
    "first": "Astrid",
    "last": "Batres-Guerrero",
    "age": 24,
    
}

print(me["first"])