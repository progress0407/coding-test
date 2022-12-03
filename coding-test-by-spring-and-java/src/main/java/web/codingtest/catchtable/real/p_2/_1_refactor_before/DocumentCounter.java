package web.codingtest.catchtable.real.p_2._1_refactor_before;

public class DocumentCounter {

    public static abstract class AbstractDocumentCounter {
        private int count = 0;
        private int increment;

        public AbstractDocumentCounter(int increment) {
            this.increment = increment;
        }

        protected int getAndIncrement() {
            this.count += this.increment;
            return this.count;
        }

        public abstract String getNewDocumentName();
    }

    public static class DocumentNameCreator extends AbstractDocumentCounter {
        private String prefix;

        public DocumentNameCreator(int increment, String prefix) {
            super(increment);
            this.prefix = prefix;
        }

        public String getNewDocumentName() {
            return prefix + getAndIncrement();
        }
    }

    public static void main(String[] args) {
        DocumentNameCreator documentNameCreator = new DocumentNameCreator(4, "hello-");
        final String newDocumentName = documentNameCreator.getNewDocumentName();
        System.out.println("newDocumentName = " + newDocumentName);
    }
}
