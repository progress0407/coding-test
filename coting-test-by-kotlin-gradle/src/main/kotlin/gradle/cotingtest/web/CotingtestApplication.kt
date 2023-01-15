package gradle.cotingtest.web

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class CotingtestApplication

fun main(args: Array<String>) {
	runApplication<CotingtestApplication>(*args)
}
