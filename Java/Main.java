import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Scanner sc = new Scanner(System.in);
        int scanned = sc.nextInt();
        System.out.println(scanned);
        int i;
        for (i=0; i<5; i++) {
            System.out.println(scanned++)
        }

    }
}