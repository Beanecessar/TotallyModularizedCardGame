class CAction(object):
	pass

class CState(object):
	pass

class CStateMachine(object):
	class Event(object):
		Update = 0
	def __init__(self) -> None:
		super().__init__()