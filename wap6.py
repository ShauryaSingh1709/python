#WAP to merge two arrays , then print duplicates.
#example: [1,2,3] + [2,3,4] Merged array: [1,2,3,2,3,4] Duplicates: [2,3]
def shaurya(arr1, arr2):
    merge = arr1 + arr2
    print("Merged array:", merge)
    duplicates = []
    for i in merge:
        if merge.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    print("Duplicates:", duplicates)
shaurya([1,2,3], [2,3,4])