/**
 * BIT235 Workshop 2 - Exercise 1.3
 * Calculate the area of a circle: Area = pi * r^2 with pi = 3.14
 * The program tries several different values of the radius.
 */
public class Exercise1_3 {
    public static void main(String[] args) {
        final double PI = 3.14;
        double[] radii = {1.0, 2.5, 5.0, 7.0, 12.0};

        System.out.println("Radius   Area of the circle");
        System.out.println("---------------------------");

        for (int i = 0; i < radii.length; i++) {
            double radius = radii[i];
            // Math.pow(radius, 2) is the same as radius * radius
            double area = PI * Math.pow(radius, 2);
            System.out.printf("%-8.2f %-10.2f%n", radius, area);
        }
    }
}