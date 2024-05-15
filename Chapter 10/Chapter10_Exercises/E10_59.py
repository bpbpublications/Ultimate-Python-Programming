def func():
    func.count += 1


func.count = 0

func()
func()
func()

print(func.count)
