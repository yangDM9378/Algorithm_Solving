def solution(files):
    answer = []
    files_apart = []

    for file in files:
        file_apart = []
        file_apart.append(file)
        for i in range(len(file)):
            if file[i].isdigit():
                num_start = i
                break
        file_apart.append(file[:num_start].upper())
        
        # Fix the numeric part extraction
        num_end = num_start + 1
        while num_end < len(file) and file[num_end].isdigit():
            num_end += 1
        file_apart.append(int(file[num_start:num_end]))

        files_apart.append(file_apart)

    files_sort = sorted(files_apart, key=lambda x: (x[1], x[2]))
    
    for file_sort in files_sort:
        answer.append(file_sort[0])

    return answer