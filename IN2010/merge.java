// Java program for implementation of Merge Sort
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class merge{

    public static void main(String[] args){
        String filePath = args[0];
        try{
            // Reads the file and adds the integers to a list
            List<Integer> list = readIntegersFromFile(filePath);
            // Converts the list to an array
            int[] A = convertListToArray(list);
            // Sorts the array using the merge method
            MergeSort(A);
            // Gets the name of the input file 
            File file = new File(filePath);
            String name = file.getName();
            // Prints the results to an output file
            PrintToFile(A, name);
        } catch (FileNotFoundException e){
            System.err.println("File not found: " + filePath);
        } catch (IOException e){
            System.err.println("Error writing to output file: " + e.getMessage());
        }  
    }

    /* Utility function to read the integer from the file and add them to a list */
    static List<Integer> readIntegersFromFile(String filePath) throws FileNotFoundException{
        List<Integer> list = new ArrayList<>();
        // Create a Scanner to read from the file
        Scanner scan = new Scanner(new File(filePath));
        
        // Loop through the lines in the file
        while (scan.hasNextLine()){
            String line = scan.nextLine();
            // Parse the line as a integer and add it to the list
            int number = Integer.parseInt(line);
            list.add(number);
        }
        // Close the scanner
        scan.close();

        return list;
    } 

    /* Utility function to convert list to array */
    static int[] convertListToArray(List<Integer> list){
        // Creates an array A of the same size as the list
        int[] A = new int[list.size()];

        // Copies all values of the list into the array A in the same order
        for (int i = 0; i < list.size(); i++){
            A[i] = list.get(i);
        }

        return A;
    }
    
    /* Function to  */
    static int[] Merge(int[] A1, int[] A2, int[] A){
        int i = 0;
        int j = 0;       

        while (i < A1.length && j < A2.length){
            if (A1[i] <= A2[j]){
                A[i+j] = A1[i];
                i++;
            }
            else{
                A[i+j] = A2[j];
                j++;
            }
        }

        while (i < A1.length){
            A[i+j] = A1[i];
            i++;
        }

        while (j < A2.length){
            A[i+j] = A2[j];
            j++;
        }

        return A;
    }

    /* Funtion that sorts an Array with n elements */
    static int[] MergeSort(int[] A){
        int n = A.length;
        if (n<=1){
            return A;
        }

        int i = n/2;
        int[] a1 = Arrays.copyOfRange(A, 0, i);
        int[] a2 = Arrays.copyOfRange(A, i, n);

        int[] A1 = MergeSort(a1);
        int[] A2 = MergeSort(a2);

        return Merge(A1, A2, A);
    }

    /*  A utility function to print the values to
     *  the output file. 
     */
    static void PrintToFile(int A[], String name) throws IOException{
        // Split the file name from the file type
        String[] Name = name.split("\\.");
        // Create file called name_insertion.out.txt where name is the same file name as the input file
        BufferedWriter writer = new BufferedWriter(new FileWriter(Name[0] + "_merge.out.txt"));
        // Write one integer on each line
        for (Integer number : A){
            writer.write(number.toString());
            writer.newLine();
        }

        writer.close();
    }
}
