from manim import *
from pathlib import Path
import os

FLAGS = f"-pql"
SCENE = "MyScene"

if __name__ == '__main__':
  script_name=f"{Path(__file__).resolve()}"
  os.system(f"manim {script_name} {SCENE} {FLAGS}")



class MyScene(Scene):
  def construct(self):
    sq1=Polygon(
      np.array([-5,2,0]),
      np.array([-5,-2,0]),
      np.array([-1,-2,0]),
      np.array([-1,2,0])

    )
    sq2=Polygon(
      np.array([-4,2,0]),
      np.array([-5,-1,0]),
      np.array([-2,-2,0]),
      np.array([-1,1,0]),
      color=ORANGE
    ).set_fill(ORANGE,opacity=0.5)
    trig2=Polygon(
      np.array([-5,-2,0]),
      np.array([-2,-2,0]),
      np.array([-5,-1,0]),
      color=YELLOW
    ).set_fill(YELLOW,opacity=0.5)
    trig3=Polygon(
      np.array([-2,-2,0]),
      np.array([-1,-2,0]),
      np.array([-1,1,0]),
      color=YELLOW
    ).set_fill(YELLOW,opacity=0.5)
    trig1=Polygon(
      np.array([-5,2,0]),
      np.array([-4,2,0]),
      np.array([-5,-1,0]),
      color=YELLOW
    ).set_fill(YELLOW,opacity=0.5)
    trig4=Polygon(
      np.array([-1,1,0]),
      np.array([-1,2,0]),
      np.array([-4,2,0]),
      color=YELLOW
    ).set_fill(YELLOW,opacity=0.5)

    sq3=Polygon(
      np.array([2,2,0]),
      np.array([2,-1,0]),
      np.array([5,-1,0]),
      np.array([5,2,0]),
      color=ORANGE

    ).set_fill(ORANGE,opacity=0.5)
    sq4=Polygon(
      np.array([1,-1,0]),
      np.array([1,-2,0]),
      np.array([2,-2,0]),
      np.array([2,-1,0]),
      color=ORANGE

    ).set_fill(ORANGE,opacity=0.5)

    text1=MathTex(r"c^2").move_to(sq2.get_center())
    
    text2=MathTex(r"a^2").move_to(sq3.get_center())

    text3=MathTex(r"b^2").move_to(sq4.get_center())

    text4=MathTex(r"c^2=a^2+b^2").to_edge(DOWN).scale(2)

    text5=MathTex(r"Pythagorean\ Theorem").to_edge(DOWN).scale(2)




    #elf.add(sq1,trig1,trig2,trig3,trig4)
    self.play(Create(sq1),run_time=3)
    self.play(DrawBorderThenFill(trig1),DrawBorderThenFill(trig2),DrawBorderThenFill(trig3),DrawBorderThenFill(trig4),run_time=2)




    self.play(sq1.copy().animate.shift(RIGHT*6))
    self.play(trig1.copy().animate.shift(RIGHT*6),trig3.copy().animate.shift(RIGHT*3,UP),trig2.copy().animate.shift(RIGHT*7),trig4.copy().animate.shift(RIGHT*6,DOWN*3))

    self.play(Create(sq2),Create(sq3),Create(sq4),run_time=3)


    self.play(Write(text1),Write(text2),Write(text3),run_time=2)
    self.play(Write(text4),run_time=2)
    self.wait()
    self.play(Transform(text4,text5))
    self.wait(2)
