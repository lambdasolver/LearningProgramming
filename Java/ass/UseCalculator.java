public class UseCalculator {
	Calculator calc;
	Expr expr;
	
	public UseCalculator() {
		LinearList<Token> toklist1, toklist2, toklist3, toklist4;

		toklist1 = new LinearList<Token>();
		toklist1.add(new Token(Token.TokType.Num, 22));
		toklist1.add(new Token(Token.TokType.Num, 5));
		toklist1.add(new Token(Token.TokType.Add));
		toklist1.add(new Token(Token.TokType.Num, 3));
		toklist1.add(new Token(Token.TokType.Mul));
		toklist1.add(new Token(Token.TokType.Num, 4));
		toklist1.add(new Token(Token.TokType.Num, 3));
		toklist1.add(new Token(Token.TokType.Mul));
		toklist1.add(new Token(Token.TokType.Add));
		toklist1.add(new Token(Token.TokType.Num, 20));
		toklist1.add(new Token(Token.TokType.Sub));
		calc = new Calculator(toklist1);
		expr = calc.makeExpr();
		System.out.println(expr.makeString());
		System.out.println("The value of the expression is: " + expr.evaluate());

		toklist2 = new LinearList<Token>();
		toklist2.add(new Token(Token.TokType.Num, 22));
		toklist2.add(new Token(Token.TokType.Num, 5));
		toklist2.add(new Token(Token.TokType.Num, 3));
		toklist2.add(new Token(Token.TokType.Mul));
		toklist2.add(new Token(Token.TokType.Add));
		toklist2.add(new Token(Token.TokType.Num, 4));
		toklist2.add(new Token(Token.TokType.Num, 3));
		toklist2.add(new Token(Token.TokType.Mul));
		toklist2.add(new Token(Token.TokType.Add));
		toklist2.add(new Token(Token.TokType.Num, 20));
		toklist2.add(new Token(Token.TokType.Sub));
		calc = new Calculator(toklist2);
		expr = calc.makeExpr();
		System.out.println(expr.makeString());
		System.out.println("The value of the expression is: " + expr.evaluate());

		toklist3 = new LinearList<Token>();
		toklist3.add(new Token(Token.TokType.Num, 22));
		toklist3.add(new Token(Token.TokType.Num, 5));
		toklist3.add(new Token(Token.TokType.Add));
		toklist3.add(new Token(Token.TokType.Num, 3));
		toklist3.add(new Token(Token.TokType.Mul));
		toklist3.add(new Token(Token.TokType.Num, 4));
		toklist3.add(new Token(Token.TokType.Num, 3));
		toklist3.add(new Token(Token.TokType.Num, 20));
		toklist3.add(new Token(Token.TokType.Sub));
		toklist3.add(new Token(Token.TokType.Mul));
		toklist3.add(new Token(Token.TokType.Add));
		calc = new Calculator(toklist3);
		expr = calc.makeExpr();
		System.out.println(expr.makeString());
		System.out.println("The value of the expression is: " + expr.evaluate());

		toklist4 = new LinearList<Token>();
		toklist4.add(new Token(Token.TokType.Num, 23));
		toklist4.add(new Token(Token.TokType.Num, 5));
		toklist4.add(new Token(Token.TokType.Num, 23));
		toklist4.add(new Token(Token.TokType.Num, 5));    
		toklist4.add(new Token(Token.TokType.Add));
		toklist4.add(new Token(Token.TokType.Add));
		toklist4.add(new Token(Token.TokType.Mul));
		toklist4.add(new Token(Token.TokType.Num, 18));
		toklist4.add(new Token(Token.TokType.Sub));
		toklist4.add(new Token(Token.TokType.Num, 4));
		toklist4.add(new Token(Token.TokType.Num, 3));
		toklist4.add(new Token(Token.TokType.Num, 20));
		toklist4.add(new Token(Token.TokType.Sub));
		toklist4.add(new Token(Token.TokType.Mul));
		toklist4.add(new Token(Token.TokType.Add));
		calc = new Calculator(toklist4);
		expr = calc.makeExpr();
		System.out.println(expr.makeString());
		System.out.println("The value of the expression is: " + expr.evaluate());
 	}
		
	public static void main(String[] args) {
		new UseCalculator();
	}
}
