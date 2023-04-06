public class Token {
	public enum TokType {Num, Add, Sub, Mul}
	private TokType toktype;
	private int tokval;
    
    public Token(TokType typ){
        toktype = typ;
    }
    public Token(TokType typ, int val){
        toktype = typ;
        tokval = val;
    }
    public void hopOnStack(Stack<Expr> stack){
        Expr exprn = null;
        if (toktype == TokType.Num){
            exprn = new NumExpr(tokval, null, null);
        }
        else{
            Expr expr1 = stack.pop();
            Expr expr2 = stack.pop();

            if (toktype == TokType.Add){
                exprn = new AddExpr(expr2, expr1);
            }
            else if (toktype == TokType.Sub){
                exprn = new SubExpr(expr2, expr1);
            }
            else if (toktype == TokType.Mul){
                exprn = new MulExpr(expr2, expr1);
            }
        }
        stack.push(exprn);
    }
}
