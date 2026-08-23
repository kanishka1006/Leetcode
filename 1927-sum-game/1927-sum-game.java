class Solution {
    public boolean sumGame(String num) {
        int n = num.length();

        int leftSum = 0;
        int rightSum = 0;

        int leftQ = 0;
        int rightQ = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num.charAt(i) == '?')
                leftQ++;
            else
                leftSum += num.charAt(i) - '0';
        }

        for (int i = n / 2; i < n; i++) {
            if (num.charAt(i) == '?')
                rightQ++;
            else
                rightSum += num.charAt(i) - '0';
        }

        // Odd number of '?' -> Alice always wins
        if ((leftQ + rightQ) % 2 == 1) {
            return true;
        }

        // Difference in number of ? on both sides
        int qDiff = leftQ - rightQ;

        // Difference in known sums
        int sumDiff = leftSum - rightSum;

        // Bob wins if he can force the sums to be equal
        return sumDiff * 2 != -qDiff * 9;
    }
}