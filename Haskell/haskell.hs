data BTree = Nil | BNode Int BTree BTree deriving (Show)
data Tree = Node Int [Tree] deriving Show
t1 :: BTree
t1 = BNode 1 (BNode 2 Nil (BNode 3 (BNode 4 Nil (BNode 5 Nil (BNode 6 Nil Nil))) (BNode 7 (BNode 8 Nil Nil) Nil))) Nil

t2 :: Tree
t2 = Node 1 [Node 2 [], Node 3 [Node 4 [], Node 5 [], Node 6[]], Node 7 [Node 8 []]]

decode :: BTree -> Tree
decode Nil               = error "No Branch"
decode (BNode x Nil Nil) = Node x []
decode (BNode x tl Nil)  = Node x [decode tl]
decode (BNode x Nil tr)  = Node x [decode tr]
decode (BNode x tl tr)   = Node x [decode tl, decode tr]

encode :: Tree -> BTree
encode (Node root branches) = BNode root (encode' branches) Nil where
    encode' :: [Tree] -> BTree 
    encode' [] = Nil
    encode' [Node t []] = BNode t Nil Nil
    encode' ((Node x xs):trs) = BNode x (encode' xs) (encode' trs)
