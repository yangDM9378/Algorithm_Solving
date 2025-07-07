function solution(phone_book) {
    const hash_number = new Set(phone_book)
    
    for (const number of phone_book) {
        for (let i=0; i < number.length; i++) {
            let pre = number.slice(0,i)
            if (hash_number.has(pre)) {
                return false
            }
        }
    }
    return true
}