/*
 * BIT235 Object Oriented Programming - Week 4
 * Classes and Objects exercises 2, 4 and 5: the object and its data live here.
 *
 * The method is NOT static: it belongs to the object, not to the class, so it
 * has to be called on an object such as myGreeting.sayHello().
 */
public class Greeting {

    // Field, not a local variable: every Greeting object keeps its own copy.
    String name;

    // Exercise 2 and 3 print "Hi there!" when no name has been given yet.
    // Exercise 4 and 5 print "Hello " plus the name once the field is set.
    public void sayHello() {
        if (name == null || name.isEmpty()) {
            System.out.println("Hi there!");
        } else {
            System.out.println("Hello " + name);
        }
    }
}
