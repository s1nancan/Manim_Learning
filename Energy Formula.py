from turtle import position
from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        
        pe_text = Text("Potential Energy", font_size=32)
        ke_text = Text("Kinetic Energy", font_size=32)
        e_text = Text("Total Energy", font_size=32)
        
        formula_text=MathTex(
            "\\frac{\hbar^{2}}{2m}\\nabla ^{2}\Psi(r)", "+" , "V(r)\Psi(r)", "=" ,"E\Psi(r)"
        )
        
        self.play(Write(formula_text))
        framebox1 = SurroundingRectangle(formula_text[0], buff = .2)
        ke_text.next_to(framebox1,DOWN)
        framebox2 = SurroundingRectangle(formula_text[2], buff = .2)
        pe_text.next_to(framebox2,DOWN)
        framebox3 = SurroundingRectangle(formula_text[4], buff = .2)
        e_text.next_to(framebox3,DOWN)


        self.play(
            Create(framebox1)
        )
        self.add(ke_text)
        self.wait(1)
        self.play(FadeOut(ke_text), run_time=2)
        #self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2)
        )
        self.add(pe_text)
        self.play(FadeOut(pe_text), run_time=2)
        #self.wait()
        self.play(
            ReplacementTransform(framebox2,framebox3)
        )
        self.add(e_text)
        self.play(FadeOut(e_text), run_time=2)
        self.remove(framebox3)
        self.wait()

        #self.play(formula_text.shift(2*UP))
        self.play(formula_text.animate.to_edge(UP+RIGHT))


        points = []
        arrow_up = Arrow(start=[1,-2,0], end=[1,0,0])
        arrow_down = Arrow(start=[3.5,1.5,0], end=[3.5,-2,0])
        pe_text_2 = Text('''Potential\nEnergy''', font_size=22, color=YELLOW)
        ke_text_2 = Text('''Kinetic\nEnergy''', font_size=22, color=YELLOW)
        for x in range(0,11):
            points.append(Dot(point=np.array([-3, 2.5-5*x*x/100 , 0.0]),radius=0.6))
        group = VGroup(*points)
        #anno = Text("Show submobjects one by one")
        #anno.shift(2*DOWN)
        #self.add(anno)
        self.add(arrow_up)
        self.add(arrow_down)
        self.add(pe_text_2.move_to([3.5,2,0]))
        self.add(ke_text_2.move_to([1,2,0]))
        self.play(ShowSubmobjectsOneByOne(group),arrow_up.animate.scale(3),arrow_down.animate.scale(1/3), run_time = 4)


