import java.util.Scanner;

public class Exercise10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Do you have a driver licence (true/false): ");
        boolean hasLicence = scanner.nextBoolean();

        if (age >= 18 && hasLicence) {
            System.out.println("You can drive independently.");
        } else if (age >= 16 && age < 18 && hasLicence) {
            System.out.println("You can drive with restrictions.");
        } else {
            System.out.println("You cannot drive.");
        }

        scanner.close();
    }
}
