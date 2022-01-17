{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Data.List ( intercalate )
import Data.Array ( Ix, Array, (!), listArray )

data Tree a = Nil | Node (Tree a) a (Tree a)
instance Show a => Show (Tree a) where
        show t = intercalate "\n"  (map snd (draw t))
        

draw :: Show a => Tree a -> [(Int,String)]
draw Nil                = [(1,"*")]
draw (Node Nil x Nil)   = [(1,show x)]
draw (Node tl x tr)     = zip (repeat 0) (map shiftl (draw tl)) ++ [(1,show x ++ "-+")] ++ zip (repeat 2) (map shiftr (draw tr)) where
        shiftl (0,x)    =       spaces ++ "  " ++ x 
        shiftl (1,x)    =       spaces ++ "+-" ++ x 
        shiftl (2,x)    =       spaces ++ "| " ++ x 
        shiftr (0,x)    =       spaces ++ "| " ++ x 
        shiftr (1,x)    =       spaces ++ "+-" ++ x 
        shiftr (2,x)    =       spaces ++ "  " ++ x
        spaces          =       replicate  (length (show x)+1) ' '
vanNickSequence :: Int -> Int
vanNickSequence n = vnkarr!n where
        vnkarr :: Array Int Int
        vnkarr = listArray (0,n) [f i | i <- [0..n]]
        f 0 = 5
        f i
         | g (vnkarr!(i-1))     = i
         | otherwise            = vnkarr!(i-1) + 2
        g m = m `mod` 5 == 0

tuples :: [[a]] -> [[a]]
tuples [] = [[]]
tuples (xs:xss) = [y:ys|y <- xs, ys <- tuples xss]

createTree :: [a] -> Tree a
createTree []   = Nil
createTree xs    = Node
    (createTree front) x (createTree back) where
        n = length xs
        (front, x:back) = splitAt (n `div` 2) xs

queens :: Int -> [[Int]]
queens n = qArr!n where
        qArr = listArray (1,n) [f i | i <- [1..n]]
        f 1 = makelsList n
        f i = concatMap (extend n)  (qArr!(i-1))
        extend n xs = [xs++[k] | k <- [1..n], validOpt k (length xs+1) 1 xs]
        validOpt _ _ _ [] = True
        validOpt n m k (x:xs) = not (n == x || n+m == x+k || n-m == x-k) && validOpt n m (k+1) xs
        makelsList 1 = [[1]] 
        makelsList n = makelsList (n-1) ++ [[n]]

queens1 :: Int -> [[Int]]
queens1 n = filter test (generate n)
    where generate 0      = [[]]
          generate k      = [q : qs | q <- [1..n], qs <- generate (k-1)]
          test []         = True
          test (q:qs)     = isSafe q qs && test qs
          isSafe   try qs = not (try `elem` qs || sameDiag try qs)
          sameDiag try qs = any (\(colDist,q) -> abs (try - q) == colDist) $ zip [1..] qs

queens2 :: Int -> [[Int]]
queens2 n = map reverse $ queens' n
    where queens' 0       = [[]]
          queens' k       = [q:qs | qs <- queens' (k-1), q <- [1..n], isSafe q qs]
          isSafe   try qs = not (try `elem` qs || sameDiag try qs)
          sameDiag try qs = any (\(colDist,q) -> abs (try - q) == colDist) $ zip [1..] qs

rocks :: Int -> [[Int]]
rocks n = qArr!n where
        qArr = listArray (1,n) [f i | i <- [1..n]]
        f 1 = makelsList n
        f i = concatMap (extend n)  (qArr!(i-1))
        extend n xs = [xs++[k] | k <- [1..n], validOpt k (length xs+1) 1 xs]
        validOpt _ _ _ [] = True
        validOpt n m k (x:xs) = not (n == x || n+m == x+k) && validOpt n m (k+1) xs
        makelsList 1 = [[1]] 
        makelsList n = makelsList (n-1) ++ [[n]]
