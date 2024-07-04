# import display

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

row = ['row1','row2','row3']
old_val = ''
index = [1,2,3]

sym = ['X', 'O']

def display():
    print(row1)
    print(row2)
    print(row3)


def check_for_winner():
    return ((row1[0] == row1[1] == row1[2] == 'X') or (row1[0] == row1[1] == row1[2] == 'O')
        or(row2[0] == row2[1] == row2[2] == 'X') or (row2[0] == row2[1] == row2[2] == 'O')
        or(row3[0] == row3[1] == row3[2] == 'X') or (row3[0] == row3[1] == row3[2] == 'O')
        or(row1[0] == row2[1] == row3[2] == 'X') or (row1[0] == row2[1] == row3[2] == 'O')
        or (row1[2] == row2[1] == row3[0] == 'X') or (row1[2] == row2[1] == row3[0] == 'O')
        or(row1[0] == row2[0] == row3[0] == 'X') or (row1[0] == row2[0] == row3[0] == 'O')
        or (row1[1] == row2[1] == row3[1] == 'X') or (row1[1] == row2[1] == row3[1] == 'O')
        or (row1[2] == row2[2] == row3[2] == 'X') or (row1[2] == row2[2] == row3[2] == 'O'))

print("Here is the empty board for tic-tok :: ")
display()
inp = 'Y'

while inp == 'Y' or inp == 'y':
    user_row = input('Enter the row in which you want to enter : ')

    if user_row.strip() in row:
        if user_row == 'row1':
            user_row = row1
        elif user_row == 'row2':
            user_row = row2
        else:
            user_row = row3
        index_position = int(input('Enter the position at which input to be enter: '))
        if index_position in index:

            val = input("Enter the value between X, O :")
            val = val.strip()
            if old_val != val :
                # if  val == 'X' or val == 'O':

                    if val in sym:
                        if user_row[index_position-1] == ' ':
                            old_val = val
                            # user_row = list(user_row)
                            print(user_row, index_position, val)
                            user_row[index_position-1] = val

                            print(user_row[index_position-1])

                            display()
                            if check_for_winner():
                                print('Congratulations!!! --You Won--')
                                row1 = [' ',' ',' ']
                                row2 = [' ',' ',' ']
                                row3 = [' ',' ',' ']
                                old_val = ''

                        else:
                            print('Already user has chosen for that position')
                    else:
                        print("Enter the valid value between X, O !!")
                # else:
                #     print('Enter valid value!!')
            else:
                print("Already choosen that symbol!!")
        else:
            print("Enter valid position")
    else:
        print("Enter valid row!!")
    if not check_for_winner():
        print("Chance for Other User:: ")
    inp = input('Do you want to continue Playing Y or N:: ')

print("Thank you for playing!!")





