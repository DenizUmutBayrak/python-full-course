# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

x = 3

func1()
func2()

# Local -> Global so the values are 1 and 2
# Built-in = variables which is in the libraries