from search import *

CAPACITY = 3

class MissCannibalsVariant(Problem):

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """Define goal state and initialize a problem"""
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
    
    def result(self, state, action):
        # applies action  strings, counts the amount of M or C and tracks whick side of the river it is on
        m_count = action.count('M')
        c_count = action.count('C')
        onLeft = state[2]
        
        # moves from L > R 
        if onLeft == True:
            m_left = state[0] - m_count
            c_left = state[1] - c_count
            onLeft = False
            new_state = (m_left, c_left, onLeft)
        # moves from R > L
        else:
            m_left = state[0] + m_count
            c_left = state[1] + c_count
            onLeft = True
            new_state = (m_left, c_left, onLeft)
        return new_state
    
    def actions(self, state):
        m_left, c_left, onLeft = state
        m_right = self.N1 - m_left
        c_right = self.N2 - c_left

        # All posibilities of actions 
        options_list = ('MCC', 'MMC', 'MMM', 'CCC', 'MC', 'CC', 'MM', 'M', 'C')
        actions_list = []

        for action in options_list: 
            # safety check for capactity of boat 
            if len(action) > CAPACITY:
                continue

            m_boat = action.count('M')
            c_boat = action.count("C")
            # makes sure missionaries cannot be outnumbered 
            boat_ok = (m_boat == 0) or (m_boat >= c_boat)
            if not boat_ok:
                continue

            # computs left and right bank counts based on action changes 
            if onLeft:
                if m_boat > m_left or c_boat > c_left:
                    continue
                new_m_left = m_left - m_boat
                new_c_left = c_left - c_boat
            else: 
                if m_boat > m_right or c_boat > c_right:
                    continue
                new_m_left = m_left + m_boat
                new_c_left = c_left + c_boat
            
            # makes sure the left and right bank are ok 
            left_ok = (new_m_left == 0) or (new_m_left >= new_c_left)
            m_right_new = self.N1 - new_m_left
            c_right_new = self.N2 - new_c_left
            right_ok = (m_right_new == 0) or (m_right_new >= c_right_new)

            if left_ok and right_ok:
                actions_list.append(action)

        return actions_list

if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    # result testing 
    # print(mc.result((4,4,True), 'MC'))
    # print(mc.result((3,3,False), 'MM'))
    # print(mc.result((4,4,True), 'MMM'))

    # actions testing
    # S1 = mc.actions((4,4,True))
    # print(S1)

    path = depth_first_graph_search(mc).solution()
    print(path)

    path = breadth_first_graph_search(mc).solution()
    print(path) 