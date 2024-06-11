"""Bảng cửu chương"""
print("Bảng cửu chương")
for i in range(1,11,1):
    for j in range(2,10,1):
        if len(str(f"{j}x{i}={i*j}")) == 5 :
            print(f"{j}x{i}={i*j}   ", end=" ")
        elif len(str(f"{j}x{i}={i*j}")) == 6:
            print(f"{j}x{i}={i*j}  ", end=" ")
        else:
            print(f"{j}x{i}={i * j} ", end=" ")
    print("\n")

