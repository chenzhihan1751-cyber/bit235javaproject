/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays extended exercise, Exercise 2: bubble sort of 20 values.
 */
public class BubbleSort {

    public static void main(String[] args) {
        int[] numbers = {
            73, 914, 256, 481, 999, 32, 678, 145, 802, 567,
            219, 430, 761, 88, 354, 690, 12, 947, 523, 276
        };

        System.out.println("Before sorting:");
        printArray(numbers);

        int swaps = bubbleSort(numbers);

        System.out.println("After sorting:");
        printArray(numbers);
        System.out.println("Total swaps: " + swaps);
    }

    // One pass compares neighbours [i] and [i + 1] and swaps them when they
    // are out of order, so the biggest value bubbles to the end of the pass.
    // Repeat until a full pass makes no swap, which means the array is sorted.
    public static int bubbleSort(int[] numbers) {
        int swaps = 0;
        boolean swappedInThisPass = true;
        int pass = 0;

        while (swappedInThisPass) {
            swappedInThisPass = false;
            pass++;
            for (int i = 0; i < numbers.length - pass; i++) {
                if (numbers[i] > numbers[i + 1]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[i + 1];
                    numbers[i + 1] = temp;
                    swappedInThisPass = true;
                    swaps++;
                }
            }
        }
        System.out.println("Passes needed: " + pass);
        return swaps;
    }

    public static void printArray(int[] numbers) {
        StringBuilder line = new StringBuilder();
        for (int i = 0; i < numbers.length; i++) {
            if (i > 0) {
                line.append(" ");
            }
            line.append(numbers[i]);
        }
        System.out.println(line);
    }
}
