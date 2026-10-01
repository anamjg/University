import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class sammenligninger{

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java Sammenligninger <file_path>");
            return;
        }

        String filePath = args[0];

        try {
            // Reads the file and adds the integers to a list
            List<Integer> list = readIntegersFromFile(filePath);
            
            // Converts the list to an array
            int[] A = convertListToArray(list);
            int n = A.length;
            
            int[][] dataInsert = new int[n + 1][3];
            int[][] allDataMerge = new int[n + 1][3];

            for (int i = 1; i < n + 1; i++) {
                int[] arrayInsert = Arrays.copyOfRange(A, 0, i);
                int[] arrayMerge = Arrays.copyOfRange(A, 0, i);

                // Sorts the array using the insertion method
                dataInsert[i] = insertionSort(arrayInsert);

                // Sorts the array using the merge method
                allDataMerge[i] = getDataMerge(arrayMerge);
            }

            // Prints results to CSV file
            printToCSVFile(n + 1, dataInsert, allDataMerge);
        } catch (IOException e) {
            System.err.println("Error writing to output file: " + e.getMessage());
        }
    }

    /* Utility function to read integers from the file and add them to a list */
    static List<Integer> readIntegersFromFile(String filePath) throws FileNotFoundException {
        List<Integer> list = new ArrayList<>();
        
        try (Scanner scan = new Scanner(new File(filePath))) {
            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                // Parse the line as an integer and add it to the list
                int number = Integer.parseInt(line);
                list.add(number);
            }
        }
        
        return list;
    }

    /* Utility function to convert a list to an array */
    static int[] convertListToArray(List<Integer> list) {
        int[] A = new int[list.size()];
        
        for (int i = 0; i < list.size(); i++) {
            A[i] = list.get(i);
        }
        
        return A;
    }

    static int[] insertionSort(int[] A) {
        long t = System.nanoTime();
        int n = A.length;
        int compsInsert = 0; // Counter for comparisons
        int swapsInsert = 0; // Counter for changes (swaps)

        for (int i = 1; i < n; i++) {
            int j = i;

            while (j > 0 && A[j - 1] > A[j]) {
                int value = A[j - 1];
                A[j - 1] = A[j];
                A[j] = value;
                j--;
                swapsInsert++;
                compsInsert++;
            }

            if (j > 0 && A[j] > A[j - 1]) {
                compsInsert++;
            }
        }

        int timeInsert = (int) ((System.nanoTime() - t) / 1000);

        int[] insertData = { compsInsert, swapsInsert, timeInsert };

        return insertData;
    }

    public static int swapsMerge = 0;
    public static int compsMerge = 0;

    static int[] merge(int[] A1, int[] A2, int[] A) {
        int i = 0;
        int j = 0;

        while (i < A1.length && j < A2.length) {
            compsMerge++; // comps: A1[i] with A2[j]
            if (A1[i] <= A2[j]) {
                compsMerge++;
                if (A[i + j] != A1[i]) {
                    A[i + j] = A1[i];
                    swapsMerge++;
                }
                i++;
            } else {
                compsMerge++; // comps: A[i+j] with A2[j]
                if (A[i + j] != A2[j]) {
                    A[i + j] = A2[j];
                    swapsMerge++;
                }
                j++;
            }
        }

        while (i < A1.length) {
            compsMerge++; // comps: A[i+j] with A1[i]
            if (A[i + j] != A1[i]) {
                swapsMerge++;
                A[i + j] = A1[i];
            }
            i++;
        }

        while (j < A2.length) {
            compsMerge++; // comps: A[i+j] with A2[j]
            if (A[i + j] != A2[j]) {
                swapsMerge++;
                A[i + j] = A2[j];
            }
            j++;
        }
        return A;
    }

    static int[] getDataMerge(int[] A) {
        long t = System.nanoTime();
        mergeSort(A);
        int timeMerge = (int) ((System.nanoTime() - t) / 1000);
        int[] data = { compsMerge, swapsMerge, timeMerge };
        compsMerge = 0;
        swapsMerge = 0;
        return data;
    }

    /* Function that sorts an array with n elements */
    static int[] mergeSort(int[] A) {
        int n = A.length;
        if (n <= 1) {
            return A;
        }

        int i = n / 2;
        int[] a1 = Arrays.copyOfRange(A, 0, i);
        int[] a2 = Arrays.copyOfRange(A, i, n);

        int[] A1 = mergeSort(a1);
        int[] A2 = mergeSort(a2);

        return merge(A1, A2, A);
    }

    static void printToCSVFile(int n, int[][] dataInsert, int[][] dataMerge) throws IOException {
        String csvFileName = "sammenligninger.csv";

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(csvFileName))) {
            // Write the header line
            writer.write("n,insert_cmp,insert_swaps,insert_time,merge_cmp,merge_swaps,merge_time");
            writer.newLine();

            // Write the data rows
            for (int i = 0; i < n; i++) {
                StringBuilder row = new StringBuilder();
                row.append(i).append(',');
                for (int j = 0; j < 3; j++) {
                    row.append(dataInsert[i][j]).append(',');
                }
                for (int j = 0; j < 3; j++) {
                    row.append(dataMerge[i][j]);
                    if (j < 2) {
                        row.append(',');
                    }
                }
                writer.write(row.toString());
                writer.newLine();
            }
        } catch (IOException e) {
            System.err.println("Error writing to CSV file: " + e.getMessage());
        }
    }
}
