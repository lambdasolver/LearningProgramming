public class Rider implements Runnable{

    // Two constants, used for random delays
    private static final double walkmax = 3000.00; // Walk around park
    private static final double ridemax = walkmax; // Ride time

    private int id;              // My numeric id
    private int ntimes;          // How many times I take a ride
    private DrivingFloor df;     // Reference to driving floor


    // Constructor
    public Rider(int i, int n, DrivingFloor d){   
	id = i;
	ntimes = n;
	df = d;
    }

    public void run(){
    
	for (int i = 0; i < ntimes; i++){
	    int walktime = 0;
	    int ridetime = 0;

	    // Randomly decide how long the ride will last

	    while (ridetime < 1000){
		ridetime = (int) (Math.random()*ridemax);
	    }

	    // Randomly decide how long to walk around between rides

	    while (walktime < 1000){
		walktime = (int) (Math.random()*walkmax);
	    }


            // Take a ride ...
	    df.takeAride(id,ridetime);

	    // ... then walk around the park for a while

	    try{
		Thread.sleep(walktime);
	    }
	    catch(InterruptedException e){};

	}
    }
}


