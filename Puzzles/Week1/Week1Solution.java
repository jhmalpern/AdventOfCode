import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Week1Solution {
// Need FileNotFoundException in case the file does not exist. 
// Not sure why, but this seems to be a requirement for Java when reading in a file
    public static void main(String[] args) throws FileNotFoundException {        
        
        File file = new File("PuzzleString.txt");
        Scanner scan = new Scanner(file); //Create Scanner object called scan, which is just file input
        String input = scan.nextLine (); //Convert scanner object of input file to string called input
        
        int floor = 0; //Initialize our counter at 0
        char someChar = '(';

        for (int i=0; i < input.length(); i++){
            if(input.charAt(i) == someChar){
                floor ++;
            }else {
                floor = floor - 1;
            }}
        
        System.out.println(floor); //Print floor result

    }
}