public class LinearList<T> {
    private class ListFrame{
        T value;
        ListFrame next = null;
        
        ListFrame(T elm){
            value = elm;
        }
    }

    private ListFrame head = null;
    private ListFrame last = null;

    private class Iter implements Iterator<T> {

        private ListFrame frame_next;

        Iter() {
            frame_next = head;
        }

        public boolean hasNext() {
            return frame_next != null;
        }

        public T next() {
            T temp = frame_next.value;
            frame_next = frame_next.next;
            return temp;
        }
    }

    public LinearList() {}

    public void add(T elt){
        ListFrame newframe = new ListFrame(elt);

        if (head == null){
            head = newframe;
            last = newframe;
        }
        else{
            last.next = newframe;
            last = newframe;
        }
    }
    
    public Iter getIterator(){
        Iter itr = new Iter();
        return itr;
    }

}
