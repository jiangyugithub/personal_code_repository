#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def quicksort(arr,i,j):
	"""
	quick sort function
	@param[1]:arr [list] array target
	@param[2]:i    [int]  leftindex
	@param[3]:j    [int]  rightindex
	@return:
	"""
	if i<j:
		base=sort_process(arr,i,j)
		quicksort(arr,i,base-1)
		quicksort(arr,base+1,j)

def sort_process(arr,i,j):
	"""
	sort process function
	@param[1]:arr [list] array target
	@param[2]:i    [int]  leftindex
	@param[3]:j    [int]  rightindex
	@return:index of base
	"""
	base=arr[i]
	while i<j:
		if base<=arr[j]:
			j-=1
		else:
			arr[i]=arr[j]
			i+=1
			arr[j]=arr[i]
	arr[i]=base	
	return i