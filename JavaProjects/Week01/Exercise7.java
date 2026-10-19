import java.util.Scanner;

public class Exercise7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your mark (0-100): ");
        int mark = scanner.nextInt();

        if (mark >= 80 && mark <= 100) {
            System.out.println("HD");
        } else if (mark >= 70) {
            System.out.println("D");
        } else if (mark >= 60) {
            System.out.println("C");
        } else if (mark >= 50) {
            System.out.println("P");
        } else {
            System.out.println("F");
        }

        scanner.close();
    }
}
