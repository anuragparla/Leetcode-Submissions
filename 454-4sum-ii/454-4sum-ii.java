class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        var pairCountBySum = new HashMap<Integer, Integer>();
	for (var num1 : nums1)
		for (var num2 : nums2)
			pairCountBySum.compute(num1 + num2, (k, sumCount) -> sumCount == null ? 1 : sumCount + 1);

	var fourSumCount = 0;
	for (var num3 : nums3)
		for (var num4 : nums4)
			fourSumCount += pairCountBySum.getOrDefault(-(num3 + num4), 0);

	return fourSumCount;
    }
}