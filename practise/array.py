def array(arr: list[int]) -> None:
    for i in arr:
        print(i, end=' ')
    print()
    arr.append(6)  # Adding an element to the end of the array
    print(arr)
    print(max(arr))
    print(min(arr))
    print(sum(arr))

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    array(arr)

# array([100, 200, 300, 400, 500])