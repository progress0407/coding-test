package web.codingtest.catchtable.real.p_3._2_after_solving;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.stream.Collectors;

public class StringOccurrence {
    public static int getOccurrenceCount(String toSearch, InputStream stream) throws Exception {
        List<String> conversations = deserializeConversations(stream);

        return (int) countWordFromConversation(toSearch, conversations);
    }

    private static long countWordFromConversation(String toSearch, List<String> conversations) {
        return conversations.stream()
                .filter(conversation -> conversation.toLowerCase().contains(toSearch.toLowerCase()))
                .count();
    }

    private static List<String> deserializeConversations(InputStream stream) throws IOException {
        List<String> converations;
        try (InputStreamReader inputStreamReader = new InputStreamReader(stream, StandardCharsets.UTF_8);
             BufferedReader bufferedReader = new BufferedReader(inputStreamReader)) {
            converations = bufferedReader.lines()
                    .collect(Collectors.toList());
        }
        return converations;
    }

    public static void main(String[] args) throws Exception {
//        String msg = "Hey! How are you?\nI am good, how about you?\nI am good too.";
//        String msg = "Hey! How are you?";
//        String msg = "";
//        String msg = "\ngoodgood";
        String msg = "\ngood\ngood";

        try (InputStream stream = new ByteArrayInputStream(msg.getBytes())) {
            System.out.println(getOccurrenceCount("good", stream));
        }
    }
}
