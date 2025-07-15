class Q {
    constructor() {
        this.items = [];
        this.head = 0;
    }
    
    enq(item) {
        this.items.push(item);
    }
    
    dq() {
        return this.items[this.head++];
    }
    isEmpty() {
        return this.head >= this.items.length;
    }
}

function solution(numbers, target) {
    const q = new Q;
    q.enq({ sum: 0, index: 0 });

    let count = 0;

    while (!q.isEmpty()) {
        const { sum, index } = q.dq();

        if (index === numbers.length) {
            if (sum === target) {
                count++;
            }
        } else {
            q.enq({ sum: sum + numbers[index], index: index + 1 });
            q.enq({ sum: sum - numbers[index], index: index + 1 });
        }
    }

    return count;
}
