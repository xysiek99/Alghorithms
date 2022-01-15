# Alghorithm 6
# { 𝑛∈ℕ∧𝑛>0}
# while(n<>1) do begin 
# if(n parzysta) n:= n/2;
# else n:= 3*n+1;end;
n = 12

while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    print(int(n))
    
