function solution(diffs, times, limit) {
    let s = 1;
    let e = 100000+ 1;
    while (e > s) {
        let chk_level = Math.floor((e + s) / 2);
        let chk_time = 0;
        
        for (let i = 0; i < diffs.length; i++) {
            let time_cur = times[i];
            let time_pre = 0
            if (i !== 0) {
                time_pre = times[i - 1]
            }
            let used_time = time_cur + Math.max(0, (diffs[i] - chk_level)) * (time_cur + time_pre);
            chk_time += used_time;
        }

        if (chk_time <= limit) {
            e = chk_level;
        } else {
            s = chk_level + 1;
        }
    }
    return s;
}
