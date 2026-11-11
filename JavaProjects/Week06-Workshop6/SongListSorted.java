/*
 * BIT235 Workshop 6 - Exercise 2 (Hard)
 *
 * Modification of Exercise 1: the same two parallel arrays (songs and
 * artists) are now output in alphabetical order of the song title.
 *
 * The hint says bubble sort, so the classic O(n^2) bubble sort is used.
 * Important: whenever two song titles swap places, the artists at the
 * same indexes must swap too, otherwise the pairs break.
 */
public class SongListSorted {

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

        System.out.println("Before sorting (order of the arrays):");
        for (int i = 0; i < songs.length; i++) {
            System.out.println("  " + songs[i] + " - " + artists[i]);
        }

        // Bubble sort: compare neighbours, swap when out of order, repeat
        // until a full pass makes no swaps.
        boolean swapped = true;
        for (int pass = 0; pass < songs.length - 1 && swapped; pass++) {
            swapped = false;
            for (int i = 0; i < songs.length - 1 - pass; i++) {
                if (songs[i].compareToIgnoreCase(songs[i + 1]) > 0) {
                    String tmpSong = songs[i];
                    songs[i] = songs[i + 1];
                    songs[i + 1] = tmpSong;

                    String tmpArtist = artists[i];
                    artists[i] = artists[i + 1];
                    artists[i + 1] = tmpArtist;

                    swapped = true;
                }
            }
        }

        System.out.println();
        System.out.println("After bubble sort (songs alphabetical):");
        for (int i = 0; i < songs.length; i++) {
            System.out.println((i + 1) + ". " + songs[i] + " - " + artists[i]);
        }
        System.out.println();
        System.out.println("Total songs stored: " + songs.length);
    }
}
