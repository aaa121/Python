# NESTED IF Statement for Confusion Matrix
predicted=int(input("Enter the Predicted Signal Occurence, either True (1) or False (0):"))
actual=int(input("Enter the Actual Signal Occurence, either True (1) or False (0):"))
if predicted ==1:
    if actual == 1:
        print("True Positive")
    else:
        print("False Positive")
elif predicted == 0:
    if actual == 0:
        print("True Negative")
    else:
        print("False Negative")
else:
    print("Wrong Input value. Enter either 1 or 0")