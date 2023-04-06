public class LinearList {
    int listsize=0;
    public class ListFrame{
        int value;
        ListFrame next = null;
        ListFrame prev = null;
        
        ListFrame(int elm){
            value = elm;
        }
    }

    public ListFrame head = null;
    public ListFrame last = null;


    public LinearList() {
        listsize=0;
    }

    public void add(int elt){
        ListFrame newframe = new ListFrame(elt);

        if (head == null){
            head = newframe;
            last = newframe;
            listsize = listsize + 1;
        }
        else{
            newframe.prev = last;
            last.next = newframe;
            last = newframe;
            listsize = listsize + 1;
        }
    }
    
    public int deq(){

        if (head == last){
            int temp;
            temp = head.value;
            head = null;
            last = null;
            listsize = listsize - 1;
            return temp;
        }
        else{
            int temp;
            temp = head.value;
            head = head.next;
            head.prev = null;
            listsize = listsize - 1;
            return temp;
        }
    }

    public String prints(){
        String s = new String();
        s = "[";
        ListFrame temp = head;
        while (temp != null){
            s = s+Integer.toString(temp.value);
            if (temp.next != null){
                s = s+",";
            }
            temp = temp.next;
        }
        s = s+"]";
        return s;
    }

}
