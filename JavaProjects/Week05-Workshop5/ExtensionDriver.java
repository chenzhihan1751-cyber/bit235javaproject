/**
 * Workshop Extension - driver from page 3 of the sheet ("How to use it in MainDriver").
 *
 * The class is called ExtensionDriver so that MainDriver can stay the driver for
 * steps 3-20 of the OOP Concepts sheet; the body is the code from the sheet.
 *
 * Run:  java ExtensionDriver
 */
public class ExtensionDriver {

    public static void main(String[] args) {
        EnclosureManager manager = new EnclosureManager();
        Cage c1 = new Cage("C-301", 4, 25.0);
        Aquarium a1 = new Aquarium("A-301", 8, "Salt water", 3.0);
        ZooKeeper z1 = new ZooKeeper(1000001, "Sam", "Lee");
        ZooKeeper z2 = new ZooKeeper(1000002, "Alex", "Kim");

        manager.addEnclosure(c1);
        manager.addEnclosure(a1);
        manager.assignKeeperToEnclosure(0, z1);
        manager.assignKeeperToEnclosure(1, z2);

        System.out.println("Zoo report - " + manager.getEnclosureCount() + " enclosures");
        System.out.println("======================");
        manager.printReport();
    }
}
