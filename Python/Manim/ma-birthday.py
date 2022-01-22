from manim import *
from pathlib import Path
import os

FLAG="-pql"
SCENE="MyScene"

if __name__ == "__main__":
    script=Path(__file__).resolve()
    os.system(f"manim {script} {SCENE} {FLAG}")

class MyScene(Scene):
    def construct(self):
        text1=MathTex(r"Happy\ Birthday").scale(2).set_color(RED).shift(UP/2)
        text2=MathTex(r"\boldsymbol{MAA}").scale(2).set_color(RED).shift(DOWN/2)
        dot1=Dot(point=ORIGIN+RIGHT*2+DOWN*1,radius=0.01)
        dot1tr=TracedPath(dot1.get_center,dissipating_time=0.5)





        dot2=Dot(point=ORIGIN+RIGHT*3+UP*2,color=YELLOW,radius=0.02)
        dot2tr=TracedPath(dot2.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot3=Dot(point=ORIGIN+RIGHT*3+UP*2,color=RED,radius=0.02)
        dot3tr=TracedPath(dot3.get_center,dissipating_time=0.5).set_color(RED)
        dot4=Dot(point=ORIGIN+RIGHT*3+UP*2,color=YELLOW,radius=0.02)
        dot4tr=TracedPath(dot4.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot5=Dot(point=ORIGIN+RIGHT*3+UP*2,color=RED,radius=0.02)
        dot5tr=TracedPath(dot5.get_center,dissipating_time=0.5).set_color(RED)
        dot6=Dot(point=ORIGIN+RIGHT*3+UP*2,color=YELLOW,radius=0.02)
        dot6tr=TracedPath(dot6.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot7=Dot(point=ORIGIN+RIGHT*3+UP*2,color=RED,radius=0.02)
        dot7tr=TracedPath(dot7.get_center,dissipating_time=0.5).set_color(RED)
        dot8=Dot(point=ORIGIN+RIGHT*3+UP*2,color=YELLOW,radius=0.02)
        dot8tr=TracedPath(dot8.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot9=Dot(point=ORIGIN+RIGHT*3+UP*2,color=RED,radius=0.02)
        dot9tr=TracedPath(dot9.get_center,dissipating_time=0.5).set_color(RED)





        self.play(Write(text1),Write(text2))
        self.add(dot1,dot1tr)
        self.play(dot1.animate.move_to(RIGHT*3+UP*2),run_time=2)
        self.remove(dot1)

        self.add(dot2,dot2tr)
        self.add(dot3,dot3tr)
        self.add(dot4,dot4tr)
        self.add(dot5,dot5tr)
        self.add(dot6,dot6tr)
        self.add(dot7,dot7tr)
        self.add(dot8,dot8tr)
        self.add(dot9,dot9tr)
        self.play(dot2.animate.move_to(RIGHT*3+UP*3),dot3.animate.move_to(RIGHT*4+UP*3),dot4.animate.move_to(RIGHT*4+UP*2),dot5.animate.move_to(RIGHT*4+UP*1),dot6.animate.move_to(RIGHT*3+UP*1),dot7.animate.move_to(RIGHT*2+UP*3),dot8.animate.move_to(RIGHT*2+UP*2),dot9.animate.move_to(RIGHT*2+UP*1),run_time=2)
        self.remove(dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9)
        
        






        dot1=Dot(point=ORIGIN+LEFT*2+DOWN*2,radius=0.01)
        dot1tr=TracedPath(dot1.get_center,dissipating_time=0.5)





        dot2=Dot(point=ORIGIN+LEFT*3+UP*3,color=YELLOW,radius=0.02)
        dot2tr=TracedPath(dot2.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot3=Dot(point=ORIGIN+LEFT*3+UP*3,color=RED,radius=0.02)
        dot3tr=TracedPath(dot3.get_center,dissipating_time=0.5).set_color(RED)
        dot4=Dot(point=ORIGIN+LEFT*3+UP*3,color=YELLOW,radius=0.02)
        dot4tr=TracedPath(dot4.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot5=Dot(point=ORIGIN+LEFT*3+UP*3,color=RED,radius=0.02)
        dot5tr=TracedPath(dot5.get_center,dissipating_time=0.5).set_color(RED)
        dot6=Dot(point=ORIGIN+LEFT*3+UP*3,color=YELLOW,radius=0.02)
        dot6tr=TracedPath(dot6.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot7=Dot(point=ORIGIN+LEFT*3+UP*3,color=RED,radius=0.02)
        dot7tr=TracedPath(dot7.get_center,dissipating_time=0.5).set_color(RED)
        dot8=Dot(point=ORIGIN+LEFT*3+UP*3,color=YELLOW,radius=0.02)
        dot8tr=TracedPath(dot8.get_center,dissipating_time=0.5).set_color(YELLOW)
        dot9=Dot(point=ORIGIN+LEFT*3+UP*3,color=RED,radius=0.02)
        dot9tr=TracedPath(dot9.get_center,dissipating_time=0.5).set_color(RED)


        self.add(dot1,dot1tr)
        self.play(dot1.animate.move_to(LEFT*3+UP*3),run_time=2)
        self.remove(dot1)

        self.add(dot2,dot2tr)
        self.add(dot3,dot3tr)
        self.add(dot4,dot4tr)
        self.add(dot5,dot5tr)
        self.add(dot6,dot6tr)
        self.add(dot7,dot7tr)
        self.add(dot8,dot8tr)
        self.add(dot9,dot9tr)
        self.play(dot2.animate.move_to(LEFT*3+UP*4),dot3.animate.move_to(LEFT*2+UP*4),dot4.animate.move_to(LEFT*2+UP*3),dot5.animate.move_to(LEFT*2+UP*2),dot6.animate.move_to(LEFT*3+UP*2),dot7.animate.move_to(LEFT*4+UP*2),dot8.animate.move_to(LEFT*4+UP*3),dot9.animate.move_to(LEFT*4+UP*4),run_time=2)
        self.remove(dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9)

        self.wait(2)
