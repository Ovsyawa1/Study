import numpy as np
access = "Allowed"
notaccess = "Denied"
message = ""
a = np.random.randint(1,10)
if (a%2==0):
    message = (f"Access {access}")
else:
    message = (f"Access {notaccess}")
print (message)