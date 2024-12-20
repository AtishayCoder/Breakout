def collides_with_paddle(turtle, paddle):
    # Get the turtle's coordinates
    turtle_x, turtle_y = turtle.position()

    # Get the paddle's coordinates and dimensions
    paddle_x, paddle_y = paddle.position()
    paddle_width = paddle.width
    paddle_height = paddle.height

    # Calculate the distance between the turtle and the paddle's center
    distance = ((turtle_x - paddle_x) ** 2 + (turtle_y - paddle_y) ** 2) ** 0.5

    if distance <= turtle.radius + paddle_width / 2 + paddle_height / 2:
        return True
    else:
        return False


BRICK_POSITIONS = [(0, 200), (23, 200), (-23, 200), (46, 200), (-46, 200), (69, 200), (-69, 200), (92, 200), (-92, 200),
                   (115, 200), (-115, 200), (138, 200), (-138, 200), (161, 200), (-161, 200), (184, 200), (-184, 200),
                   (207, 200), (-230, 200),
                   (-207, 200), (230, 200),

                   (0, 225), (23, 225), (-23, 225), (46, 225), (-46, 225), (69, 225), (-69, 225), (92, 225), (-92, 225),
                   (115, 225), (-115, 225), (138, 225), (-138, 225), (161, 225), (-161, 225), (184, 225), (-184, 225),
                   (207, 225), (-230, 225),
                   (-207, 225), (230, 225),

                   (0, 175), (23, 175), (-23, 175), (46, 175), (-46, 175), (69, 175), (-69, 175), (92, 175), (-92, 175),
                   (115, 175), (-115, 175), (138, 175), (-138, 175), (161, 175), (-161, 175), (184, 175), (-184, 175),
                   (207, 175), (-230, 175),
                   (-207, 175), (230, 175),

                   (0, 150), (23, 150), (-23, 150), (46, 150), (-46, 150), (69, 150), (-69, 150), (92, 150), (-92, 150),
                   (115, 150), (-115, 150), (138, 150), (-138, 150), (161, 150), (-161, 150), (184, 150), (-184, 150),
                   (207, 150), (-230, 150),
                   (-207, 150), (230, 150)
                   ]
