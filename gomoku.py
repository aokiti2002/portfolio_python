# player1は○、player2は×を使う。ただし、○を1、×を2として扱う。

masu=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
place=['行','列']
result=0
count=0
end=0

def horizontal_func(masu) : 
    global result

    for a in masu :
        if a[0]==a[1]==a[2]==a[3]==a[4]!=0 :
            result=a[0]
            break

def vertical_func(masu) : 
    global result

    for b in range(5) :
        if masu[0][b]==masu[1][b]==masu[2][b]==masu[3][b]==masu[4][b]!=0 :
            result=masu[0][b]
            break

def diagonal_func(masu) : 
    global result

    if masu[0][0]==masu[1][1]==masu[2][2]==masu[3][3]==masu[4][4]!=0 :
        result=masu[0][0]
    elif masu[0][4]==masu[1][3]==masu[2][2]==masu[3][1]==masu[4][0]!=0 :
        result=masu[0][4]

def judgment_func() :
    global result,count,end
    
    count+=1

    if result==1 :
        print('player1の勝利')
        end=1
    elif result==2 :
        print('player2の勝利')
        end=1
    elif count==25 :
        print('引き分け')
        end=1
    
while True :
    p1=[]
    p2=[]

    p1=[int(input('player1:'+i+'=')) for i in place]
    masu[p1[0]-1][p1[1]-1]=1
    for n in masu : 
        print(n)
    horizontal_func(masu)
    vertical_func(masu)
    diagonal_func(masu)
    judgment_func()
    if end==1 :
        break

    p2=[int(input('player2:'+i+'=')) for i in place]
    masu[p2[0]-1][p2[1]-1]=2
    for n in masu : 
        print(n)
    horizontal_func(masu)
    vertical_func(masu)
    diagonal_func(masu)
    judgment_func()
    if end==1 : 
        break