
class GapBuffer:
    def __init__(self):
        self.main_array = ['_']*50
        self.buffer_length = 10
        self.left_gap = 0
        self.right_gap = 9
    
    def print_buffer(self):
        for x in range(self.buffer_length):
            print(self.main_array[x], end="")
        print("\n")
        # print(self.main_array)

        return
    
    def grow(self, pos):
        temp_main_array = self.main_array[:self.buffer_length]
        for x in range(pos):
            self.main_array[x] = temp_main_array[x]
        
        for x in range(10):
            self.main_array[pos+x] = '_'
        
        for x in range(pos, len(temp_main_array)):
            self.main_array[x+10] = temp_main_array[x]
        
        self.right_gap = self.right_gap + 10
        self.buffer_length = self.buffer_length + 10

        return
    
    def move_left(self, pos):
        while(self.left_gap != pos):
            self.left_gap = self.left_gap - 1
            self.right_gap = self.right_gap - 1
            self.main_array[self.right_gap+1] = self.main_array[self.left_gap]
            self.main_array[self.left_gap] = '_'

        return
    
    def move_right(self, pos):
        while(self.left_gap != pos):
            self.left_gap = self.left_gap + 1
            self.right_gap = self.right_gap + 1
            self.main_array[self.left_gap-1] = self.main_array[self.right_gap]
            self.main_array[self.right_gap] = '_'
        return

    
    def move_gap(self, pos):
        if pos < self.left_gap:
            self.move_left(pos)
        else:
            self.move_right(pos)
        
        return

    
    def insert(self, in_string, pos):
        if self.left_gap != pos:
            self.move_gap(pos)
        
        for x in range(len(in_string)):
            if (self.left_gap == self.right_gap):
                self.grow(pos+x)
            self.main_array[pos+x] = in_string[x]
            self.left_gap = self.left_gap + 1
        


if __name__ == '__main__':
    gp = GapBuffer()
    gp.print_buffer()
    gp.insert("open-genus", 0)
    gp.print_buffer()
    gp.insert("welcome-", 5)
    gp.print_buffer()
