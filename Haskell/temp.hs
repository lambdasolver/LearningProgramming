import Stack

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