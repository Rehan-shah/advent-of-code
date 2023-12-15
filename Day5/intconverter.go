package main

import (
	"errors"
	"strconv"
	"strings"
)

type StringToInt struct {
}

func (s StringToInt) turnIntoInt(char string) []int {
	i := strings.Split(char, " ")
	v := []int{}

	for _, val := range i {
		if val != "" {
			is, _ := strconv.Atoi(val)
			v = append(v, is)
		}
	}

	return v
}

func (s StringToInt) turnIntoIntArr(char []string) ([][3]int, error) {
	v := [][3]int{}

	for _, val := range char {
		value, err := s.turnInt3arr(val)
		if err != nil {
			return nil, err
		}
		v = append(v, value)
	}

	return v, nil
}

func (s StringToInt) turnInt3arr(char string) ([3]int, error) {
	arr := strings.Split(char, " ")
	if len(arr) != 3 {
		return [3]int{}, errors.New("does not confome to type")

	}

	intArr := [3]int{}

	for i, val := range arr {
		val, err := strconv.Atoi(val)
		if err != nil {
			return intArr, errors.New("does not confome to type")

		}
		intArr[i] = val
	}

	return intArr, nil
}
