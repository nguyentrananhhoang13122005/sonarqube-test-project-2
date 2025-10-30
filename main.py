# BUG NGHIÊM TRỌNG: Hai tham số có cùng tên
# SonarCloud CHẮC CHẮN sẽ phát hiện và xếp vào loại Bug.
def my_buggy_function(param, param):
    print("This function has a bug!")

my_buggy_function(1, 2)
