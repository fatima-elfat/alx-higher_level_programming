#!/usr/bin/python3
"""
the module of class Rectangle, inherits from class Base.
"""


from models.base import Base


class Rectangle(Base):
	"""
	Defines class Rectangle.

	Attributes:
		__width
		__height
		__x
		__y
	Inherited attributes:
		id
	"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		Calls super for id, Assign each argument
		width, height, x and y to the right attribute.
		"""
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		"""
		Getter function for width.
		"""
		return self.__width

	@width.setter
	def width(self, value):
		"""
		Setter function for width.

		Arguments:
			value
		Raises:
			TypeError : if value not int.
			ValueError : if value is not > 0.
		"""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		"""
		Getter function for height.
		"""
		return self.__height

	@height.setter
	def height(self, value):
		"""
		Setter function for height.

		Arguments:
			value
		Raises:
			TypeError : if value not int.
			ValueError : if value is not > 0.
		"""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value

	@property
	def x(self):
		"""
		Getter function for x.
		"""
		return self.__x

	@x.setter
	def x(self, value):
		"""
		Setter function for x.

		Arguments:
			value
		Raises:
			TypeError : if value not int.
			ValueError : if value is not >= 0.
		"""
		if type(value) is not int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		"""
		Getter function for y.
		"""
		return self.__y

	@y.setter
	def y(self, value):
		"""
		Setter function for y.

		Arguments:
			value
		Raises:
			TypeError : if value not int.
			ValueError : if value is not >= 0.
		"""
		if type(value) is not int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

	def area(self):
		"""
		Calculates the value of area.

		Return: the value of area.
		"""
		return self.__width * self.__height

	def display(self):
		"""
		Prints in stdout the Rectangle instance
		with the character # -.
		"""
		for i in range(self.__height):
			print("\n" * self.__y +
		 		"\n".join(" " * self.__x + "#" * self.__width))

	def __str__(self):
		"""
		Overrides the __str__ method and prints
		[Rectangle] (<id>) <x>/<y> - <width>/<height>.
		"""
		return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
			self.__class__.__name__,
			self.id,
			self.__x,
			self.__y,
			self.__width,
			self.__height
			)

	def update(self, *args, **kwargs):
		"""
		Assigns and updates the Rectangle.

		Arguments:
			*args : the attribute values.
			**kwargs : the key/value of attributes.
		"""
		if args and len(args) != 0:
			i = 0
			for a in args:
				if i == 0:
					if a is None:
						self.__init__(self.width, self.height, self.x, self.y)
					else:
						self.id = a
				elif i == 1:
					self.width = a
				elif i == 2:
					self.height = a
				elif i == 3:
					self.x = a
				elif i == 4:
					self.y = a
				i += 1
		elif kwargs and len(kwargs) != 0:
			if "id" in kwargs:
				self.id = kwargs["id"]
			if "width" in kwargs:
				self.width = kwargs["width"]
			if "height" in kwargs:
				self.height = kwargs["height"]
			if "x" in kwargs:
				self.x = kwargs["x"]
			if "y" in kwargs:
				self.y = kwargs["y"]

	def to_dictionary(self):
		"""
		Prints the dictionary representation of a Rectangle.
		"""
		dct = {}
		dct["id"] = self.id
		dct["width"] = self.width
		dct["height"] = self.height
		dct["x"] = self.x
		dct["y"] = self.y
		return dct

	