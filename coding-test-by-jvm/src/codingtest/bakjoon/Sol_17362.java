package codingtest.bakjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashMap;

import static java.lang.System.out;

public class Sol_17362 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String input = br.readLine();

        int num = Integer.parseInt(input);

        LinkedHashMap<Integer, Integer> map = new LinkedHashMap<>();

        map.put(1, 1);

        map.put(2, 2);
        map.put(0, 2);

        map.put(3, 3);
        map.put(7, 3);

        map.put(4, 4);
        map.put(6, 4);

        map.put(5, 5);


        Integer result = map.get(num);

        out.println(result);

        br.close();
    }
}
