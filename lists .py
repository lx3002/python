# lists are used to store multiple items
shoppingbasket = ['kales', 'booze', 'beer', 'beef', 'barley', 'flour']
#
# feature with lists they can be changed ordered chngaableand duplicate values
# lists are indexed: counting starts from zero
# lists are odered changeable and allow duplicate values
# list items can be acceessed added removed and changed
# accessing thingin basket
print(shoppingbasket[0])
print(shoppingbasket[2:5])
print(shoppingbasket[-4:-2])
print(shoppingbasket[0:6])

# chekin items in alist

x = input('check for this item')
if x in shoppingbasket:
    print(x + 'available in basket')
else:
    print(x + 'unavailable in basket')


    #changing list items

''
shoppingbasket[3] = 'paste'
shoppingbasket[4] = ' magerine'
shoppingbasket[5] = 'fish'
shoppingbasket[6] = 'soap'
print(shoppingbasket)

shoppingbasket[1:4] = []
shoppingbasket.insert(0, 'spinach')
print(shoppingbasket)
shoppingbasket.append('lube')# adds  items to the end
toolshopping = ['hammers', 'pliers', 'nails']
shoppingbasket.extend(toolshopping)# adds items to another
print(shoppingbasket)
#how to remove
#1. remove
shoppingbasket.remove()
print(shoppingbasket)
shoppingbasket.pop()
print()
shoppingbasket.clear()
print(shoppingbasket)
del shoppingbasket
print(shoppingbasket)





