import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class teque{    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = Integer.parseInt(scan.nextLine());
        
        List<String> S = new ArrayList<>();
        List<Integer> x = new ArrayList<>();

        for(int i = 0; i < N; i++){
            String[] input = scan.nextLine().split(" ");
            S.add(input[0]);
            x.add(Integer.parseInt(input[1]));
        }

        scan.close();

        ArrayList<Integer> myNum = new ArrayList<>();
        List<Integer> results = new ArrayList<>();

        for(int i = 0; i < N; i++){
            String function = S.get(i);
            int value = x.get(i);

            if(function.equals("push_front")){
                myNum.add(0, value);
            } else if(function.equals("push_back")){
                myNum.add(value);
            } else if(function.equals("push_middle")){
                if(myNum.size()%2 != 0){
                    myNum.add(myNum.size()/2 + 1, value);
                } else{
                    myNum.add(myNum.size()/2, value);
                }
                
            } else if(function.equals("get")){
                results.add(myNum.get(value));
            }
        }

        for (int result : results){
            System.out.println(result);
        }
    }    
}
