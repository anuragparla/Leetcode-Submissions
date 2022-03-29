class Solution {
    private void helper(int[][]image,int r , int c, int color, int startingVal) {
        int nr = image.length;
        int nc = image[0].length;
        int clr = color;
        int sr = r;
        int sc = c;
        if(sr>=nr || sc>=nc || sr<0 || sc<0)
            return;
        if(image[sr][sc] == startingVal)  
            image[sr][sc] = clr;
        else 
            return;
        
        helper(image,sr-1,sc,clr,startingVal);
        helper(image,sr+1,sc,clr,startingVal);
        helper(image,sr,sc-1,clr,startingVal);
        helper(image,sr,sc+1,clr,startingVal);
        //return image;
        
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int nr = image.length;
        int nc = image[0].length;
        if (nc == 0)
            return image;
        else if (image[sr][sc] == newColor)
            return image;
        int r = sr;
        int c = sc;
        int color = newColor;
        int startingVal = image[sr][sc];
        //for(int i = 0;)
        helper(image,r,c,color,startingVal);
        return image;
    }
}