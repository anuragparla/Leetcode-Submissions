class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack();
        for ( int i = 0; i < s.length(); i++) {
            if( s.charAt(i) == '(' || s.charAt(i) =='{' || s.charAt(i) == '[') {
                
                st.push(s.charAt(i));
                System.out.println(s.charAt(i)+"is pushed");
            }
            else {
                switch (s.charAt(i)) {
                    case ')':
                        
                        if(( st.isEmpty() || st.pop() != '('))
                            return false;
                        break;
                    case '}':
                        if((st.isEmpty() || st.pop() != '{'))
                        {
                            System.out.println("breaking here at 18");
                            return false;
                        }
                        break;
                    case ']':
                        if((st.isEmpty() || st.pop() != '['))
                            return false;
                        break;
                    default:
                        return false;
                }  
            }
        }
        if(st.isEmpty())
        {
            System.out.println("is empty");
            return true;
        }
        return false;
    }
}