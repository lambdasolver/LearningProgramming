import Data.List (intercalate)
data BTree a    = Nil | Node (BTree a) a (BTree a) deriving Eq
-- Instances of BST
instance Show a => Show (BTree a) where
    show t = "\n" ++ intercalate "\n" (map (map snd) (fst $ draw5 t)) ++ "\n"

-- End of instances
data Tag        = L | M | R deriving (Eq,Show)
type Entry      = (Tag, Char)
type Line       = [Entry] 

draw4 :: Show a => BTree a -> ([Line],Int)
draw4 Nil               =   ([zip [M] "*"],1 )
draw4 (Node Nil x Nil)  =   
    let (sx,n,m) = (show x, length sx, n `div` 2) in
        ([zip (replicate m L ++ [M] ++ replicate (n-m-1) R) sx], n) 
-- ("2",1,0)=(sx,n,m) ->
-- ([zip (replicate 0 L ++ [M] ++ replicate 0 R), "2"],1) -> ([[(M,"2")]],1)   
-- ("2000",4,2)=(sx,n,m) ->
-- ([zip (replicate 2 L ++ [M] ++ replicate 1 R), "2000"],4) -> ([[(L,"2"),(L,"0"),(M,"0"),(R,"0")]],4) 
draw4 (Node tl x tr)    =   
    (line1:line2:line3:line4:combine linesl linesr, max n (sl+sr+3)) where 
        (sx, n, m)      = (show x , length sx, n `div` 2) 
        (linesl, sl)    = draw4 tl 
        (linesr, sr)    = draw4 tr
        line1           = replicate (sl+1-m) (L,' ')
                            ++ zip (replicate m L ++ [M] ++ replicate (n-m-1) R) sx
                            ++ replicate (sr+2-m+m) (R, ' ')
        line2           = replicate (sl+1) (L,' ')  ++ [(M, '|')] ++ replicate (sr+1) (R,' ')
        line3           = map (process R) (head linesl)
                            ++ [(L,'-'), (M,'+'),(R,'-')]
                            ++ map (process R) (head linesr)
        line4           = map follow line3
        follow (t,c)
            | (t,c) == (L,'+')  = (L,'|')
            | (t,c) == (R,'+')  = (R,'|')
            | otherwise         = (t,' ')
        process b (t,_)
            | t == M            = (b,'+')
            | t == b            = (b,' ')
            | otherwise         = (b,'-')
        combine [] ls           = map (replicate (sl+3) (L,' ') ++) ls
        combine ks []           = map (++ replicate (sr+3) (R,' ')) ks 
        combine (k:ks) (l:ls)   = (k ++ [(L,' '),(M,' '),(R,' ')] ++ l) : combine ks ls


createTree :: [a] -> BTree a
createTree []   = Nil
createTree xs    = Node
    (createTree front) x (createTree back) where
        n = length xs
        (front, x:back) = splitAt (n `div` 2) xs
        
-- my own draw
draw5 :: Show a => BTree a -> ([Line],(Int,Int,Int))
draw5 Nil               =   ([zip [M] "*"],(0,1,0) )
draw5 (Node Nil x Nil)  =   
    let (sx,n,m) = (show x, length sx, n `div` 2) in
        ([zip (replicate m L ++ [M] ++ replicate (n-m-1) R) sx], (m,1,n-m-1)) 

draw5 (Node tl x tr) = (l1:l2:l3:l4:mainline,(a,b,c)) where
    (mainline ,(a,b,c)) = drawing xs ys
    (xs,(xsa,xsb,xsc)) = draw5 tl
    (ys,(ysa,ysb,ysc)) = draw5 tr 
    drawing xs ys = (join xs ys, (xsa+xsb+xsc+1, 1, ysa+ysb+ysc+1) )
    join (as:ass) (bs:bss) = go as bs : join ass bss
    join xss []  = map (++  ([(L,' '),(M, ' '),(R,' ')] ++ replicate (ysa+ysb+ysc) (R,' ') )) xss
    join [] yss  = map ((replicate (xsa+xsb+xsc) (L,' ') ++  [(L,' '),(M, ' '),(R,' ')]) ++ ) yss
    go xss yss = xss ++ [(L,' '),(M, ' '),(R,' ')] ++ yss
    ([cs],(m,n,o)) = draw5 (Node Nil x Nil)
    l1 = replicate (a-m) (L,' ') ++ cs ++ replicate (c-o) (R,' ')
    l2 = replicate a (L,' ') ++ [(M, '|')] ++ replicate c (R,' ')
    l3 = replicate xsa (L,' ') ++ [(L,'+')] ++ replicate (xsc+1) (L,'-') ++ [(M,'+')] ++ replicate (ysa+1) (R,'-') ++ [(R,'+')] ++ replicate ysc (R,' ')
    l4 = replicate xsa (L,' ') ++ [(L,'|')] ++ replicate (xsc+ysa+3) (M,' ') ++ [(R,'|')] ++ replicate ysc (R,' ')
 
fibs :: [Int]
fibs = 0:1:zipWith (+) fibs (tail fibs)
fib :: Int -> Int
fib n = fibs!!n
