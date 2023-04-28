n = int(input("Enter the length of reference string: "))
rs = list(map(int, input("Enter the reference string: ").split()))
f = int(input("Enter the number of frames: "))
m = [-1]*f
pf = 0
count = 0
print("The Page Replacement Process is:\n")
for i in range(n):
    k = 0
    while k < f:
        if m[k] == rs[i]:
            break
        k += 1
    if k == f:
        m[count] = rs[i]
        count = (count+1) % f
        pf += 1
    print("\t".join(str(page) if page != -1 else '-' for page in m), end="")
    if k == f:
        print("\tPF No.", pf)
    else:
        print()
print("\nThe number of Page Faults using FIFO are", pf)
