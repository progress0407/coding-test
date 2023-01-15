package gradle.cotingtest.console.codility

import java.util.Arrays


fun solution(A: IntArray, K: Int): IntArray {
    val stack = ArrayDeque(A.toList())
    for (i in 1..K) {
        val last = stack.removeLast()
        stack.addFirst(last)
    }
    return stack.toIntArray()
}

fun main() {
    println(Arrays.toString(solution(intArrayOf(3, 8, 9, 7, 6), 3)))
}