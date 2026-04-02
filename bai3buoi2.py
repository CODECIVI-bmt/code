def ve(cot, hang):
    if cot < 1 or hang < 1:
        print("chiu!")

    cacHang = "+" + (" -" * 4 + " +") * (cot - 1)
    cacCot = ("|" + " " * 9) * (cot - 1) + "|"

    print(cacHang)
    for _ in range(hang - 1):
        for _ in range(4):
            print(cacCot)
        print(cacHang)

print("3 hang x 3 cot :")
ve(3, 3)

print(" 4 hang x 4 cot:")
ve(4, 4)
      
      