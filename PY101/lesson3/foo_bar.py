def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")


print(bar(foo()))

# bar("yes")

# False and "yes" or "no"
# False and "yes" 
# Final -> False