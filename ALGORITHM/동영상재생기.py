def time_to_sec(time_str):
    m, s = map(int,time_str.split(":"))
    return m*60 + s

def sec_to_time(sec):
    return f"{sec//60:02d}:{sec%60:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    if pos >= op_start and pos <= op_end: 
            pos = op_end 
    for command in commands: 
        if command == "prev":
            if pos > 10:
                pos = pos - 10
            else:
                pos = 0
        if command == "next":
            if video_len-pos < 10:
                pos = video_len
            else:
                pos += 10  
        if pos >= op_start and pos <= op_end: 
            pos = op_end
    return sec_to_time(pos)
