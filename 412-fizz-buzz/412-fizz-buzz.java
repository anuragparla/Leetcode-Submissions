class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<>();
        String temp;
        for(int i =1; i<=n; i++) {
             if( i % 3 == 0 && i % 5 == 0) {
            temp = "FizzBuzz";
        }
            else if (i % 3 == 0) {
            temp = "Fizz";
        }
        else if (i % 5 == 0) {
            temp = "Buzz";
        }
        else {
            temp = Integer.toString(i);
        }
           answer.add(temp); 
        }
        return answer;
    }
}