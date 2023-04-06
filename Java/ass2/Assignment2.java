public class Assignment2{

    public static void main(String[] args){

	int nriders = 0;
	int i, ntimes;
	DrivingFloor df = new DrivingFloor(10);  
           // Number of cars on the floor is 10, 1..10


	// Generate a random number of riders, between 11 and 20
	while (nriders < 10){
	    nriders = (int) (Math.random()*20.0);
	}

	Rider riderlist[] = new Rider[nriders];
	Thread riderthreads[] = new Thread[nriders];

	// Create the Riders in riderlist
	for (i = 0; i < riderlist.length; i++){

	    // Choose random number of rides for rider, 
	    // between 2 and 4
	    ntimes = 0;
	    while (ntimes < 2){
		ntimes = (int) (Math.random()*4.0);
	    }

	    riderlist[i] = new Rider(i,ntimes,df);

	}
		
	// Create a Thread for each Rider in riderlist
	for (i = 0; i < riderthreads.length; i++){
	    riderthreads[i] = new Thread(riderlist[i]);
	}

	// Start off  all the Rider Threads in parallel
	for (i = 0; i < riderthreads.length; i++){
	    riderthreads[i].start();
	}

    }
	
}
