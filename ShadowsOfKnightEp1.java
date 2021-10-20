import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int X0 = in.nextInt();
        int Y0 = in.nextInt();

        // values for edges of a section
        int X1 = 0;
        int Y1 = 0;
        int X2 = W - 1;
        int Y2 = H - 1;

        // current position of batman
        int X = X0;
        int Y = Y0;

        // game loop
        while (true) {
            String bombDir = in.next(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");

            // checks to see if combination direction e.g. UR, DR, UL, DL
            for (int i = 0; i < bombDir.length(); i++) {

                // two if statements for combination directions
                if (bombDir.charAt(i) == 'U') {
                    Y2 = Y - 1; // because Y = 0 is in top left
                }
                else if (bombDir.charAt(i) == 'D') {
                    Y1 = Y + 1;
                }

                if (bombDir.charAt(i) == 'L') {
                    X2 = X - 1;
                }
                else if (bombDir.charAt(i) == 'R') {
                    X1 = X + 1;
                }
            }

            // divide section into two
            X = X1 + ((X2 - X1) / 2);
            Y = Y1 + ((Y2 - Y1) / 2);

            // the location of the next window Batman should jump to.
            System.out.println( X + " " + Y );
        }
    }
}

// Reference: https://www.xarg.org/puzzle/codingame/shadows-of-the-knight-episode-1/