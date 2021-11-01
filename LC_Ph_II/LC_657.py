class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        init_pos = [0, 0]

        for move in moves:
            if move == 'R':
                init_pos[0] = init_pos[0] + 1
            elif move == 'L':
                init_pos[0] = init_pos[0] - 1
            elif move == 'U':
                init_pos[1] = init_pos[1] + 1
            elif move == 'D':
                init_pos[1] = init_pos[1] - 1

        if init_pos == [0, 0]:
            return True
        return False

