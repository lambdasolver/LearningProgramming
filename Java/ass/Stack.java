public class Stack {
    // Stack by Linked List implementation
    private int stacksize = 0;
    private class Stackframe{
        int value;
        Stackframe prev = null;

        Stackframe(int elm){
            value = elm;
        }
    }

    private Stackframe head = null;
    
	public Stack() {}
    public void push(int elt) {
        Stackframe newframe = new Stackframe(elt);
        newframe.prev = head;
        head = newframe;
        stacksize = stacksize + 1;
    }
    public int pop() {
        int temp = head.value;
        head = head.prev;
        stacksize = stacksize - 1;
        return temp;
    }
    public boolean isEmpty() {
        return head == null;
    }
    public int peek() {
        return head.value;
    }
}

