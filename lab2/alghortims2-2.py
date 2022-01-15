# Alghorithm 2
# { 𝑛∈ℕ∧𝑛>0∧𝑛 podzielna przez 3}
# while(n<>153) do n:= suma sześcianów cyfr liczby n;
n = 30

while n != 153:
    n_string = str(n)
    new_n = 0
    for i in str(n):
        new_n += int(i)**3
    n = new_n
    print(n)    