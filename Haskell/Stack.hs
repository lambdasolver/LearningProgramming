import Data.List ( intercalate )
import qualified Data.Functor as Num

newtype Stack a = Stack [a]
    deriving Eq 

instance Show a => Show (Stack a) where 
    show (Stack xs) = fancyShow xs where 
        fancyShow = intercalate "->" . map show

push :: a -> Stack a -> Stack a
pop :: Stack a -> (a, Stack a)
top :: Stack a -> a 
fromList :: [a] -> Stack a
empty :: Stack a 
isEmpty :: Stack a -> Bool  

push n (Stack xs) = Stack (n:xs) 
pop (Stack []) = error "Empty stack"
pop (Stack (x:xs)) = (x, Stack xs)
top (Stack []) = error "Empty stack"
top (Stack (x:_)) = x 
fromList = Stack 
empty = Stack [] 
isEmpty (Stack xs) = null xs 



-- if a belongs to the type class Show, then so does [a]
-- if a belong to the type class Eq, then so does [a] 
-- if a belong to the type class Num, [a] does not belong to the type class Num 

-- So we can do Stack a = ... deriving (Eq, Show) 
-- and Haskell will give default implementations of == and show 
-- for values in Stack a, provided a belongs to the classes Eq, Show. 
-- But we cannot do deriving Stack a = ... deriving Num, 
-- because Haskell does not know how to define (+), (*) etc. for 
-- values of type Stack a, even when a belongs to Num. 
-- 
-- In the unlikely event you want to make Stack a an instance of Num,
-- use "instance" like we did for Show. 

-- Meanwhile, you can define functions which work only when the 
-- elements of the Stack belong to a numeric type, by explicitly 
-- adding a constraint.

-- sumStack :: Num a => Stack a -> a 
-- sumStack (Stack xs) = sum xs 










data Op = Add | Sub | Mul | Div --checked
instance Show Op where 
    show Add = "+"
    show Sub = "-"
    show Mul = "*"
    show Div = "/"

data Exp = Leaf Int | Node Exp Op Exp  --checked
instance Show Exp where 
    show = go 0  where 
        prec Add = 1
        prec Sub = 1
        prec Mul = 2
        prec Div = 2 
        go p (Leaf n) = show n 
        go p (Node expl op expr) = f $ go q expl ++ " " ++ show op 
                            ++ " " ++ go (q+1) expr where 
            q = prec op 
            f s = if q < p then "(" ++ s ++ ")" else s 

type Token = Either Int Op    --checked

expToTokList :: Exp -> [Token] 
expToTokList (Leaf n) = [Left n]
expToTokList (Node e1 op e2) = expToTokList e1 ++ expToTokList e2 ++ [Right op]

tokListToExp :: [Token] -> Exp 
tokListToExp = top . foldl step empty where 
    step :: Stack Exp -> Token -> Stack Exp 
    step st (Left n) = push (Leaf n) st 
    step st (Right op) = push (Node expl op expr) stl where 
        (expr, str) = pop st 
        (expl, stl) = pop str 

eval :: Exp -> Int 
eval (Leaf n) = n 
-- eval (Node e1 op e2) = opToFunc op (eval e1) (eval e2)
eval (Node e1 op e2) = f (eval e1) (eval e2) where 
    f = case op of 
        Add -> (+)
        Sub -> (-)
        Mul -> (*)
        Div -> div

strToTokList :: String -> [Token] --checked
strToTokList str = map tokenize (words str) where 
    tokenize :: String -> Token 
    tokenize "+" = Right Add 
    tokenize "-" = Right Sub 
    tokenize "*" = Right Mul 
    tokenize "/" = Right Div 
    tokenize str = Left (read str :: Int)  

main :: IO ()
main = interact (unlines . map processLine . lines) 

processLine :: String -> String 
processLine line = show exp ++ " = " ++ show (eval exp) where 
    exp = tokListToExp $ strToTokList line