/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays extended exercise, Exercise 3: binary search vs linear search.
 *
 * Task A: sort the list with bubble sort, then search it with binary search.
 * Task B: count the comparisons each search needs and compare the two.
 */
public class BinaryVsLinearSearch {

    public static void main(String[] args) {
        int[] unsorted = {
            73, 914, 256, 481, 999, 32, 678, 145, 802, 567,
            219, 430, 761, 88, 354, 690, 12, 947, 523, 276
        };

        int[] sorted = unsorted.clone();    // keep the original order for the linear search
        bubbleSort(sorted);

        System.out.println("Sorted array:");
        printArray(sorted);

        int[] targets = {523, 500};
        for (int target : targets) {
            System.out.println();
            System.out.println("Searching for " + target + ":");

            int[] binary = binarySearch(sorted, target);
            System.out.println("  Binary search (sorted): index = " + binary[0]
                    + ", comparisons = " + binary[1]);

            int[] linear = linearSearch(unsorted, target);
            System.out.println("  Linear search (unsorted): index = " + linear[0]
                    + ", comparisons = " + linear[1]);

            if (binary[1] < linear[1]) {
                System.out.println("  Binary search used "
                        + (linear[1] - binary[1]) + " fewer comparisons.");
            } else if (binary[1] > linear[1]) {
                System.out.println("  Linear search used "
                        + (binary[1] - linear[1]) + " fewer comparisons.");
                System.out.println("  (Unusual case: the target was near the front.)");
            } else {
                System.out.println("  Both searches used the same number of comparisons.");
            }
        }
    }

    // Returns {index, comparisons}; index is -1 when the value is not there.
    public static int[] binarySearch(int[] sorted, int target) {
        int low = 0;
        int high = sorted.length - 1;
        int comparisons = 0;

        while (low <= high) {
            int middle = (low + high) / 2;
            comparisons++;
            if (sorted[middle] == target) {
                return new int[] {middle, comparisons};
            } else if (sorted[middle] < target) {
                low = middle + 1;       // target is in the right half
            } else {
                high = middle - 1;      // target is in the left half
            }
        }
        return new int[] {-1, comparisons};
    }

    // Returns {index, comparisons}; index is -1 when the value is not there.
    public static int[] linearSearch(int[] numbers, int target) {
        int comparisons = 0;
        for (int i = 0; i < numbers.length; i++) {
            comparisons++;
            if (numbers[i] == target) {
                return new int[] {i, comparisons};
            }
        }
        return new int[] {-1, comparisons};
    }

    public static void bubbleSort(int[] numbers) {
        boolean swapped = true;
        int pass = 0;
        while (swapped) {
            swapped = false;
            pass++;
            for (int i = 0; i < numbers.length - pass; i++) {
                if (numbers[i] > numbers[i + 1]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[i + 1];
                    numbers[i + 1] = temp;
                    swapped = true;
                }
            }
        }
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
