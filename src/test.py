def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocaxl"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()