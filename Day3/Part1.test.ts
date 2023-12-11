// sum.test.js

import { expect, test } from 'vitest'
import { isSymbol  , isDigit } from "./Part1" 

console.log(isSymbol("."))

test('checks symbool', () => {
    expect(isSymbol(".")).toBe(false)
    expect(isSymbol("?")).toBe(true)
    expect(isSymbol("i")).toBe(false)
    expect(isSymbol("1")).toBe(false)
})



test("check for is the string a digit " ,() => {
    expect(isDigit("?")).toBe(false)
    expect(isDigit("i")).toBe(false)
    expect(isDigit("1")).toBe(true)
})



