package gradle.cotingtest.console.codility;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;

public class Demo11st {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println("# = " + solution.solution(new int[]{1, 2, 3}));
        System.out.println("# = " + solution.solution(new int[]{-1, -3}));
        System.out.println("# = " + solution.solution(new int[]{1, 3, 6, 4, 1, 2}));
    }

    static class Solution {
        public int solution(int[] A) {
            List<Integer> positiveNums = Arrays.stream(A)
                    .filter(n -> n > 0)
                    .boxed()
                    .sorted(Comparator.reverseOrder())
                    .collect(toList());

            if (positiveNums.isEmpty()) {
                return 1;
            }
            int max = positiveNums.get(0);
            List<Integer> removedNums = removedNums(max, positiveNums);

            if (removedNums.isEmpty()) {
                return max + 1;
            }

            return removedNums.get(0);
        }

        private List<Integer> removedNums(int max, List<Integer> positiveNums) {
            List<Integer> removedNums = IntStream.range(1, max + 1)
                    .boxed()
                    .sorted(Comparator.reverseOrder())
                    .collect(toList());

            for (Integer num : positiveNums) {
                removedNums.remove(num);
            }

            return removedNums;
        }
    }
}
