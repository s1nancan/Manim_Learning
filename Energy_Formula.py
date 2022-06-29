#  manim -p Energy_Formula.py energy_conservation
from manim import *

class energy_conservation(Scene):
    def construct(self):
        
        # Text for box labels and formula
        pe_text = Text("Potential Energy", font_size=32)
        ke_text = Text("Kinetic Energy", font_size=32)
        e_text = Text("Total Energy", font_size=32)
        formula_text=MathTex("\\frac{1}{2}mv^2", "+" , "mgh", "=" ,"E")
        
        # Animate formula and boxes
        self.play(Write(formula_text))
        framebox1 = SurroundingRectangle(formula_text[0], buff = .2)
        ke_text.next_to(framebox1,DOWN)
        framebox2 = SurroundingRectangle(formula_text[2], buff = .2)
        pe_text.next_to(framebox2,DOWN)
        framebox3 = SurroundingRectangle(formula_text[4], buff = .2)
        e_text.next_to(framebox3,DOWN)


        # Creaate first framebox, and display the initial text, remove text
        self.play(Create(framebox1))
        self.add(ke_text)
        self.wait(1)
        self.play(FadeOut(ke_text), run_time=2)

        # Move framebox to second position, and display the second text, remove text
        self.play(ReplacementTransform(framebox1,framebox2))
        self.add(pe_text)
        self.play(FadeOut(pe_text), run_time=2)

        # Move framebox to third position, and display the last text, remove text
        self.play(ReplacementTransform(framebox2,framebox3))
        self.add(e_text)
        self.play(FadeOut(e_text), run_time=2)
        self.remove(framebox3)
        self.wait()

        # Move formula to top
        self.play(formula_text.animate.to_edge(UP))

        # Define: points, arrows and new text to be displayed
        points = []
        arrow_up = Arrow(start=[-1,-2,0], end=[-1,0,0])
        arrow_down = Arrow(start=[1,1.5,0], end=[1,-2,0])
        pe_text_2 = Text('''Potential\nEnergy''', font_size=22, color=YELLOW)
        ke_text_2 = Text('''Kinetic\nEnergy''', font_size=22, color=YELLOW)

        # Create many points to simulate free fall. 
        for x in range(0,90):
            points.append(Dot(point=np.array([0, 1-5*x*x/10000 , 0.0]),radius=0.4))
        group = VGroup(*points)

        # Add arrows, text and animate all points
        self.add(arrow_up)
        self.add(arrow_down)
        self.add(pe_text_2.move_to([1,2,0]))
        self.add(ke_text_2.move_to([-1,2,0]))
        self.play(ShowSubmobjectsOneByOne(group),arrow_up.animate.scale(3),arrow_down.animate.scale(1/3), run_time = 4)


