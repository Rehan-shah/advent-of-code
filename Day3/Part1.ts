
const file = Bun.file("./input.txt")


const inputString = await file.text();

// const inputString = `467..114..
// ...*......
// ..35..633.
// ......#...
// 617*......
// .....&.58.
// ..592.....
// ......755.
// ...$.*....
// .664.598.`

const list:string[][] = inputString.split("\n").map( e => e.split(""))


String.prototype.isDigit = function (): boolean {
    return !Number.isNaN(Number(this.toString()))
}


String.prototype.isSymbol = function (): boolean {
    const re = /[^\w\s.]/g;
    return re.test(this.toString())
}


const checkNearBy = (x: number , y : number ):boolean => {
    const arr = [-1 ,0 ,1]
    let isSymbolNearBy = false
    for(let i = 0 ; i < arr.length ; i++){
        for(let j = 0 ; j < arr.length ;j++ ){
            try {
                if(list[x + arr[i]][y + arr[j]].isSymbol() ){
                    isSymbolNearBy = true
                }
                }catch{}

        }

    }

    return isSymbolNearBy
}


let sum = 0
let number = ""
let addNumer = false


list.forEach((row , i) => {
    row.forEach((col ,j) => {
        if (col.isDigit()){
            number += col
            if (checkNearBy(i , j)){
                addNumer = true
            }
        }else {
            if (addNumer){
                hi.push(number)
                sum += parseInt(number)
            }
            addNumer = false
            number = ""
        }
    })
})




console.log( "sum: ",sum)
