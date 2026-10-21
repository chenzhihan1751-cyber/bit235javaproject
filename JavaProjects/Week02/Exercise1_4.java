/**
 * BIT235 Workshop 2 - Exercise 1.4
 * Compound interest: A = P * (1 + r)^n
 * P = 5000.00, r = 4% per year, n = 10 years
 */
public class Exercise1_4 {
    public static void main(String[] args) {
        double principal = 5000.00;   // P
        double rate = 0.04;           // r = 4% per year
        int years = 10;               // n

        double amount = principal * Math.pow(1 + rate, years);
        double interest = amount - principal;

        System.out.printf("Principal (P)     : $%,.2f%n", principal);
        System.out.printf("Interest rate (r) : %.0f%% per year%n", rate * 100);
        System.out.printf("Time period (n)   : %d years%n", years);
        System.out.printf("Amount (A)        : $%,.2f%n", amount);
        System.out.printf("Interest earned   : $%,.2f%n", interest);
    }
}