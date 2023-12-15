package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strings"
)

func maps[e any](arr []e, mfunc func(e) e) []e {
	newArr := make([]e, len(arr))

	for i, element := range arr {
		newArr[i] = mfunc(element)
	}

	return newArr
}

func mapsN[e any](arr []e, mfunc func(e) []e) [][]e {
	newArr := make([][]e, len(arr))

	for i, element := range arr {
		newArr[i] = mfunc(element)
	}

	return newArr
}

func removeNames(char string) string {
	return strings.Split(char, ":")[1]
}

func getNumber(orginal_arr []int, mat_range [][3]int) [][2]int {
	list := [][2]int{}

	for _, elemeet := range orginal_arr {
		added := false
		for _, arr_range := range mat_range {
			if elemeet < arr_range[2]+arr_range[1] && elemeet >= arr_range[1] {
				diff := int(math.Abs(float64(arr_range[1] - elemeet)))
				soil_num := arr_range[0] + diff
				list = append(list, [2]int{elemeet, soil_num})
				added = true
				break
			}
		}

		if !added {
			list = append(list, [2]int{elemeet, elemeet})
		}
	}

	return list
}

func tupleToInt(mat [][2]int) []int {
	arr := []int{}

	for _, v := range mat {
		arr = append(arr, v[1])
	}

	return arr

}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// real data
	dat, err := os.ReadFile("./input.txt")
	check(err)
	inputString := string(dat)

	// 	// mock data
	// 	inputString := `seeds: 79 14 55 13
	//
	// seed-to-soil map:
	// 50 98 2
	// 52 50 48
	//
	// soil-to-fertilizer map:
	// 0 15 37
	// 37 52 2
	// 39 0 15
	//
	// fertilizer-to-water map:
	// 49 53 8
	// 0 11 42
	// 42 0 7
	// 57 7 4
	//
	// water-to-light map:
	// 88 18 7
	// 18 25 70
	//
	// light-to-temperature map:
	// 45 77 23
	// 81 45 19
	// 68 64 13
	//
	// temperature-to-humidity map:
	// 0 69 1
	// 1 0 69
	//
	// humidity-to-location map:
	// 60 56 37
	// 56 93 4`

	inputArray := strings.Split(inputString, "\n\n")

	only_number := mapsN(maps(inputArray, removeNames), func(e string) []string {
		return strings.Split(e, "\n")
	})

	only_number = maps(only_number, func(e []string) []string {
		returnVal := []string{}
		for _, val := range e {
			if val != "" {
				returnVal = append(returnVal, val)
			}
		}
		return returnVal
	})

	s := StringToInt{}

	seed := s.turnIntoInt(only_number[0][0])

	for i := 1; i < 8; i++ {
		hi, err := s.turnIntoIntArr(only_number[i])

		if err != nil {
			fmt.Println(err)
		} else {
			// fmt.Println(hi)
		}
		part1 := getNumber(seed, hi)
		seed = tupleToInt(part1)
		fmt.Println(part1)
		fmt.Println("------------")
		fmt.Println(seed)

	}

	fmt.Printf("\n The min location : %d", slices.Min(seed))

}
