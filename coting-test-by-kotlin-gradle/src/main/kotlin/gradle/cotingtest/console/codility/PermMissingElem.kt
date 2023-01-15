package gradle.cotingtest.console.codility

import java.util.stream.Collectors
import java.util.stream.IntStream
import kotlin.streams.toList

class PermMissingElem {
    fun solution(A: IntArray): Int {
        val max = A.maxOrNull() ?: 0
        val nums: MutableList<Int> = IntStream.rangeClosed(1, max).toList().toMutableList()
        for (num in A) {
            nums.remove(num)
        }
        return nums[0]
    }
}

fun main() {
    val permMissingElem = PermMissingElem()
    println("answer = ${permMissingElem.solution(intArrayOf(2, 3, 1, 5))}")
}
