class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length ) return false
        let mapS = new Map()
        let mapT = new Map()
        for (let i of s ){
            mapS.set(i , (mapS.has(i) ||0)+1)
        }
        for (let i of t ){
            mapT.set(i , (mapT.has(i) ||0)+1)
        }

        for (let [key, value] of mapS) {
        if (!mapT.has(key) || mapT.get(key) !== value) {
            return false;
        }
    }
    
        return true;
    }
}
