import java.util.Scanner;


public class Temperature{
    public static void main(String args[]){
        float f;
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter temperature in Fahrenheit:");
        f = input.nextFloat();

        float c = ((f - 32) * 5)/9;
        System.out.println("Celsius :" + c);
        input.close();
    }
}