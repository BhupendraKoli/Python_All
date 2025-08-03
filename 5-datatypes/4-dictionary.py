# Dictionary{}
'''
dictiinary is collection of uniqe data
it is mutable
it is ordered after python 3.6
is a indexed (keys are indexes)
key should be unique
are collection of key value pair ,are creatde using curely brackets {}
duplicat allow only value 
duplicate key is not allows
'''
# # Creating a dictionary
# person = {"name": "John", "age": 30, "city": "New York"}
# print(person["name"])  # Output: John
# print(type(person))
# print(person["age"])


# d={"a":45,"b":89,"c":55}
# print(d)
# print(type(d))
# # we can store duplicate value 
# d={"a":45,"b":89,"c":55,"d":45}
# print(d)

# # key is unique
# d={"a":45,"a":89,"c":55,"d":45}
# print(d)


# # how to fetch vlaue by using accessing a key
# d={"mango":89,"bananan":56,"lichi":34}
# print(d["mango"])
# # using get method 
# print(d.get("lichi"))

# print(d["lichi"])
# print(d.get("lic"))

# # how to iterate a dictionary
# d={"mango":89,"bananan":56,"lichi":34}
# for i in d :
#     print(i," ",d[i]) 


# d={"mango":89,"bananan":56,"lichi":34}
# for i in d :
#     print(i) #mango bananan lichi



# .item convert the dictionary into list of tuple 
# d={"mango":89,"bananan":56,"lichi":34}
# print(d.items()) #dict_items([('mango', 89), ('bananan', 56), ('lichi', 34)])


# for key,val in d.items():
#     print(key,val) #mango 89  bananan 56

# d={1:11,2:22,3:33,4:44}
# for i in d :
#     print(i,";",d[i]) 

# # if i want to print all keys 

# d={"mango":89,"bananan":56,"lichi":34}
# print(d.keys()) #dict_keys(['mango', 'bananan', 'lichi'])
# print(d.values())   #dict_values([89, 56, 34]) 

# # modifaction 
# d={"mango":89,"bananan":56,"lichi":34}
# d["mango"]=900
# print(d) # {'mango': 900, 'bananan': 56, 'lic


# d={"mango":89,"bananan":56,"lichi":34}
# d["mangoes"]=900
# print(d) # {'mango': 89, 'bananan': 56, 'lichi': 34, 'mangoes': 900}

# # update
# d={"mango":89,"bananan":56,"lichi":34}
# d.update({"graps":900,"jamun":1000})
# print(d) # {'mango': 89, 'bananan': 56, 'lichi': 34, 'graps': 900, 'jamun': 1000}

# d1={"mango":89,"bananan":56,"lichi":34}
# d2={"graps":90,"kivi":100}
# d1.update(d2)
# print(d1) # {'mango': 89, 'bananan': 56, 'lichi': 34, 'graps': 90, 'kivi': 100}

# # setdefult() 
# d1={"mango":89,"bananan":56,"lichi":34}
# d1.setdefault("mango",600)
# print(d1) # {'mango': 89, 'bananan': 56, '
# d1.setdefault("kivi",600)
# print(d1) # {'mango': 89, 'bananan': 56, 'lichi': 34, 'kivi': 600}


# #c deletion method :
# # pop():- it will remove the element of specified key 
# d={"mango":89,"bananan":56,"lichi":34}
# d.pop("mango")
# print(d) # {'bananan': 56, 'lichi': 34}

# # popitems() delete the last item key value pair 
# d1={"mango":89,"bananan":56,"lichi":34}
# d1.popitem()
# print(d1) # {'mango': 89, 'bananan': 56, '}

# del d1["mango"]
# d1.clear()
# print(d1) # {}
# 1.Create a dictionary of three countries and their capitals. Print all the keys.
d1={"india ":"New Delhi","japan":"Tokyo","china":" Beijing"}
print(d1.keys()) #dict_keys(['india ', 'japan', 'china'])

# 2.fruit_prices = {"apple": 100, "banana": 40, "cherry": 150}
#   --Print all values.
#   -- Use .get() to find the price of "banana".
fruit_prices = {"apple": 100, "banana": 40, "cherry": 150}
print(fruit_prices.values())
print(fruit_prices.get("banana"))

# 3.Update the price of "apple" to 120. Then add a new fruit "orange" with price 80.
fruit_prices = {"apple": 100, "banana": 40, "cherry":150}
fruit_prices["apple"]=120
fruit_prices["orange"]=80

print(fruit_prices) # {'apple': 120, 'banana': 40, 'ch
# 4.Use .items() to loop through the fruit_prices dictionary and print each item as Fruit: Price.
fruit_prices = {"apple": 100, "banana": 40, "cherry":150}
for key,val in fruit_prices.items():
    print(f"{key}:{val}") 

# 5.Remove "banana" using .pop(). What’s left in the dictionary, print it.
fruit_prices = {"apple": 100, "banana": 40, "cherry":150}
fruit_prices.pop("banana")
print(fruit_prices) # {'apple': 100, 'cherry': 150}



car={"model":"top","year":2024,"brand":"TATA","color":["red","yellow","black","green"]}
#print colot red
print(car["color"][0]) # red
# print i like Tata in black color
print(f"I like {car['brand']} in {car['color'][2]} color") #
brand = car["brand"]
clr = car["color"][2]
print(f"I like {brand} in {clr} color.")

phone = {"brand": "Samsung", "model": "Galaxy S23", "colors": ["black", "white", "blue"]}
print(f"My favorite phone is  {phone['brand']} in {phone['colors'][1]} color")

brand = phone["brand"]
clr = phone["colors"][1]
print(f"my favorrite phone is  {brand} in {clr} color.")

# create a dictionary using two list
list1=[1,2,3,4,5]
list2=["jeh","vitat","lina","komal","mariya"]
d={}
for i in range(len(list1)):
    d[list1[i]]=list2[i]
print(d)

#using zip function 
list1=[1,2,3,4,5]
list2=["jeh","vitat","lina","komal","mariya"]
d=dict(zip(list1,list2))
print(d)


