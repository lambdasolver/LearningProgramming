import Data.Map (Map)
data Shape a = Circle a a a |
                Rectangle a a a a deriving (Ord)
instance Show a => Show (Shape a ) where
    show (Circle a b c) = "(" ++ show a ++ show b ++ show c++ ")"
instance Eq a => Eq (Shape a) where
    (Circle a _ _) == (Circle b _ _) = a == b 
    (Circle a _ _) /= (Circle b _ _) = a /= b 




data Shapee = Circlee {xcoordinate :: Int,
                        ycoordinate :: Int,
                        zcooradinate :: Int}

f :: Shapee -> Int
f Circlee {xcoordinate = a, ycoordinate = b, zcooradinate = c} = a + b + c

type String = [Char]
type Shapes = [Shape Int]

type Phonenumber = Int 
type  List a b = [(a,b)]
type MapInt = Data.Map.Map Int
-- f' :: List Int Char -> Char 
-- f' []  = error "Nothing"
-- f' (x:xs) = snd x

data Tree a = Null | Node a (Tree a) (Tree a)

--type Stack a = [a]  
--push :: Stack a -> a -> Stack a
--push xs x = x:xs

--pop :: Stack a -> (a, Stack a)
--pop [] = error "Empty List"
--pop (x:xs) = (x, xs)

newtype Stack a = Stack [a]
instance Show a => Show (Stack a) where
    show (Stack [a]) = show [a]

push :: Stack a -> a -> Stack a
push (Stack xs) x = Stack (x:xs)

pop :: Stack a -> (a,Stack a)
pop (Stack xs) 
                | null xs = error "Empty List"
                |  otherwise = (head xs, Stack xs) 

isEmpty :: Stack a -> Bool 
isEmpty (Stack xs ) = null xs


--type Q a = [a]

--enq :: Q a -> a -> Q a
--enq (xs) x = xs ++ [x]

--deq :: Q a -> (a,Q a)
--deq [] = error "Emmpty List"
--deq (x:xs) = (x,xs)


-- [a,b,c] ++ [] = a : ([b,c]++ [])= a :(b: ([c]++[]))=
-- [a,b,c,d,e,f] g -> [a,b,c,d] [f,e] g -> [a,b,c,d] g:[f,e]
-- Q (xs,ys) = xs ++ reverse ys
newtype Q a = Q ([a],[a])
instance Show a => Show (Q a)  where 
    show (Q (xs,ys)) = show $ xs ++ reverse ys

enq :: Q a -> a -> Q a
enq (Q (xs,ys)) x = Q (xs,x:ys)

deq :: Q a -> (a, Q a )
deq (Q ([],[])) =  error "Empty List"
deq (Q ([], ys)) = deq $ Q (reverse  ys , [])
deq (Q (x:xs,ys)) = (x, Q (xs,ys))