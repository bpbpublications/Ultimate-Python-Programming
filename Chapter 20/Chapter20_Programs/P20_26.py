try:
    file = open('data.txt')
    try:
        x = file.readlines()
        print(x)
    except Exception as e:
        print(type(e))
        print(e)
    finally:
        file.close()
except FileNotFoundError as e:
    print(e)
