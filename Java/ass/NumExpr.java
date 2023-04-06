class NumExpr extends Expr {
    int value;

    public NumExpr(int val, Expr e1, Expr e2){
        super(null, null);
        value = val;
    }

    public String makeString(){
        return Integer.toString(value);
    }
    
    public int evaluate(){
        return value;
    }
}

