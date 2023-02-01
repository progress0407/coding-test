package codingtest.others;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

import static java.util.function.Function.identity;
import static java.util.stream.Collectors.counting;
import static java.util.stream.Collectors.groupingBy;

public class KHLEE {

    public static void main(String[] args) {
        String str = "1559";

        List<Integer> numbers = new ArrayList<>();
        for (char ch : str.toCharArray()) {
            int number = Integer.parseInt(String.valueOf(ch));
            numbers.add(number);
        }

        Map<Integer, Long> map = 그룹핑하기(numbers);


        Map.Entry<Integer, Long> maxOne = 최댓값_찾기(map);

        System.out.println("map = " + map);
        System.out.println("maxOne = " + maxOne.getKey());
    }

    @NotNull
    private static Map.Entry<Integer, Long> 최댓값_찾기(Map<Integer, Long> map) {

        return map.entrySet().stream()
//                .max((Map.Entry<Integer, Long> e1, Map.Entry<Integer, Long> e2) -> e1.getValue().compareTo(e2.getValue()))
                .max(Map.Entry.comparingByValue())
                .get();
    }

    @NotNull
    private static Map<Integer, Long> 그룹핑하기(List<Integer> numbers) {

        return numbers.stream()
                .collect(groupingBy(identity(), counting()));
    }

    @NotNull
    private static Map.Entry<Integer, Long> 최댓값_찾기_다른_방법(Map<Integer, Long> map) {

        return map.entrySet().stream()
                .max((Map.Entry<Integer, Long> e1, Map.Entry<Integer, Long> e2) -> e1.getValue().compareTo(e2.getValue()))
                .get();
    }
}
