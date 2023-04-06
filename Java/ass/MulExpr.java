class MulExpr extends Expr {

    public MulExpr(Expr e1, Expr e2){
        super(e1,e2);
    }

    String makeString(){
        String s = "(" + subexp1.makeString() + " * " + subexp2.makeString() + ")";
        return(s);
    }
    
    public int evaluate(){
        return subexp1.evaluate() * subexp2.evaluate();
    }
}

