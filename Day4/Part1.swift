import Cocoa

/*let inputString = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""*/

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

var gameArray = inputString.split(separator: "\n" )
var sum = 0

for unGame in gameArray {
    let game = Game(gameArray: unGame.components(separatedBy: [":" , "|"]))
    var pointPerGame = 0
    print(game)
    for point in game.pointString.split(separator: " " ) {
        if (game.checkString+" ").contains(" "+point+" "){
            print("point" , point)
           pointPerGame += 1
        }
    }
    
    if pointPerGame > 0 {
       sum += Int(pow(Double(2) , Double(pointPerGame - 1 )))
    }
}

print("sum is \(sum)")



struct Game {
    let gameNumber  : String
    let pointString : String
    let checkString : String
    
    init(gameArray : [String]){
        gameNumber = gameArray[0]
        pointString = gameArray[1]
        checkString = gameArray[2]
    }
    
}
