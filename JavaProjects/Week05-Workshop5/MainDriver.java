/**
 * OOP Concepts Workshop - driver for steps 3 and 6-20.
 *
 * Run:  java MainDriver
 *
 * The steps are printed in order so the output can be matched against the
 * workshop sheet.
 */
public class MainDriver {

    public static void main(String[] args) {

        // Step 3: one ZooKeeper object, displayDetails() called.
        System.out.println("=== Step 3: one ZooKeeper object ===");
        ZooKeeper oneKeeper = new ZooKeeper(1000000, "Nina", "Park");
        oneKeeper.displayDetails();

        // Steps 6-7: one Enclosure and one ZooKeeper, then assign and display.
        System.out.println();
        System.out.println("=== Steps 6-7: one Enclosure with a ZooKeeper assigned ===");
        Enclosure firstEnclosure = new Enclosure("E-001", 6);
        ZooKeeper sam = new ZooKeeper(1000001, "Sam", "Lee");
        firstEnclosure.assignKeeper(sam);
        firstEnclosure.displayDetails();

        // Steps 8-11: several keepers, several enclosures (Cage, Aquarium, Aviary).
        System.out.println();
        System.out.println("=== Steps 8-11: several keepers and several enclosures ===");
        ZooKeeper alex = new ZooKeeper(1000002, "Alex", "Kim");
        ZooKeeper priya = new ZooKeeper(1000003, "Priya", "Nair");

        Cage cage = new Cage("C-101", 4, 25.0);
        Aquarium aquarium = new Aquarium("A-101", 12, "Salt water", 3.5);
        Aviary aviary = new Aviary("V-101", 30, 8.0);

        cage.assignKeeper(sam);
        aquarium.assignKeeper(alex);
        aviary.assignKeeper(priya);

        cage.displayDetails();
        System.out.println();
        aquarium.displayDetails();
        System.out.println();
        aviary.displayDetails();

        // Steps 12-14: an array of Enclosure holding different subclasses.
        System.out.println();
        System.out.println("=== Steps 12-14: an Enclosure[] array holding different types ===");
        Enclosure[] enclosures = new Enclosure[3];
        enclosures[0] = cage;
        enclosures[1] = aquarium;
        enclosures[2] = aviary;
        for (Enclosure e : enclosures) {
            // The variable is Enclosure, but the object's own displayDetails()
            // runs - that is polymorphism (steps 15-16).
            e.displayDetails();
            System.out.println();
        }

        // Steps 17-20: one keeper managing several enclosures.
        System.out.println();
        System.out.println("=== Steps 17-20: one ZooKeeper managing several enclosures ===");
        ZooKeeper manager = new ZooKeeper(1000004, "Dana", "Wong");
        Cage cage2 = new Cage("C-201", 6, 20.0);
        Aquarium aquarium2 = new Aquarium("A-201", 10, "Fresh water", 2.0);
        Aviary aviary2 = new Aviary("V-201", 25, 6.5);

        manager.assignEnclosure(cage2);
        manager.assignEnclosure(aquarium2);
        manager.assignEnclosure(aviary2);

        manager.displayDetails();
        manager.displayEnclosures();

        // Step 20: every keeper and the enclosures they are responsible for.
        System.out.println();
        System.out.println("=== Step 20: every keeper and their enclosures ===");
        ZooKeeper[] keepers = { oneKeeper, sam, alex, priya, manager };
        for (ZooKeeper k : keepers) {
            k.displayEnclosures();
            System.out.println();
        }
    }
}
