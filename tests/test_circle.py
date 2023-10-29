import pytest
import source.shapes as shapes
import math

class TestCircle:

    def setup_method(self, method):
        # Setting up method
        self.circle = shapes.Circle(10)
    
    def teardown_method(self, method):
        # Tearing down method
        del self.circle

    def test_area(self):
        result = self.circle.area()
        assert result == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 2 * math.pi * self.circle.radius