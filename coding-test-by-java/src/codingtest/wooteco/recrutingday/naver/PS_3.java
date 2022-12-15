package codingtest.wooteco.recrutingday.naver;

class PS_3 {

    public static void main(String[] args) {
        Solution sol = new Solution();
        sol.solution(0, 100);
    }

    static class Solution {

        /**
         * 상황의 복잡성 대비 문제 풀이에 필요한 알고리즘이 단순하다고 생각되어...
         * 아래와 같이 제출합니다...
         */
        public int[] solution(int a, int b) {
            if (a == 0 && b == 0) {
                return new int[]{1, 0}; // A의 패배이므로, B의 승리
            } else if (a == 0 || b == 0) { // 더미 어느 한쪽만 동전이 없는 경우
                return new int[]{0, 1};
            } else { // 더미에 항상 동전이 있는 경우
                return new int[]{1, 2};
            }
        }
    }
}
