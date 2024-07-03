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

print("Here is the empty board for tic-tok :: ")
display()
inp = 'Y'

while inp == 'Y':
    user_row = input('Enter the row in which you want to enter : ')

    if user_row in row:
        if user_row == 'row1':
            user_row = row1
        elif user_row == 'row2':
            user_row = row2
        else:
            user_row = row3
        index_position = int(input('Enter the position at which input to be enter: '))
        if index_position in index:

            val = input("Enter the value between X, O :")
            if old_val != val :
                if  val == 'X' or val == 'O':
                    old_val = val
                    if val in sym:
                        # user_row = list(user_row)
                        print(user_row, index_position, val)
                        user_row[index_position-1] = val

                        print(user_row[index_position-1])

                        display()
                    else:
                        print("Enter the valid value between X, O !!")
                else:
                    print('Enter valid value!!')
            else:
                print("Already choosen that symbol!!")
        else:
            print("Enter valid position")
    else:
        print("Enter valid row!!")

    print("Chance for Other User:: ")
    inp = input('Do you want to continue Playing Y or N:: ')

print("Thank you for playing!!")





