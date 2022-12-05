def mix(y, r):
    yy = len(y)
    rr = len(r)
    data = ""

    if len(y) < len(r):
        for yr in range(yy):
            data += y[yr] + r[yr]

        for yr in range(rr-yy):
            data += r[yr+yy]

        return data
    else:
        for ry in range(rr):
            data += y[ry] + r[ry]

        for ry in range(yy-rr):
            data += y[ry+rr]

        return data

w1 = str(input("Enter first word: "))
w2 = str(input("Enter second word: "))

print(f"Mixed word: {mix(w1, w2)}")
