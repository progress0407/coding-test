package codingtest.codility

import java.util.Comparator
import java.util.stream.Collectors
import java.util.stream.Collectors.toList
import java.util.stream.IntStream
import kotlin.streams.toList

class Solution {

    fun solution(A: IntArray): Int {
        val positiveNums: List<Int> = A.toList().stream()
                .filter { it > 0 }
                .sorted(kotlin.Comparator.reverseOrder())
                .collect(toList())
        if (positiveNums.isEmpty()) {
            return 1
        }
        val max = positiveNums[0]
        val removedNums = removeNums(max, positiveNums)

        if (removedNums.isEmpty()) {
            return max + 1
        }

        return removedNums[0]
    }

    private fun removeNums(max: Int, positiveNums: List<Int>): List<Int> {
        var removedNums = IntStream.range(1, max + 1)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .collect(toList())

        for (num in positiveNums) {
            removedNums.remove(num)
        }

        return removedNums.toList()
    }
}

fun main() {
    println(Solution().solution(intArrayOf(1, 2, 3))) // 4
    println(Solution().solution(intArrayOf(-1, -3))) // 1
    println(Solution().solution(intArrayOf(1, 3, 6, 4, 1, 2))) // 5
}
