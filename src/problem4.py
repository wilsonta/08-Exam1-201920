"""
Exam 1, problem 4.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Tim Wilson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem4'
    window = rg.RoseWindow(400, 400, title)

    problem4(8, 40, rg.Point(10, 350), window)
    window.close_on_mouse_click()

    # THREE tests on ANOTHER window.
    title = 'Tests 2, 3 and 4 of problem4'
    window = rg.RoseWindow(450, 400, title)

    problem4(5, 50, rg.Point(50, 270), window)
    window.continue_on_mouse_click()

    problem4(20, 10, rg.Point(10, 350), window)
    window.continue_on_mouse_click()

    problem4(3, 100, rg.Point(130, 350), window)
    window.close_on_mouse_click()


def problem4(number_of_stairs, step_size, starting_point, window):
    """
    See   problem4_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- Two positive integers
      -- An rg.Point.
      -- A rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given RoseWindow:
      -- The given starting_point.
      -- A "staircase" of rg.Line objects as DESCRIBED ON THE ATTACHED PDF
            (problem4_picture.pdf).
      -- The last (highest and furthest to the right) point.
           (Draw it as an rg.Point.)
      Must render but   ** NOT close **   the window.

    Type hints:
      :type number_of_stairs:  int
      :type step_size:          int
      :type starting_point:    rg.Point
      :type window:            rg.RoseWindow
    """
    point=starting_point
    point.attach_to(window)
    for k in range(number_of_stairs+1):
        line=rg.Line(point,rg.Point(point.x,point.y-step_size))
        line.color='magenta',3
        line2=rg.Line(rg.Point(point.x,point.y-step_size),rg.Point(point.x+step_size,point.y-step_size))
        line.color='black'
        line.attach_to(window)
        line2.attach_to(window)
        point=rg.Point(point.x + ((k + 1) * step_size), point.y - ((k + 1) * step_size))
        window.render()

    return point
    point.attach_to(window)
    window.close_on_mouse_click
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT: For PARTIAL CREDIT, you can draw just the black "bottoms"
    #            of the stair steps.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
