# prac4.py
import os
def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    
    '''
    try:
        file_path = '/Users/a-09/Desktop/yeardream/Python programming base/yeardream_04/'
        print("Input the file name : ",end="")
        filename = input()
        if os.path.exists(file_path) == True:
            print(f"File '{filename}' exists!")
    except FileNotFoundError:
        print("File name does not exits")
    '''
    
    try:
        file_name = input("Enter the file name: ")
        with open(file_name, 'r') as file:
            print(f"{file.name} exits!")
    except FileNotFoundError:
        print("File not found try again.")

if __name__ == "__main__":
    read_file()
