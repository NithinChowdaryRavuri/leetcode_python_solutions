class Solution(object):
    def maximum69Number(self, num):
        num_string = str(num)

        for i in range(len(num_string)):
            if num_string[i] == "6":
                new_num = num_string[:i] + "9" + num_string[i + 1:]
                return (int(new_num))

        return num