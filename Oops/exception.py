try:
    print("Enter the net sales for")

    previous=float(input("- Prior period:"))
    current=float(input("- Current period"))

    change=(current-previous)*100/previous

    if change>0:
        res=f"Sales increase {abs(change)}%"
    else:
        res=f"sales decrease {abs(change)}"
    
    print(res)    
except ValueError:
    print("Error! please enter a nummber for net sales")
except ZeroDivisionError:
    print("Error! The prior net sales cannot be zero")
except Exception as error:
    print(error)
