public class Calculator {
	LinearList<Token> toklist;
	Stack<Expr> exprstack;
	
	public Calculator(LinearList<Token> toks) {
		toklist = toks;		
		exprstack = new Stack<Expr>();
	}
    
    public Expr makeExpr(){
        Iterator<Token> itr = toklist.getIterator();

        while(itr.hasNext()){
            itr.next().hopOnStack(exprstack);
        }

        return exprstack.pop();
    }
}
