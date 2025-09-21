from search import *

class MissCannibalsVariant(Problem):

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """Define goal state and initialize a problem"""
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
    
    def result(self, state, action):
        m_count = action.count('M')
        c_count = action.count('C')
        boat_on_left = state[2]
        
        if boat_on_left == True:
            m_left = state[0] - m_count
            c_left = state[1] - c_count
            boat_on_left = False
            new_state = (m_left, c_left, boat_on_left)
        else:
            m_right = state[0] + m_count
            c_right = state[1] + c_count
            boat_on_left = True
            new_state = (m_right, c_right, boat_on_left)
        return new_state
    
    def actions(self, state):
        return state.actions

if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    # result testing 
    # print(mc.result((4,4,True), 'MC'))
    # print(mc.result((3,3,False), 'MM'))
    # print(mc.result((4,4,True), 'MMM'))

    # actions testing

    # path = depth_first_graph_search(mc).solution()
    # print(path)

    # path = breadth_first_graph_search(mc).solution()
    # print(path) 