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
        int N = in.nextInt(); // the total number of nodes in the level, including the gateways
        int L = in.nextInt(); // the number of links
        int E = in.nextInt(); // the number of exit gateways

        boolean[][] path = new boolean[N][N]; // container for links
        int[] gates = new int[E]; // container for gateways

        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt(); // N1 and N2 defines a link between these nodes
            int N2 = in.nextInt();

            path[N1][N2] = true; // confirms a link between N1 and N2 (and vice versa) exists
            path[N2][N1] = true;
        }
        for (int i = 0; i < E; i++) {
            int EI = in.nextInt(); // the index of a gateway node
            gates[i] = EI; // stores index of all gateway nodes
        }

        // game loop
        while (true) {
            int SI = in.nextInt(); // The index of the node on which the Bobnet agent is positioned this turn

            Queue<Integer> gateNode = new LinkedList<>(); // container for gateway nodes
            boolean[] isNear = new boolean[N]; // container for checking links

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");

            for (int i = 0; i < gates.length; i++) { // storing gateway nodes indeces
                gateNode.add(gates[i]);
                isNear[gates[i]] = true; // node is near gateway
            }

            while (!gateNode.isEmpty()) { // while there are still active nodes
                int C1 = gateNode.remove(); // last gateway node in list
                for (int C2 = 0; C2 < path.length; C2++) { // while there are still links
                    if (path[C1][C2]){ // if link between two nodes exists
                        if (!isNear[C2]) { // if C2 node is not near gateway
                            gateNode.add(C2); 
                            isNear[C2] = true; // consider breaking link
                        }
                        if (C2 == SI) { // agent is near gateway or undeleted node near gateway
                            System.out.println(C1 + " " + C2); // link bet. gateway node to neighbor node where agent is
                            path[C2][C1] = false; // break link between node and gateway node
                            path[C1][C2] = false; // break link between nodes
                            gateNode.clear();
                            break;
                        }
                    }
                }
            }

            // Example: 0 1 are the indices of the nodes you wish to sever the link between
            // System.out.println(C1 + " " + C2);


        }
    }
}

// Reference for BFS: https://www.youtube.com/watch?v=y4dWsmd7Gqg