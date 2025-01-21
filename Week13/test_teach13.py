from teach13 import compute_area


class Test_Teach13:
    def test_teach13_square(self):
        shape = 'square'
        side = 5.2
        area = compute_area(shape, side)
        
        assert area == 27.04

    def test_teach13_rectangle(self):
        shape = 'rectangle'
        length = 5.5
        width = 3.2
        area = compute_area(shape, length, width)
        
        assert area == 17.6

    def test_teach13_circle(self):
        shape = 'circle'
        radius = 5
        area = compute_area(shape, radius)
        
        assert area == 78.54
