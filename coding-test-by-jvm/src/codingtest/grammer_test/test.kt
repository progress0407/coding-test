package codingtest.grammer_test

fun main() {
    var a = 100
    var b = 200

//    a = b.also { b=a }
    run { var temp = a;a = b;b = temp }

    println("a = $a")
    println("b = $b")

    println("hello")
}
