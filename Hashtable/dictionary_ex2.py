
# program for getting key

a={
    1:4,
    2:2,
    3:3
}
def ju(val):
    for key,value in a.items():
        if val==value:
            print(key)
ju(4)




