package gradle.cotingtest.console.codility

import java.lang.RuntimeException

fun solution(A: IntArray): Int {
    val set = A.toSet()
    for (num in set) {
        val matchesNum = A.count { it == num }
        if (matchesNum % 2 == 1) {
            return num
        }
    }
    throw RuntimeException("Data is Not Correct")
}

fun main() {
    println("answer = ${solution(intArrayOf(9, 3, 9, 3, 9, 7, 9))}")
    println("answer = ${solution(intArrayOf(1, 2, 2))}")
}
