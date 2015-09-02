f1 = 1
f2 = 2
sum = 2

while f1 + f2 <= 4000000 do
    tmp = f2
    f2 += f1
    f1 = tmp

    if f2.even?
        sum += f2
    end
end

puts sum 
