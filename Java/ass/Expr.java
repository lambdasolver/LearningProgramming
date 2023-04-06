abstract public class Expr {

	Expr subexp1;
	Expr subexp2;

	public Expr(Expr e1, Expr e2) {
		subexp1 = e1;
		subexp2 = e2;
	}

	abstract String makeString();
	abstract public int evaluate();
}
