/*
 * 
import java.util.Scanner;
public class tests{   
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = Integer.parseInt(scan.nextLine());

        String[] command = new String[N];
        int[] number = new int[N];

        for(int i = 0; i < N; i++){
            String[] input = scan.nextLine().split(" ");
            command[i] = input[0];
            number[i] = Integer.parseInt(input[1]);
        }
        
        scan.close();

        for(int i = 0; i < N; i++){
            
            if(command[i].equals("push_front")){
                push_front(number[i]);
            } else if (command[i].equals("push_back")) {
                push_back(number[i]);
            } else if (command[i].equals("push_middle")) {
                push_middle(number[i]);
            } else if (command[i].equals("get")) {
                get(number[i]);
            } else{
                System.out.println("Did not work");
            }
        }
    }
    public static int[] A = new int[0]; 
    
    static void push_front(int x){
        int[] A_new = new int[A.length + 1];
        A_new[0] = x;
        for(int i = 0; i < A_new.length - 1; i++){
            A_new[i+1] = A[i];
        }
        A = A_new;
    }

    static void push_back(int x){
        int[] A_new = new int[A.length + 1];
        for(int i = 0; i < A_new.length - 1; i++){
            A_new[i] = A[i];
        }
        A_new[A_new.length - 1] = x;
        A = A_new;
    }

     static void push_middle(int x){
        int[] A_new = new int[A.length + 1];
        int mid = A_new.length/2;
        for(int i = 0; i < mid; i++){
            A_new[i] = A[i];
        }
        A_new[mid] = x;
        for(int i = mid; i < A_new.length-1; i++){
            A_new[i+1] = A[i];
        }
        A = A_new;
    }

    static void get(int i){
        System.out.println(A[i]);
    }
}
*/
/*
//import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import com.opencsv.CSVWriter;

public class tests{   
    public static void main(String[] args){
        try{
            int[] A = {80, 91, 7, 33, 50, 70, 13, 321, 12};
            int n = A.length;
            int[][] data_insert = new int[n+1][3];
            int[][] data_merge = new int[n+1][3];
            for(int i = 0; i < n+1; i++){
                int[] A_merge = new int[i];
                int[] A_insert = new int[i];
                for(int j = 0; j < i; j++){
                    A_merge[j] = A[j];
                    A_insert[j] = A[j];
                }
                
                long t_merge = System.nanoTime();
                MergeSort(A_merge);          
                int time_merge = (int)((System.nanoTime()-t_merge)/1000);
                data_merge[i][0] = comps_merge;
                data_merge[i][1] = swaps_merge;
                data_merge[i][2] = time_merge;  
                data_insert[i] = InsertionSort(A_insert);
                swaps_merge = 0;
                comps_merge = 0;
                PrintToCSVFile(n+1, data_insert, data_merge);
            }
        }catch (IOException e){
            System.err.println("Error writing to output file: " + e.getMessage());
        } 
    }

    static int[] InsertionSort(int[] A) {
        long t_insert = System.nanoTime();
        int n = A.length;
        int comps_insert = 0;   // Counter for comparisons
        int swaps_insert = 0;       // Counter for changes (swaps)

        for (int i = 1; i < n; i++) {
            int j = i;
            
            while(j > 0 && A[j - 1] > A[j]){
                int value = A[j - 1];
                A[j - 1] = A[j];
                A[j] = value;
                j--; 
                swaps_insert++;     
                comps_insert++;
            }

            if(j>0 && A[j]>A[j-1]){
                comps_insert++;
            }         
        }
        
        int time_insert = (int)((System.nanoTime()-t_insert)/1000);

        int[] insert_data = {comps_insert,swaps_insert, time_insert};

        return insert_data;
            
    }

    public static int swaps_merge = 0;
    public static int comps_merge = 0;

    static int[] Merge(int[] A1, int[] A2, int[] A){
        int i = 0;
        int j = 0;

        while (i < A1.length && j < A2.length){  
            comps_merge++;  
            if (A1[i] <= A2[j]){ 
                comps_merge++; 
                if(A[i+j] != A1[i]){    
                    A[i+j] = A1[i];  
                    swaps_merge++;   
                }              
                
                i++;               
            }
            else{
                comps_merge++;  
                if(A[i+j] != A2[j]){  
                    A[i+j] = A2[j]; 
                    swaps_merge++;        
                }  
                j++;
            }
        }

        while (i < A1.length){  
            comps_merge++;
            if(A[i+j] != A1[i]){   
                    swaps_merge++;    
                    A[i+j] = A1[i];       
            }
            i++;
        }

        while (j < A2.length){  
            comps_merge++;  
            if(A[i+j] != A2[j]){   
                swaps_merge++;  
                A[i+j] = A2[j];        
            }
            j++;
        }
        return A;
    }

    // Funtion that sorts an Array with n elements 
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

    static void PrintToCSVFile(int n, int[][] data_insert, int[][] data_merge) throws IOException{
        // Create file called sammenligninger.csv
        CSVWriter writer = new CSVWriter(new FileWriter("sammenligning_test.txt"));
        // Writes the header line in the csv file
        String header[] = {"n", "insert_cmp", "insert_swaps", "insert_time", "merge_cmp", "merge_swaps", "merge_time"};
        writer.writeNext(header);
        //Writing data to a csv file
        for (int i=0; i<n; i++){
            writer.write(i + ","); 
            for (int number : data_insert[i]){
                writer.write(number + ",");
                String line2[] = {"1", "Krishna", "2548", "2012-01-01", "IT"};
            }
            for (int number : data_merge[i]){
                writer.write(number + ",");
            }    
            writer.newLine();      
        }

        writer.close();
    }
}

 */

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class tests{   
    public static void main(String[] args) throws IOException{
        int[][] all_data = {
            {0,0,0,0,0,0,0},
            {1,0,0,2,0,0,1},
            {2,1,0,0,3,0,34},
            {3,3,2,2,8,5,8},
            {4,6,4,1,12,4,7},
            {5,9,6,2,18,5,9},
            {6,12,8,2,25,11,8},
            {7,18,13,2,33,18,10},
            {8,19,13,2,40,14,13},
            {9,27,20,2,49,20,11},
        };

        int[][] data_insert = {
            {0,0,0},
            {0,0,2},
            {1,0,0},
            {3,2,2},
            {6,4,1,12,4,7},
            {9,6,2,18,5,9},
            {12,8,2,25,11,8},
            {18,13,2,33,18,10},
            {19,13,2,40,14,13},
            {27,20,2,49,20,11},
        };

        int[][] data_merge = {
            {0,0,0},
            {0,0,1},
            {3,0,34},
            {8,5,8},
            {12,4,7},
            {18,5,9},
            {25,11,8},
            {33,18,10},
            {40,14,13},
            {49,20,11},
        };
        
        // Writing the data into the file
        File csvFile = new File("test_csv_file.csv");
        FileWriter fileWriter = new FileWriter(csvFile);
        // Writes the header line in the file
        fileWriter.write("n,insert_cmp,insert_swaps,insert_time,merge_cmp,merge_swaps,merge_time \n");
        for(int[] data : all_data){
            StringBuilder line = new StringBuilder();
            for(int i = 0; i < data.length; i++){
                line.append(data[i]);
                if(i != data.length - 1){
                    line.append(',');
                }
            }
            line.append("\n");
            fileWriter.write(line.toString());
        }
        
        fileWriter.close();
    }
 }