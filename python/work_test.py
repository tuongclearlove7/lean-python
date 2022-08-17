def app():
    combs = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                combs.append((x, y))
    print(combs)
    while True:
        try:
            key = input("nhap pass : ")
            k = {'tuong': lambda:app()}[key]()
            break;
        except:
            print(False)






