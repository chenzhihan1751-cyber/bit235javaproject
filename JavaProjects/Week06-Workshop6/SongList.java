/*
 * BIT235 Workshop 6 - Exercise 1 (Easy)
 *
 * Store the names of 10 favourite songs in an array of strings and the
 * artist of each song in a second array of strings, then output the list.
 *
 * Two parallel arrays are used: index i in "songs" always belongs to
 * index i in "artists". That keeps the pairing without a Song class.
 */
public class SongList {

    public static void main(String[] args) {

        String[] songs = {
            "Bohemian Rhapsody",
            "Hotel California",
            "Imagine",
            "Billie Jean",
            "Shape of You",
            "Rolling in the Deep",
            "Blinding Lights",
            "Smells Like Teen Spirit",
            "Take On Me",
            "Hey Jude"
        };

        String[] artists = {
            "Queen",
            "Eagles",
            "John Lennon",
            "Michael Jackson",
            "Ed Sheeran",
            "Adele",
            "The Weeknd",
            "Nirvana",
            "A-ha",
            "The Beatles"
        };

        if (songs.length != artists.length) {
            System.out.println("Arrays must be the same length.");
            return;
        }

        System.out.println("My 10 favourite songs");
        System.out.println("----------------------");
        for (int i = 0; i < songs.length; i++) {
            System.out.println((i + 1) + ". " + songs[i] + " - " + artists[i]);
        }
        System.out.println();
        System.out.println("Total songs stored: " + songs.length);
    }
}
