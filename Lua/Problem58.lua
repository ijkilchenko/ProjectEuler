max_n = math.pow(10,9)

--Make an eratosthenes sieve of primes. 
nums = {}
for i=1, max_n do
    nums[i] = i
end

for i=2, math.sqrt(#nums)+1 do
    if nums[i] ~= 0 then
        mul = 2
        p = i * mul
        while p < #nums do
            nums[p] = 0
            mul = mul + 1
            p = i * mul
        end
    end
end
--[[
for i=1, max_n do
    print(nums[i])
end
]]--

function is_prime(n)
    --A number i is prime iff a[i] != 0. 
    if nums[n] ~= 0 then
        return true
    else
        return false
    end
end

nums_prime_on_diagonal = 3
curr_side_length = 5
i = 13
j = 1
while i < max_n do
    if is_prime(i) then
        nums_prime_on_diagonal = nums_prime_on_diagonal + 1
    end    
    --If we just completed the outer layer of the box, i.e., if i is the lower right number. 
    if j % 4 == 0 then 
        nums_corners = curr_side_length*2 - 1
        if nums_prime_on_diagonal/nums_corners < 0.1 then
            print(i)
            print(curr_side_length)
            break
        end
        --[[
        print(i)
        print(curr_side_length)
        print(nums_prime_on_diagonal)
        print(nums_corners)
        print(nums_prime_on_diagonal/nums_corners)
        ]]--
    end
    
    i = i + (curr_side_length-1)
    if i > (curr_side_length)*(curr_side_length) then
        curr_side_length = curr_side_length +2 
        i = i + 2
    end
    j = j + 1
end

