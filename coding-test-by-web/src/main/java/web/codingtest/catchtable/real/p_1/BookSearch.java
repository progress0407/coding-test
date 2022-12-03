package web.codingtest.catchtable.real.p_1;

import java.util.ArrayList;
import java.util.List;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class BookSearch {

    @Bean
    public BookRepository bookRepository() {
        return new BookRepository();
    }

    @Bean
    public RecommendationService recommendationService() {
        return new RecommendationService(bookRepository());
    }
}

class RecommendationService {
    private final BookRepository repository;

    public RecommendationService(BookRepository bookRepository) {
        this.repository = bookRepository;
    }

    public String recommendBook() {
        return repository.getBooks().get(0);
    }
}

class BookRepository {
    public List<String> getBooks() {
        List<String> books = new ArrayList<>();
        books.add("Book");
        books.add("Short book");
        books.add("Long book");

        return books;
    }
}
