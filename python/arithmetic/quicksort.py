#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def quicksort(arr,i,j):
    '''
    @summary: quick sort function
    @param arr:array target
    @param i:leftindex
    @param j:rightindex
    @result: 
    '''
	if i<j:
		base=sort_process(arr,i,j)
		quicksort(arr,i,base-1)
		quicksort(arr,base+1,j)

def sort_process(arr,i,j):
    '''
    @summary: sort process function
    @param arr:array target
    @param i:leftindex
    @param j:rightindex
    @result: index of base
    '''
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