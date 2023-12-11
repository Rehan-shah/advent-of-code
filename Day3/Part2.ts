
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

const getDigit = (x : number, y: number) : number => {
    let i = 0
    let num = ""
    try {
    while(list[x][y + i].isDigit()) {
        num += list[x][y+i]
        i ++
    }
    } catch {}
    i  = -1
    try {
    while(list[x][y + i].isDigit()) {
        num = list[x][y+i] + num
        i --
    }
    }catch{}

    return parseInt(num)
}


function getGearRatio(x:number , y:number) : number{
    const aroundList = [-1,0,1]
    let resultArray : number[] = []
    for(let i =0 ; i < aroundList.length ; i++){
        for(let j = 0 ; j < aroundList.length ; j++){
            const xcord = x + aroundList[i]
            const ycord = y + aroundList[j]
            try {
                if(list[xcord][ycord].isDigit()){
                    resultArray.push(getDigit(xcord , ycord ))
                }
            }catch {}
        }
    }
    
    resultArray = resultArray
                    .filter((item  , index) => resultArray.indexOf(item) === index)
    if (resultArray.length >= 2){
        return resultArray.reduce((a , b) => a * b)
    } 
    return 0
}

let sum = 0

list.forEach((row ,i) => {
    row.forEach((item, j) => {
        if (item === "*"){
            console.log(getGearRatio(i , j))
            sum += getGearRatio(i ,j)
        } 
    })
})

console.log( "sum: ",sum)


