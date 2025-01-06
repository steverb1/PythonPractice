from teach04 import calculate_velocity


class Test_Teach04:
    def test_teach04_sphere(self):
        m = 5
        g = 9.8
        t = 10
        p = 1.3
        A = .01
        C = .5
        c, velocity = calculate_velocity(m, g, t, p, A, C)
        
        assert c == '0.003'
        assert velocity == '67.512'

    def test_teach04_bowling_ball_in_water(self):
        m = 7.3
        g = 9.8
        t = 10
        p = 1000
        A = .0366
        C = .5
        c, velocity = calculate_velocity(m, g, t, p, A, C)
        
        assert c == '9.150'
        assert velocity == '2.796'

    def test_teach04_sphere_on_jupiter(self):
        m = 5
        g = 24
        t = 10
        p = 1.3
        A = .01
        C = .5
        c, velocity = calculate_velocity(m, g, t, p, A, C)
        
        assert c == '0.003'
        assert velocity == '137.046'

    def test_teach04_bowling_ball_in_air_terminal_velocity(self):
        m = 7.3
        g = 9.8
        t = 98
        p = 1.3
        A = .0366
        C = .5
        c1, velocity1 = calculate_velocity(m, g, t, p, A, C)

        t = 99
        c2, velocity2 = calculate_velocity(m, g, t, p, A, C)
        
        assert c1 == c2
        assert velocity1 == velocity2
        