# Alghorithm 1
# { 𝑛∈ℕ ∧ 𝑛>0 }
# while((n<>4) and(n<>1)) do n:= suma kwadratów cyfr liczby n; 
n = 1618
a = 1

while n != 1 and n!= 4:
    print(f"Iteration: {a}")
    n_string = str(n)
    new_n = 0
    for i in str(n):
        new_n += int(i)**2
    n = new_n
    print(n)
    a += 1