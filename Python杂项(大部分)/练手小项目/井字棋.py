#coding=UTF-8
theBoard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '}
		  
the_Board={'top-L':1,'top-M':2,'top-R':3,
          'mid-L':4,'mid-M':5,'mid-R':6,
          'low-L':7,'low-M':8,'low-R':9}

ch_eck=[3,4,0,5,6,7,8,9,10]

def printBoard(board):
    print board['top-L']+'|'+board['top-M']+'|'+board['top-R']
    print '-+-+-'
    print board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R']
    print '-+-+-'
    print board['low-L']+'|'+board['low-M']+'|'+board['low-R']
	
turn='X'
for i in range(9):
	printBoard(theBoard)
	print 'Turn for ' + turn + '. Move on which space?'
	move=raw_input()
	theBoard[move]=turn
	if turn=='X':
		ch_eck[the_Board[move]-1]=1
		turn='O'
	else:
		ch_eck[the_Board[move]-1]=2
		turn='X'
	if (ch_eck[0]==ch_eck[1]==ch_eck[2])|(ch_eck[3]==ch_eck[4]==ch_eck[5])|(ch_eck[6]==ch_eck[7]==ch_eck[8])|(ch_eck[0]==ch_eck[3]==ch_eck[6])|(ch_eck[1]==ch_eck[4]==ch_eck[7])|(ch_eck[2]==ch_eck[5]==ch_eck[8])|(ch_eck[0]==ch_eck[4]==ch_eck[8])|(ch_eck[2]==ch_eck[4]==ch_eck[6]):
			if turn=='O':
				print 'The Gamer One is win!'
				break
			else:
				print 'The Gamer Two is win!'
				break
printBoard(theBoard)