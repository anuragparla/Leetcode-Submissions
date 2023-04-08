class Solution {
    public boolean isValid(String s) {
        // () {}[]
        Stack<Character> str = new Stack();
        for(int i=0;i< s.length();i++){
            if((s.charAt(i) == '(') || (s.charAt(i) == '{') || (s.charAt(i) == '['))
            str.push(s.charAt(i));
            else if(str.isEmpty()){
                return false;
            }
            else{
                
                if(s.charAt(i) ==')'){
                    if(str.pop()!='(')
                        return false;
                }
                else if (s.charAt(i) =='}'){
                    if(str.pop()!='{')
                        return false;
                }
                    else if (s.charAt(i) ==']'){
                    if(str.pop()!='[')
                        return false;
                }
                    
                //} 
                    //str.pop();
            
        }
        }
        
        if(str.isEmpty()){
            return true;
        }
        else{
         return false;   
        }
        
    }
    
}


/*
 * Using HashMap to store the pair of opening and closing brackets
 * class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        Map<Character,Character> dict = new HashMap<>();
        dict.put(')','(');
        dict.put(']','[');
        dict.put('}','{');

        for (int i = 0; i<s.length(); i++){
            Character c = s.charAt(i);
            if(dict.containsKey(c)){
                char topElement = st.isEmpty() ? '#' : st.pop();
                if (topElement != dict.get(c)) return false;
            }
            else{
                st.push(c);
            }
        }
        return st.isEmpty();
    }
}
*/
