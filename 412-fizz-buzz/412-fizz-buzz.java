class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<>();
        String temp;
        
        
        for(int i =1; i<=n; i++) {
             if( i % 3 == 0 && i % 5 == 0) {
            temp = "FizzBuzz";
            answer.add(temp);
        }
            else if (i % 3 == 0) {
            temp = "Fizz";
            answer.add(temp);
        }
        else if (i % 5 == 0) {
            temp = "Buzz";
            answer.add(temp);
        }
        else {
            temp = Integer.toString(i);
            answer.add(temp);
        }
            
        }
        return answer;
    }
}