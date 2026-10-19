public class Exercise8 {
    public static void main(String[] args) {
        int temperature = 32;

        if (temperature > 30) {
            System.out.println("It is hot.");
        } else if (temperature >= 20 && temperature <= 30) {
            System.out.println("It is mild.");
        } else {
            System.out.println("It is cold.");
        }
    }
}
