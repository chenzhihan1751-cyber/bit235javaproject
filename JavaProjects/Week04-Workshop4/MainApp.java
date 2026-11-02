/*
 * BIT235 Object Oriented Programming - Week 4
 * Classes and Objects exercises 1, 3, 5 and 6: the program that uses the
 * Greeting class. Each step of the exercise is marked with a comment.
 */
public class MainApp {

    public static void main(String[] args) {
        // Exercise 1: the first program in the new class.
        System.out.println("Hello from my first class");

        // Exercise 2 and 3: instantiate an object and call its method.
        Greeting firstGreeting = new Greeting();
        firstGreeting.sayHello();

        // Exercise 4 and 5: give the object its own data, then use it.
        Greeting myGreeting = new Greeting();
        myGreeting.name = "Zhihan";
        myGreeting.sayHello();

        // Exercise 6: two objects, each keeps its own name.
        Greeting friendGreeting = new Greeting();
        friendGreeting.name = "Alex";
        myGreeting.sayHello();
        friendGreeting.sayHello();
    }
}
