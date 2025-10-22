'''
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"
or printed:

I
 I
  I
Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I
'''

def draw_stairs(n):
    # Jeśli n <= 0, nic do narysowania
    if n <= 0:
        return ""

    lines = []
    for i in range(n):
        line = " " * i + "I"
        lines.append(line)

    result = "\n".join(lines)
    return result
