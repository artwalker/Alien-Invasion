class Settings():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self): # 最开始时使用了一个_导致属性赋值失败，应该是两个_
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)