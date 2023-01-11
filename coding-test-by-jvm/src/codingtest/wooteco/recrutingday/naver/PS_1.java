package codingtest.wooteco.recrutingday.naver;

import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;

import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

class PS_1 {

    public static void main(String[] args) {
        Solution sol = new Solution();
//        sol.solution(new String[]{
//                "DS7651 A0",
//                "CA0055 D+",
//                "AI5543 C0",
//                "OS1808 B-",
//                "DS7651 B+",
//                "AI0001 F",
//                "DB0001 B-",
//                "AI5543 D+",
//                "DS7651 A+",
//                "OS1808 B-"
//        });

        sol.solution(new String[]{"DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"});
    }

    static class Solution {

        public String[] solution(String[] inputData) {
            List<SubjectGrade> subjectGradeList = createSubjectGrades(inputData);

            arrangeSubject(subjectGradeList);

            return createResultStrings(subjectGradeList);
        }

        private List<SubjectGrade> createSubjectGrades(String[] inputGrades) {
            List<SubjectGrade> subjectGradeList = new LinkedList<>();

            int order = 1;
            for (String inputGrade : inputGrades) {
                subjectGradeList.add(new SubjectGrade(inputGrade, order++));
            }

            return subjectGradeList;
        }

        private void arrangeSubject(List<SubjectGrade> subjectGradeList) {
            int index = 0;
            while (true) {
                SubjectGrade peekOne = subjectGradeList.get(index);
                long subjectMatchesCount = countIdMatches(subjectGradeList, peekOne);
                if (subjectMatchesCount >= 2) {
                    SubjectGrade max = findMax(subjectGradeList, peekOne);
                    List<SubjectGrade> removes = findRemoves(subjectGradeList, max);
                    removeDuplicated(subjectGradeList, index, max, removes);
                }
                int lastIndex = subjectGradeList.size() - 1;
                index++;
                if (index >= lastIndex) {
                    break;
                }
            }
        }

        private long countIdMatches(List<SubjectGrade> subjectGradeList, SubjectGrade peekOne) {
            return subjectGradeList.stream()
                    .filter(it -> it.equalsId(peekOne))
                    .count();
        }

        private SubjectGrade findMax(List<SubjectGrade> subjectGradeList, SubjectGrade peekOne) {
            return subjectGradeList.stream()
                    .filter(it -> it.equalsId(peekOne))
                    .max((o1, o2) -> o2.getGrade().compareTo(o1.getGrade()))
                    .get();
        }

        private List<SubjectGrade> findRemoves(List<SubjectGrade> subjectGradeList, SubjectGrade max) {
            return subjectGradeList.stream()
                    .filter(it -> it.equalsId(max))
                    .collect(toList());
        }

        private void removeDuplicated(List<SubjectGrade> subjectGradeList,
                                      int i,
                                      SubjectGrade max,
                                      List<SubjectGrade> removes) {
            for (SubjectGrade removeOne : removes) {
                subjectGradeList.remove(removeOne);
            }
            subjectGradeList.add(i, max);
        }

        private String[] createResultStrings(List<SubjectGrade> subjectGradeList) {
            return subjectGradeList.stream()
                    .sorted(comparing(SubjectGrade::getGrade).thenComparing(SubjectGrade::getOrder))
                    .map(SubjectGrade::resultForView)
                    .toArray(String[]::new);
        }

        static class SubjectGrade {
            private final String subjectId;
            private final String grade;
            private final int order;

            public SubjectGrade(String inputGrade, int order) {
                String[] subjectIdAndGrade = inputGrade.split(" ");
                this.subjectId = subjectIdAndGrade[0];
                this.grade = subjectIdAndGrade[1];
                this.order = order;
            }

            public String getGrade() {
                return grade;
            }

            public int getOrder() {
                return order;
            }

            public String resultForView() {
                return subjectId + " " + grade;
            }

            public boolean equalsId(SubjectGrade other) {
                return subjectId.equals(other.subjectId);
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) {
                    return true;
                }
                if (o == null || getClass() != o.getClass()) {
                    return false;
                }
                SubjectGrade that = (SubjectGrade) o;
                return Objects.equals(subjectId, that.subjectId) && Objects.equals(grade, that.grade);
            }

            @Override
            public int hashCode() {
                return Objects.hash(subjectId, grade);
            }
        }
    }
}
