from teach04 import calculate_velocity


class Test_Teach04:
    def test_teach04_1(self):
        m = 5
        g = 9.8
        t = 10
        p = 1.3
        A = .01
        C = .5
        c, velocity = calculate_velocity(m, g, t, p, A, C)
        
        assert c == '0.003'
        assert velocity == '67.512'
