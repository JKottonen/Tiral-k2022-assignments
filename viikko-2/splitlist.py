def count(t):
    greatest = t[0]
    smallest = t[0]
    splits = 0
    for i in t:
        if i > greatest:
            greatest = i
            splits += 1
        if i <= smallest:
            smallest = i
            splits = 0
        
 
    return splits
    
 
if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([1,2,3,1])) # 0
    print(count([1, 1, 4, 4, 2, 5, 4, 8, 10, 6])) # 0
    print(count([3, 6, 10, 8])) # 2
