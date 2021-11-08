class CState(object):
	def __init__(self, functor) -> None:
		super().__init__()
		self.transitions = []
		self.functor = functor

	def tick(self, dt):
		for transition in self.transitions:
			if transition.check():
				return transition.end
		self.functor(dt)
		return self

class CTransition(object):
	def __init__(self, discriminant) -> None:
		super().__init__()
		self.discriminant = discriminant
		self.end = None

	def test(self) -> bool:
		return bool(self.discriminant)

class CStateMachine(object):
	def __init__(self) -> None:
		super().__init__()
		self.start = None
		self.current = None

	def tick(self, dt):
		self.current = self.current.tick(dt)