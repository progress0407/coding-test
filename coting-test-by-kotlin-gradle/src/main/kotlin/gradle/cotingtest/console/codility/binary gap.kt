package gradle.cotingtest.console.codility

fun solution(N: Int): Int {
    val binaryString = Integer.toBinaryString(N)
    val binaryArray = binaryString.toCharArray()

    var cnt: Int = 0
    var lastBit = '9'
    val binarySet = mutableSetOf<Int>()
    for (currentBit in binaryArray) {
        if (currentBit == '0') {
            cnt++
        } else if(lastBit == '0' && currentBit == '1') {
            binarySet.add(cnt)
            cnt = 0
        }
        lastBit = currentBit
    }
    return binarySet.maxOrNull() ?: 0
}

fun main() {
    //  1041     1 00000 1 000 1
    println(solution(1041)) // 5
    //  15      1111
    println(solution(15)) // 0
    // 32       1 00000
    println(solution(32)) // 5
}
