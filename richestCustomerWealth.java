class Solution {
    public int maximumWealth(int[][] accounts) {
        int maximumWealth = 0;
        for (int[] account : accounts) {
            int customerWealth = 0;
            for (int dollars : account) {
                customerWealth += dollars;
            }
            maximumWealth = Math.max(maximumWealth, customerWealth);
        }
        return maximumWealth;
    }
}

