package gradle.cotingtest.console.codility

import kotlin.math.ceil

fun solution(X: Int, Y: Int, D: Int): Int {
    return ceil((Y-X).toDouble()/D).toInt()
}

fun main() {
    println("answer = ${solution(X = 10, Y = 85, D = 30)}")
}
