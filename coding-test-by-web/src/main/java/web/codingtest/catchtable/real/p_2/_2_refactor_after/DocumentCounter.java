package web.codingtest.catchtable.real.p_2._2_refactor_after;

public class DocumentCounter {

    public static class Counter {
        private int count = 0;
        private int increment;

        public Counter(int increment) {
            this.increment = increment;
        }

        public int getAndIncrement() {
            this.count += this.increment;
            return this.count;
        }
    }

    public static class DocumentNameCreator {
        private final String prefix;
        private final Counter counter;

        public DocumentNameCreator(Counter counter, String prefix) {
            this.counter = counter;
            this.prefix = prefix;
        }

        public String getNewDocumentName() {
            return prefix + counter.getAndIncrement();
        }
    }

    public static void main(String[] args) {
        final Counter counter = new Counter(4);
        DocumentNameCreator documentNameCreator = new DocumentNameCreator(counter, "hello-");
        final String newDocumentName = documentNameCreator.getNewDocumentName();
        System.out.println("newDocumentName = " + newDocumentName);
    }
}
