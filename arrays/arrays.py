#ARRAY / LIST MANIPULATION & EXPIRAMENTATION

"""def arr_practice():
    array = [1,2,3,4,5]
    print(array)
    #array manipulation
    
    #array POP - removes last item
    array.pop()
    print("POP: -removed (5)", array)

    #array APPEND -  add element to end of array
    array.append(6)
    print("APPENED: ", array)

    #array REMOVE - remove first item
    array.remove(1)
    print("REMOVE: ", array)

    #array INDEX -  retunr index of first occurence
    print( "INDEX: ", array.index(4))
    
   #array REVERSE - reverse order of array list
    array.reverse()
    print("REVERSED: ", array)

   #array SORT - sort array list
    array.sort()
    print("SORTED: ", array)

    #array INSERT - insert element at specific index
    array.insert(0, 1)
    array.insert(4, 5)

    #adding new insert number
    array.insert(7,7)
    array.insert(7,8)       

    print("INSERT: ", array)
"""
#PRACTICING ARRAY MANIPULATION
def veges_array():
    veges_array =["lettuce", "tomato" , "apple", "cucumber",]
    print(veges_array)
    
    veges_array.pop()
    print("POP: ", veges_array)
    
    veges_array.remove("apple")
    print("REMOVE: ", veges_array)
    
    veges_array.insert(2, "carrots")
    print("INSERT: ",veges_array)

    #veges_array.extend()

#PRACTICING MORE ARRAY MANIPULATION
def kitchenAppli():
        kitchenAppli = ["pots", "pans", "fork", "knife", "spoon"]
        print(kitchenAppli)

        kitchenAppli.pop()
        print("Pop: ", kitchenAppli)

        kitchenAppli.append("dish")
        print("Append: ", kitchenAppli)

#trying to fuse arrays
def houseList():
        houseList = [kitchenAppli(), veges_array()]
        print(houseList)
    

    
print(veges_array())
#print(arr_practice())
print("")
print(kitchenAppli())
print(houseList())


def main():
    #arr_practice
    veges_array
    kitchenAppli
    houseList

if __name__ == "__main__":
    main()
