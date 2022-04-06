# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space,
# with and inserted before the last item. 
# 
# For example, passing the previous spam list to the function would
# return 'apples, bananas, tofu, and cats'. But your function should
# be able to work with any list value passed to it. Be sure to test
# the case where an empty list [] is passed to your function.


def spam(someList):
    # make sure list is not empty
    if bool(someList) == True:
        # create a list of strings
        stringList = [str(item) for item in someList]

        # replacing last item
        lastItem = stringList[-1]
        newLastItem = str(' and ' + lastItem)
        stringList.remove(lastItem)
        stringList.append(newLastItem)
        lastString = ', '.join(stringList)
        print(lastString)
    elif bool(someList) == False: 
        print('Empty list')

bacon = [1, 2, 3]
spam(bacon)

cheese = []
spam(cheese)


