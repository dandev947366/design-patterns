from enum import Enum

# Define an enumeration for colors with three values: RED, GREEN, and BLUE.
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Define an enumeration for sizes with three values: SMALL, MEDIUM, and LARGE.
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Class representing a product with a name, color, and size.
class Product:
    def __init__(self, name, color, size):
        self.name = name  # Name of the product.
        self.color = color  # Color of the product.
        self.size = size  # Size of the product.

# Base class for all specifications.
class Specification:
    def is_satisfied(self, item):
        pass  # Method to check if the item satisfies the specification.
    
    # Overload the '&' operator to combine specifications using the AndSpecification class.
    def __and__(self, other):
        return AndSpecification(self, other)

# Base class for all filters.
class Filter:
    def filter(self, items, spec):
        pass  # Method to filter items based on the specification.

# Specification to filter products by color.
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color  # Color to filter by.

    def is_satisfied(self, item):
        return item.color == self.color  # Check if the product's color matches the specified color.

# Specification to filter products by size.
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size  # Size to filter by.

    def is_satisfied(self, item):
        return item.size == self.size  # Check if the product's size matches the specified size.

# Specification to combine multiple specifications using logical AND.
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args  # Store the specifications to be combined.

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.args)  # Check if the item satisfies all specifications.

# Filter class to filter items based on a given specification.
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item  # Yield items that satisfy the specification.

# Main block to test the functionality.
if __name__ == '__main__':
    # Create some sample products.
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
        
    # List of all products.
    products = [apple, tree, house]
    bf = BetterFilter()  # Create an instance of the BetterFilter.

    # Filter and print green products.
    print('Green products:')
    green_spec = ColorSpecification(Color.GREEN)  # Create a color specification for green.
    for p in bf.filter(products, green_spec):
        print(f'- {p.name} is green')  # Print the name of green products.

    # Filter and print large products.
    print('Large products:')
    large_spec = SizeSpecification(Size.LARGE)  # Create a size specification for large.
    for p in bf.filter(products, large_spec):
        print(f'- {p.name} is large')  # Print the name of large products.

    # Filter and print large blue products.
    print('Large blue items:')
    # large_blue_spec = AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
    large_blue_spec = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)  # Combine size and color specifications.
    for p in bf.filter(products, large_blue_spec):
        print(f'- {p.name} is large and blue')  # Print the name of large and blue products.



