class private_App:

    def app():

        data = [] # private data

        def set(*value):

            data.append(value)

        def get(index):

            return data[index]
        
        def gets():

            index = 0

            for i in data[index]:

                print(i)

        def edit_dict(index,key,value):
            
            data[index][index][key] = value

        set({"me" : "","crush" : ""},{},dict(),[])
        print(get(0))
        edit_dict(0,"me","tuong")
        edit_dict(0,"crush","thao")
        print(get(0))
        gets()
        
        for i in get(0)[0]:

            print(get(0)[0][i])

def main():

    private_App.app()

main()