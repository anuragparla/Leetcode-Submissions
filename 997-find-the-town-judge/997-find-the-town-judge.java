class Solution {
    public int findJudge(int n, int[][] trust) {
         /*
         Logic used : In graph there is a concept called innodes and outnodes.
         Innodes are the number of nodes trusting a single node and outnodes
         are the nodes emitted from a particular node i.e nodes being trusted
         by the current node. Here innodes are the people trusting a particular
         node (judge) and outnodes are a person trusting many other persons.
         
         */ 
        int[] judge = new int[n+1];
        for (int[] person : trust) {
            judge[person[0]] --;
            judge[person[1]] ++;
        }
        for ( int i = 1; i<judge.length;i++) {
            if(judge[i] == n-1) {
                return i;
            }
        }
        return -1;
    }
}