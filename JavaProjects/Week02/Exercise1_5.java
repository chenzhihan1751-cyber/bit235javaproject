/**
 * BIT235 Workshop 2 - Exercise 1.5
 * Volume of a sphere = (4/3) * pi * r^3
 * pi = 3.14 and r = diameter / 2
 */
public class Exercise1_5 {
    public static void main(String[] args) {
        final double PI = 3.14;
        double sunDiameter = 865000.0;     // miles
        double earthDiameter = 7600.0;     // miles

        double sunRadius = sunDiameter / 2;
        double earthRadius = earthDiameter / 2;

        double earthVolume = 4.0 / 3 * PI * Math.pow(earthRadius, 3);
        double sunVolume = 4.0 / 3 * PI * Math.pow(sunRadius, 3);
        double ratio = sunVolume / earthVolume;

        System.out.printf("a.) Volume of the Earth : %,.2f cubic miles%n",
                          earthVolume);
        System.out.printf("b.) Volume of the Sun   : %,.2f cubic miles%n",
                          sunVolume);
        System.out.printf("c.) Sun / Earth ratio   : %,.2f%n", ratio);
    }
}