class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        
    int[] passengersAt = new int[10001];

	for (int[] trip : trips) {
		int start = trip[1];
		int end = trip[2];

		passengersAt[start] += trip[0];
		passengersAt[end] -= trip[0];
	}

	int passengers = 0;
	for (int count : passengersAt) {
		passengers += count;

		if (passengers > capacity) return false;
	}

	return true;
}
}