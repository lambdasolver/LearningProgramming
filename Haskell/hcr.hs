f :: Int -> Int 
f n 
    | n < 10    = fact n 
    | otherwise = fact(n `mod` 10) + f (n `div` 10)

fact :: Int -> Int 
fact 0 =1
fact n = n * fact (n-1)

s :: Int -> Int 
s n = n `mod` 10 + s (n `div` 10)

g :: Int -> Int 
g n = g' 1 n 
    where g' i n
            | s(f i) == n  = i
            | otherwise     = g' (i+1) n