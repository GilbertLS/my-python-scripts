from random import randint

A = [-1,3,4,3,2,3,6,7,11,14,6,4,3,2,3,4,5,6,5,4,8,90,12,11,10,1,0]

def partition2(A, left, right):
	pivotValue = A[right];
	index = left-1;
	count = 1;
	i = left;

	while(i <= right-count):
		while(A[i] == pivotValue and count < right-i):
			switch(A,i,right-count);
			count += 1;

		if(A[i] < pivotValue):
			index += 1;
			switch(A,i,index);

		i += 1;


	for j in range(1,count+1):
		switch(A,j+index,j+right-count);

	return([index,index+count]);


def switch(A, a, b):
	temp = A[a];
	A[a] = A[b];
	A[b] = temp;

def rp(A, left, right):
	i = randint(left,right);
	switch(A,i, right);
	return partition2(A, left, right);

def qs(A,left,right):
	if left < right:
		B = rp(A,left,right);
		qs(A,left,B[0]-1);
		qs(A,B[1],right);

qs(A, 1, len(A)-1);

print(A);