def sum(a,b,count=0):
        if a == 0:
            return b
        else:
            return 2 + sum(a-1, b-1)

