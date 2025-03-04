class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    
    enqueueAll(values) {
        for (let value of values) {
            this.enqueue(value);
        }
    }
    enqueue(value) {
        let newNode = new Node(value);
        if (this.head === null) {
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.size +=1;
    }
    
    dequeue() {
        if (this.head === null) {
            return null;
        }
        let nowNode = this.head;
        this.head = this.head.next;
        this.size -= 1;
        return nowNode.value;
    }
    
    isEmpty() {
        return this.size === 0;
    }
}

function solution(n, words) {
    let usedWords = new Set();
    let queue = new Queue();
    
    queue.enqueueAll(words);
    let preWord = queue.dequeue()
    usedWords.add(preWord);
    let cnt = 1
    while (!queue.isEmpty()) {
        cnt += 1
        let word = queue.dequeue()
        if ((word[0] !== preWord[preWord.length - 1]) || usedWords.has(word)) {
            let person = (cnt - 1) % n + 1;
            let turn = Math.ceil(cnt / n);
            return [person, turn]
        }
        
        preWord = word
        usedWords.add(word)
    }
    return [0, 0];
}