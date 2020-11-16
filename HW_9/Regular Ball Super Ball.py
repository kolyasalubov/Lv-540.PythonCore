# Create a class Ball.

# Ball objects should accept one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

class Ball(object):
    def __init__(self, type = "regular"):
        self.ball_type = type

ball1 = Ball()
print (ball1.ball_type)