/**
 * BIT235 Workshop 2 - Exercise 1.6
 * Fuel consumption: 8 litres per 100 km on normal roads,
 * 15% more on rough roads, fuel tank = 40 litres.
 */
public class Exercise1_6 {
    public static void main(String[] args) {
        double tankSize = 40.0;              // litres
        double normalConsumption = 8.0;      // litres per 100 km
        double roughConsumption = normalConsumption * 1.15;  // 15% more

        double normalDistance = tankSize / normalConsumption * 100;
        double roughDistance = tankSize / roughConsumption * 100;

        System.out.printf("Normal road consumption : %.2f litres / 100 km%n",
                          normalConsumption);
        System.out.printf("Rough road consumption  : %.2f litres / 100 km%n",
                          roughConsumption);
        System.out.printf("Distance on normal road : %.2f km%n",
                          normalDistance);
        System.out.printf("Distance on rough road  : %.2f km%n",
                          roughDistance);
    }
}