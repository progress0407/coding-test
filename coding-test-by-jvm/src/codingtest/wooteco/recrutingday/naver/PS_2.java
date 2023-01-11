package codingtest.wooteco.recrutingday.naver;

import static java.util.stream.Collectors.toUnmodifiableSet;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

class PS_2 {

    public static void main(String[] args) {
        Solution sol = new Solution();
        sol.solution(new int[]{1, 1, 3, 3, 3, 6}, new int[]{6, 3, 1, 3, 1, 3});
    }

    static class Solution {

        public long[] solution(int[] sequence1, int[] sequence2) {
            Set<Integer> symbols = createSymbols(sequence1);

            List<ResultSet> resultSets = new ArrayList<>();

            for (Integer symbol : symbols) {
                HashSet<Integer> s1Indexes = createIndexes(symbol, sequence1);
                HashSet<Integer> s2Indexes = createIndexes(symbol, sequence2);
                HashSet<Integer> intersection = createIntersection(s1Indexes, s2Indexes);

                for (Object removeOne : intersection) {
                    s1Indexes.remove(removeOne);
                    s2Indexes.remove(removeOne);
                }

                int count = calculateCount(s1Indexes, s2Indexes);

                resultSets.add(new ResultSet(symbol, count));
            }

            ResultSet minOne = extractMinFrom(resultSets);

            return minOne.dataForView();
        }

        private Set<Integer> createSymbols(int[] s1) {
            return Arrays.stream(s1)
                    .boxed()
                    .collect(toUnmodifiableSet());
        }

        private HashSet<Integer> createIndexes(Integer symbol, int[] s1) {
            HashSet<Integer> s1Indexes = new HashSet<>();
            for (int i = 0; i < s1.length; i++) {
                if (symbol.equals(s1[i])) {
                    s1Indexes.add(i);
                }
            }
            return s1Indexes;
        }

        private HashSet<Integer> createIntersection(HashSet<Integer> setA, HashSet<Integer> setB) {
            HashSet<Integer> intersection = new HashSet<>(setA);
            intersection.retainAll(setB);
            return intersection;
        }

        private int calculateCount(HashSet<Integer> s1Indexes, HashSet<Integer> s2Indexes) {
            Iterator<Integer> iter1 = s1Indexes.iterator();
            Iterator<Integer> iter2 = s2Indexes.iterator();

            int count = 0;
            while (iter1.hasNext()) {
                final Integer e1 = iter1.next();
                final Integer e2 = iter2.next();
                count += Math.abs(e1 - e2);
            }
            return count;
        }

        private ResultSet extractMinFrom(List<ResultSet> resultSets) {
            return resultSets.stream()
                    .min(Comparator.comparingLong((ResultSet o) -> o.count).thenComparing((ResultSet o) -> o.number))
                    .get();
        }

        static class ResultSet {
            private final long number;
            private final long count;

            public ResultSet(long number, long count) {
                this.number = number;
                this.count = count;
            }

            public long getCount() {
                return count;
            }

            public long[] dataForView() {
                return new long[]{number, count};
            }
        }
    }
}
