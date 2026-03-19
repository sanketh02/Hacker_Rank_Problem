if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    records.sort(key=lambda x: x[1])
    
    lowest = records[0][1]
    
    second_lowest = 0
    for rec in records:
        if rec[1] > lowest:
            second_lowest = rec[1]
            break
    
    second = []
    for rec in records:
        if rec[1] == second_lowest:
            second.append(rec)
    
    second.sort(key=lambda x:x[0])
    
    for k in second:
        print(k[0])
