import java.util.Scanner;

/*
 * BIT235 Workshop 3 - Part 3, Exercise 6
 * Picture framing cost calculator.
 *
 * Each frame is 1 inch wide, so the outside edge of the frame is
 * (length + 2) by (width + 2) inches and its perimeter is
 *     2 * (length + 2 + width + 2) = 2 * (length + width + 4) inches.
 *
 * Prices per inch: colouring $0.10, regular frame $0.15, fancy frame $0.25.
 * A crown costs $0.35 each.
 */
public class FramingCost {
    public static void main(String[] args) {
        final double COLOUR_PER_INCH = 0.10;
        final double REGULAR_PER_INCH = 0.15;
        final double FANCY_PER_INCH = 0.25;
        final double CROWN_EACH = 0.35;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Length of the picture (inches):");
        double length = scanner.nextDouble();
        System.out.println("Width of the picture (inches):");
        double width = scanner.nextDouble();

        System.out.println("Type of frame (regular/fancy):");
        String frameType = scanner.next().trim().toLowerCase();

        System.out.println("Colour of the frame:");
        String colour = scanner.next().trim();

        System.out.println("Add crowns? (yes/no):");
        String crownsAnswer = scanner.next().trim().toLowerCase();
        int crowns = 0;
        if (crownsAnswer.startsWith("y")) {
            System.out.println("Number of crowns:");
            crowns = scanner.nextInt();
        }

        double framePerInch;
        String frameName;
        if (frameType.startsWith("f")) {
            framePerInch = FANCY_PER_INCH;
            frameName = "fancy";
        } else if (frameType.startsWith("r")) {
            framePerInch = REGULAR_PER_INCH;
            frameName = "regular";
        } else {
            System.out.println("Unknown frame type, using a regular frame.");
            framePerInch = REGULAR_PER_INCH;
            frameName = "regular";
        }

        double perimeter = 2 * (length + width + 4);
        double colourCost = perimeter * COLOUR_PER_INCH;
        double frameCost = perimeter * framePerInch;
        double crownCost = crowns * CROWN_EACH;
        double totalCost = colourCost + frameCost + crownCost;

        System.out.println();
        System.out.println("----------- Framing quote -----------");
        System.out.printf("Picture size        : %.2f x %.2f inches%n",
                length, width);
        System.out.printf("Frame               : %s, 1 inch wide%n",
                frameName);
        System.out.printf("Colour              : %s%n", colour);
        System.out.printf("Frame perimeter     : %.2f inches%n", perimeter);
        System.out.printf("Colouring  (%.2f/in): $%.2f%n",
                COLOUR_PER_INCH, colourCost);
        System.out.printf("Frame      (%.2f/in): $%.2f%n",
                framePerInch, frameCost);
        System.out.printf("Crowns     (%d x $%.2f): $%.2f%n",
                crowns, CROWN_EACH, crownCost);
        System.out.printf("TOTAL COST          : $%.2f%n", totalCost);
        System.out.println("-------------------------------------");

        scanner.close();
    }
}
