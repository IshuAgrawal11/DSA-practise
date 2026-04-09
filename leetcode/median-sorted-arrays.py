class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2

        if n % 2 == 0:
            return (merged[mid] + merged[mid - 1]) / 2.0
        else:
            return float(merged[mid])

# --- DRIVER CODE (How you run it in VS Code) ---

if __name__ == "__main__":
    nums1 = list(map(int, input("Enter numbers separated by space: ").split()))
    nums2 = list(map(int, input("Enter numbers separated by space: ").split()))
    result = Solution().findMedianSortedArrays(nums1, nums2)

    print(f"\nThe merged sorted list is: {sorted(nums1 + nums2)}")
    print(f"The Median is: {result}")