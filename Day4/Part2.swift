
import Cocoa

//let inputString = """
//Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
//Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
//Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
//Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
//Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
//Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
//"""

func readFile(inputFile:String) -> String {
    let fileName = inputFile
    let fileURL = try! FileManager.default.url(for:.desktopDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        .appendingPathComponent("coding")
        .appendingPathComponent("adventvy_code")
        .appendingPathComponent("Day4")
    let inputFile = fileURL.appendingPathComponent(fileName).appendingPathExtension("txt")
    
    do{
    let savedData = try String(contentsOf: inputFile)
    return savedData
    } catch {
        return error.localizedDescription
    }
}

let inputString = readFile(inputFile: "input")

var gameArray = inputString.split(separator: "\n")
print(gameArray[0].components(separatedBy: [":" , "|"])[0].replacingOccurrences(of: "Card ", with:""))
var hashMap : [Int : Int] = [:]

for unGame in gameArray {
    let game = Game(gameArray: unGame.components(separatedBy: [":" , "|"]))
    var numberToAdd :Int = 1;
    var pointPerGame = 0
    for point in game.pointString.split(separator: " " ) {
        if (game.checkString+" ").contains(" "+point+" "){
           pointPerGame += 1
        }
    }

    if hashMap.keys.contains(game.gameNumber){
        numberToAdd *= (hashMap[game.gameNumber] ?? 0) + 1
    }
    
//    print("game: \(game.gameNumber) , point: \(pointPerGame)  , number : \(numberToAdd)" )

    if pointPerGame > 0 {
        for element in (game.gameNumber+1)...(pointPerGame+game.gameNumber) {
            hashMap[element] = (hashMap[element] ?? 0) + numberToAdd
        }
    }
    hashMap[game.gameNumber] = (hashMap[game.gameNumber] ?? 0) + 1
//    print(hashMap)
    
}

let sum = hashMap.values
//    .map{$0+1}
    .reduce(0){$0 + $1 }
print("sum: " ,sum)



struct Game {
    let gameNumber  : Int
    let pointString : String
    let checkString : String
    
    init(gameArray : [String]){
        gameNumber = (Int(gameArray[0].replacingOccurrences(of: "Card", with:"").replacingOccurrences(of: " ", with: "")))!
        pointString = gameArray[1]
        checkString = gameArray[2]
    }
    
}
