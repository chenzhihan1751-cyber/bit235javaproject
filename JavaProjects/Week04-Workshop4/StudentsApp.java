/*
 * BIT235 Object Oriented Programming - Week 4
 * Classes and Objects exercise 7: two Student objects with different IDs.
 */
public class StudentsApp {

    public static void main(String[] args) {
        Student firstStudent = new Student();
        firstStudent.studentId = 1001;

        Student secondStudent = new Student();
        secondStudent.studentId = 1002;

        firstStudent.displayId();
        secondStudent.displayId();
    }
}
