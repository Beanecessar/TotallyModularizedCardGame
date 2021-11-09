from weakref import WeakKeyDictionary

class CSignal(object):
	"""
	非线程安全
	"""
	class CSignalWrapper(object):
		def __init__(self, signal, instance) -> None:
			super().__init__()
			self.signal = signal
			self.instance = instance

		def connect(self, functor):
			self.signal.reflections.setdefault(self.instance, [])
			self.signal.reflections[self.instance].append(functor)

		def emit(self, *args):
			for functor in self.signal.reflections[self.instance]:
				functor(*args)

	def __init__(self) -> None:
		super().__init__()
		self.reflections = WeakKeyDictionary()

	def __get__(self, instance, owner):
		return CSignal.CSignalWrapper(self, instance)

	def __set__(self, instance, owner):
		raise ValueError("Signal is read only.")

	def __delete__(self, instance, owner):
		self.reflections.pop(id(instance))

# Test Code
if __name__ == "__main__":
	class TestClass(object):
		TestSignal = CSignal()

	test1 = TestClass()
	test2 = TestClass()

	test1.TestSignal.connect(lambda: setattr(test1, "a", 1))
	test2.TestSignal.connect(lambda: setattr(test2, "a", 2))

	test1.TestSignal.emit()
	test2.TestSignal.emit()

	assert(test1.a == 1)
	assert(test2.a == 2)

	del test1
	del test2

	import gc
	gc.collect()

	assert(len(TestClass.TestSignal.signal.reflections) == 0)

	print("Finish.")