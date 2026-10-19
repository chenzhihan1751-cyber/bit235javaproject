import java.util.Scanner;

public class Exercise9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        // .equals() compares the text, == would only compare the references
        if (username.equals("admin") && password.equals("java123")) {
            System.out.println("Login successful.");
        } else {
            System.out.println("Access denied.");
        }

        scanner.close();
    }
}
