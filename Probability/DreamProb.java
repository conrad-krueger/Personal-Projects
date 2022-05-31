import java.util.*;
import java.lang.Math;
class DropRatesTest{
    //#his program simulates 262 ender pearl and 305 blaze rod drops chances for 50,000,000 iterations and compares them to Dream's odds.
    private static long seedUniquifier = 8682522807148012L;



    private static long seedUniquifier(){
        seedUniquifier = seedUniquifier * 181783497276652981L;
        return seedUniquifier;
    }

    public static void main(String args[]){


        //trials to perform

        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of iterations: ");
        int iter = scan.nextInt();

        System.out.println();

        System.out.print("See each iteration? 1] Yes, detailed 2] Yes, not detailed 3] No ");
        long select = scan.nextLong();
        //System.out.print("Seed setting (enter random long integer): ");
        //long seed = scan.nextLong();



        boolean verbose = (select == 2) ? true : false;
        boolean verboseDetailed = (select == 1) ? true : false;

        System.out.println();



        //counters to track if we ever surpass the below target ona single interation
        int dream_ender_luck = 0;
        int dream_blaze_luck = 0;
        int dream = 0;

        int maxBlaze = 0;
        int maxEnder = 0;

        int minBlaze = 0;
        int minEnder = 0;


        int sumBlaze = 0;
        int sumEnder = 0;


        Random rand = new Random(seedUniquifier() ^ System.nanoTime());


        for (long i = 0; i < iter; i++){
            int ender_tracker = 0;
            int blaze_tracker = 0;

            //simulate 262 ender pearl trades with 5% chance of getting an ender pearl
            for (int a = 0; a < 262; a++){
                double chance = rand.nextInt(423);  //423 since this is the sum of the weight's of an item a piglin can drop 
                if (chance < 20) // 20/423 chance of dropping ender pearl
                    ender_tracker++;
            } 

            //simulate 305 blaze rod trades with 5% chance of getting an ender pearl
            for (int a = 0; a < 305; a++){
                int chance = rand.nextInt(2);
                if (chance == 1) //either 1 or 0 blaze rod drops
                    blaze_tracker++;
            } 

            //keep track if blaze rods and/or ender pearl drops meet or exceed dreams odds
        
            boolean lucky = false;

            if (blaze_tracker >= 211){
                dream_blaze_luck++;
                lucky = true;
            }
                
            if (ender_tracker >= 42){
                dream_ender_luck++;
                lucky = true;
            }
            if (blaze_tracker >= 211 && ender_tracker >= 42){
                dream++;
                lucky = true;
            }

            
            if (verbose || lucky || verboseDetailed){
                System.out.print("Iteration: "+ (i+1));
                if (lucky)  
                    System.out.print(" [LUCKY]");
                System.out.println();
            }
                

            if(verboseDetailed || lucky)
                System.out.println("Ender Drop: "+ ender_tracker + "/262 (~"+ ((Math.round(ender_tracker/262.0 * 100000))/1000.0) + "%) Blaze Drop: " +  blaze_tracker + "/305 (~"+ ((Math.round(blaze_tracker/262.0 * 100000))/1000.0) + "%)");

            if (blaze_tracker > maxBlaze)
                maxBlaze = blaze_tracker;
            
            if (ender_tracker > maxEnder)
                maxEnder = ender_tracker;
            
            if (blaze_tracker < minBlaze)
                minBlaze = blaze_tracker;
            
            if (ender_tracker < minEnder)
                minEnder = ender_tracker;

            sumBlaze += blaze_tracker;
            sumEnder += ender_tracker;


        }




        //takes average of all ender pearl and blaze rod results and averages them
        double avgE = sumEnder/iter;
        double avgB = sumBlaze/iter;


        //depict final results
        System.out.println("\n");

        System.out.println("After simulating pearl barters and blaze rod drops for " + iter + " iterations. Here is the data:");
        System.out.println();
        System.out.println("Average Ender Pearl Drop: "+avgE + " out of 262");
        System.out.println("Highest Ender Pearl Drop: "+maxEnder);
        System.out.println("Lowest Ender Pearl Drop: "+minEnder);
        System.out.println();
        System.out.println("Average Blaze Rod Drop: "+avgB + " out of 305");
        System.out.println("Highest Blaze Rod Drop: "+maxBlaze);
        System.out.println("Lowest Blaze Rod Drop: "+minBlaze);
        System.out.println();
        System.out.println("Dream's Ender Pearl luck was achieved: " + dream_ender_luck +" times during the simulation.");
        System.out.println("Dream's Blaze Rod luck was achieved: "+ dream_blaze_luck+ " times during the simulation.");
        System.out.println("Dream's Blaze Rod AND Ender Pearl luck on the same run was achieved: "+dream+ " times during the simulation.");



    }
}