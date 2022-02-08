class Solution {
    private int sumDigits(int num){  
        int sum=0;
        while(num!=0){
            int rem=num%10;
            sum+=rem;
            num=num/10;
        }
        return sum;
    }
    public int addDigits(int num) {
        if(num>=0 && num<=9)             
            return num;
        
        while(num<0 || num>9){
            num=sumDigits(num);
        }
        
        return num;
}
}