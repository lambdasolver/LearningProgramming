import java.util.*;
public class DrivingFloor{
    int ncars, carcount;

    LinearList riders = new LinearList();
    LinearList carlist = new LinearList();

    public DrivingFloor(int n){
        ncars = n;
        carcount = 0;
        for (int i=1; i <= ncars; i++){
            carlist.add(i);
        }
    }

    // Checks if cars are available
    public boolean nocars(){
        if (carlist.listsize == 0){
            return true;
        }
        return false;
    }

    // rider joins the line
    public synchronized void riderjoins(int rid){
        riders.add(rid);
        Date date = new Date();
        System.out.println("Rider "+Integer.toString(rid)+" joins queue at "+date);
        System.out.println("Car queue "+carlist.prints());
        System.out.println("Rider queue "+riders.prints());
        System.out.println("Cars on the floor "+Integer.toString(carcount));
        System.out.println("");
    }

    // rider starts ramping
    public synchronized int enter(int rid, int rtime){
        while  (carcount >= 5 || riders.head == null || riders.head.value != rid || this.nocars()){
            try{
                wait();
            }
            catch(InterruptedException e){}
        }
        int car = carlist.deq();
        riders.deq();
        carcount = carcount + 1;
        Date date = new Date();
        System.out.println("Rider "+Integer.toString(rid)+" starts ride in car "+Integer.toString(car)+" at "+date);
        System.out.println("Car queue "+carlist.prints());
        System.out.println("Rider queue "+riders.prints());
        System.out.println("Cars on the floor "+Integer.toString(carcount));
        System.out.println("");
        return car;
    }

    // rider leaves 
    private synchronized void leave(int rid, int rcar){
        carlist.add(rcar);
        carcount = carcount - 1;
        Date date = new Date();
        System.out.println("Rider "+Integer.toString(rid)+" finishes ride at "+date);
        System.out.println("Car "+Integer.toString(rcar)+" joins queue at "+date);
        System.out.println("Car queue "+carlist.prints());
        System.out.println("Rider queue "+riders.prints());
        System.out.println("Cars on the floor "+Integer.toString(carcount));
        System.out.println("");
        notifyAll();
    }
    public void takeAride(int rider_id, int ride_time){
        int car;
        this.riderjoins(rider_id);
        car = this.enter(rider_id, ride_time);
        try{
            Thread.sleep(ride_time);
        }
        catch(InterruptedException e){}
        this.leave(rider_id, car);
        
    }

}
