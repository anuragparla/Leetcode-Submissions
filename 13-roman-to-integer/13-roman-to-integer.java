class Solution {
    public int romanToInt(String s) {
        Map<String,Integer> hm = new HashMap<>();
        hm.put("I",1);
        hm.put("V",5);
        hm.put("X",10);
        hm.put("L",50);
        hm.put("C",100);
        hm.put("D",500);
        hm.put("M",1000);
        hm.put("IV",4);
        hm.put("IX",9);
        hm.put("XL",40);
        hm.put("XC",90);
        hm.put("CD",400);
        hm.put("CM",900);
        int i = 0;
        int sum = 0;
        while(i<s.length()) {
            if(i+1 < s.length() && hm.containsKey(s.substring(i,i+2))) {
                sum +=hm.get(s.substring(i,i+2));
                i+=2;
            }
            
            
            else {
                sum +=hm.get(s.substring(i,i+1));
                i+=1;
            }
        }
        return sum;
    }
}