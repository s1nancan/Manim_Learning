from manim import *
import numpy as np

class MathProblem(MovingCameraScene):
    def construct(self):

        N_DOTS = 10
        INIT_NO = 7
        NEXT_NO = INIT_NO * 3 + 1 


        initial_text = Text("Collatz Conjecture", font_size=44)
        subtext = Text("The Simplest Math Problem No One Can Solve", font_size=32).shift(2*DOWN)
        self.play(Write(initial_text))
        self.wait(1)
        self.play(Write(subtext))
        self.play(FadeOut(initial_text),FadeOut(subtext))

        #dots = [Circle(arc_center=np.array([-4.5, 1, 0.]), radius=0.3) for i in range(N_DOTS)]
        dots = [Circle(radius=0.3, color=GREY, fill_opacity=0.7) for i in range(N_DOTS)]
        
        directions = [i*RIGHT for i in range(N_DOTS)]
        #self.add(*dots) # It isn't absolutely necessary
        animations_dots = [ApplyMethod(dot.shift,direction+UP +4.5*LEFT) for dot,direction in zip(dots,directions)]
        #self.play(*animations) # * -> unpacks the list animations
        
        numbers = [Text(str(i+1), color=WHITE, font_size=22) for i in range(N_DOTS)]   
        #self.add(*numbers)
        animations_numbers =[ApplyMethod(number.shift,direction+UP+4.5*LEFT) for number, direction in zip(numbers,directions)]
        #self.add(numbers.shift(directions[2] +UP +4.5*LEFT))

        pick_number = Text('Pick any positive number',font_size=22).shift(2*UP)
        self.play(FadeIn(pick_number))
        self.wait(1)
        self.play(*animations_dots, *animations_numbers)
        self.wait()
        self.play(FadeOut(pick_number))
        fade_out_dots = []
        fade_out_text = []
        for i,(dot,number) in enumerate(zip(dots,numbers)):
            if i!= INIT_NO-1:
                fade_out_dots.append(FadeOut(dot))
                fade_out_text.append(FadeOut(number))
            else:
                main_dot = dot
                main_number = number


        # MAKE SELECTION, FADE OUT DOTS, CHANGE COLORS TO HIGHLIGHT SELECTION
        self.play(*fade_out_dots,*fade_out_text)
        #self.wait()
        self.play(main_number.animate.set_color(YELLOW), main_dot.animate.set_stroke_color(YELLOW))

        # MOVE THE SELECTED DOT TO CENTER, MAKE IT BIGGER
        self.play(main_dot.animate.move_to([0,0,0]), main_number.animate.move_to([0,0,0]) )
        self.play(main_dot.animate.scale(2), main_number.animate.scale(2))

        # MULTIPLY BY 3

        def multip_by_three(coor):
            return Text("x3+1", color = WHITE, font_size=22).next_to(coor,3.5*RIGHT).align_to(coor).scale(2)


        multip_by_3 = multip_by_three(main_dot)
        #self.add(multip_by_3)

        if_odd = Text('If odd: Multiply by 3 and add 1',font_size=32).shift(2*UP)
        self.play(Write(if_odd))
        self.wait(1)
        self.play(main_number.animate.set_color(RED), main_dot.animate.set_stroke_color(RED))
        self.play(Write(multip_by_3), FadeOut(if_odd))

        #MOVE 7 to bottom, FADE IN ANOTHER DOT WITH 21, MAKE DOT ORIGINAL COLOR AGAIN

        self.play(main_dot.animate.shift(3*DOWN,3*LEFT), main_number.animate.shift(3*DOWN,3*LEFT), multip_by_3.animate.shift(3*DOWN,3*LEFT))

        dot_2 = Circle(radius=0.3, color=GREY, fill_opacity=0.7).scale(3/2)
        number_2 = Text(str(22), color=WHITE, font_size=22).scale(3/2)
        arrow_1 = Arrow(start=main_dot, end=[0,0,0], color=WHITE)
        
        self.play(main_number.animate.set_color(WHITE), main_dot.animate.set_stroke_color(GRAY))
        self.play(main_dot.animate.scale(3/4), main_number.animate.scale(3/4),FadeIn(dot_2),
                            FadeOut(multip_by_3),Write(number_2),GrowArrow(arrow_1))


        # DIVIDE BY 2

        
        def divide_by_two(coord):
            return Text("÷2", color = WHITE, font_size=22).next_to(coord,3.5*RIGHT).align_to(coord).scale(2)
        if_even = Text('If even divide by 2',font_size=32).shift(2*UP)
        self.play(Write(if_even))
        self.wait(1)
        divide_by_2 = divide_by_two([0,0,0])#Text("÷2", color = WHITE, font_size=22).next_to([0,0,0],3.5*RIGHT).align_to([0,0,0]).scale(2)
        self.play(Write(divide_by_2), FadeOut(if_even))


        # MOVE EVERYTHING 
        scene_1 = VGroup(main_number, main_dot, dot_2, number_2, arrow_1, divide_by_2)
        animate_scene_1 = [ApplyMethod(element.shift, 2*LEFT+ 2* UP) for element in scene_1]
        self.play(*animate_scene_1)


        dot_3 = Circle(radius=0.3, color=GREY, fill_opacity=0.7).scale(3/2)
        number_3 = Text(str(11), color=WHITE, font_size=22).scale(3/2)
        arrow_2 = Arrow(start=dot_2, end=[0,0,0], color=WHITE)

        self.play(FadeOut(divide_by_2),FadeIn(dot_3),Write(number_3),GrowArrow(arrow_2))


        # STEP 3:
        self.camera.frame.save_state()
                


        def create_multiply_by_3(self, up_move, number, previous_dot):

            multip_by_3 = multip_by_three(previous_dot)
            self.play(Write(multip_by_3))

            previous_pos = previous_dot.get_center()
            next_dot =  Circle(radius=0.3, color=GREY, fill_opacity=0.7).scale(3/2).move_to(previous_pos + up_move)
            next_number = Text(str(number), color=WHITE, font_size=22).scale(3/2).move_to(next_dot.get_center())
            next_arrow = Arrow(start=previous_pos, end=next_dot, color=WHITE)

            # next_dot = Circle(radius=0.3, color=GREY, fill_opacity=0.7).scale(3/2).shift(up_move)
            # next_number = Text(str(number), color=WHITE, font_size=22).scale(3/2).shift(up_move)
            # next_arrow = Arrow(start=previous_dot, end=next_dot, color=WHITE)

            #self.wait()
            self.play(FadeOut(multip_by_3), FadeIn(next_dot),Write(next_number),GrowArrow(next_arrow), self.camera.frame.animate.set(width=10).move_to(next_dot))
            return next_number, next_dot




        def create_divide_by_two(self, down_move, number, previous_dot, zoom_out=True):
            
            divide_by_2 = divide_by_two(previous_dot)
            self.play(Write(divide_by_2))

            previous_pos = previous_dot.get_center()
            next_dot =  Circle(radius=0.3, color=GREY, fill_opacity=0.7).scale(3/2).move_to(previous_pos + down_move)
            next_number = Text(str(number), color=WHITE, font_size=22).scale(3/2).move_to(next_dot.get_center())
            next_arrow = Arrow(start=previous_pos, end=next_dot, color=WHITE)

            #self.wait()
            if zoom_out:
                self.play(FadeOut(divide_by_2), FadeIn(next_dot),Write(next_number),GrowArrow(next_arrow), self.camera.frame.animate.set(width=10).move_to(next_dot))

            else:
                self.play(FadeOut(divide_by_2), FadeIn(next_dot),Write(next_number),GrowArrow(next_arrow))

            return next_number, next_dot

        
        number_4, dot_4 = create_multiply_by_3(self, up_move=4*UP+2*RIGHT, number=34, previous_dot = dot_3)
        number_5, dot_5 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=17, previous_dot = dot_4)
        number_6, dot_6 = create_multiply_by_3(self, up_move=4*UP+2*RIGHT, number=52, previous_dot = dot_5)
        number_7, dot_7 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=26, previous_dot = dot_6)
        number_8, dot_8 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=13, previous_dot = dot_7)
        number_9, dot_9 = create_multiply_by_3(self, up_move=4*UP+2*RIGHT, number=40, previous_dot = dot_8)
        number_10, dot_10 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=20, previous_dot = dot_9)
        number_11, dot_11 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=10, previous_dot = dot_10)
        number_12, dot_12 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=5, previous_dot = dot_11)
        number_13, dot_13 = create_multiply_by_3(self, up_move=4*UP+2*RIGHT, number=16, previous_dot = dot_12)
        number_14, dot_14 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=8, previous_dot = dot_13)
        number_15, dot_15 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=4, previous_dot = dot_14)
        number_16, dot_16 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=2, previous_dot = dot_15)
        number_17, dot_17 = create_divide_by_two(self, down_move=2*DOWN+2*RIGHT, number=1, previous_dot = dot_16, zoom_out=False)

        curved = a = ArcBetweenPoints(dot_17.get_center(), dot_15.get_center(), radius=3, color = RED)
        curved.add_tip()
        #CurvedArrow(start_point=dot_17.get_center(), end_point=dot_16.get_center(), color=RED)
        multip_by_3 = multip_by_three(dot_17)
        self.play(FadeIn(curved), Write(multip_by_3))
        self.wait(2)
        self.play(FadeOut(multip_by_3))

        a1 = Arrow(start=dot_15, end=dot_16, color=RED)
        a2 = Arrow(start=dot_16, end=dot_17, color=RED)
        d1 = divide_by_two(dot_15)
        d2 = divide_by_two(dot_16)
        self.play(FadeIn(a1),Write(d1))
        self.wait()

        self.play(FadeOut(d1),FadeIn(d2),FadeIn(a2))
        self.wait(2)

        self.play(FadeOut(d2))

        self.wait(1)

        self.play(self.camera.frame.animate.set(width=20).move_to(dot_15))
        final_text = Text('Whatever you pick initially,\n you end up in this loop!').move_to(dot_15.get_center()+5*RIGHT+3*UP)
        #print(dot_16.get_center())
        self.play(Write(final_text))












       








