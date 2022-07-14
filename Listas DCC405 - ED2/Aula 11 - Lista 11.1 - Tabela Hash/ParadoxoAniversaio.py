def birthday(n):
    p = (1.0/365)**n
    for i in range((366-n),366):
        p *= i
    return 1-p