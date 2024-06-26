
import streamlit as st
import random

def numbers3_simulator_customize(num1,num2,num3):
    numbers3=random.sample(range(0,10),3)
    your_numbers=[num1,num2,num3]
    straight=[]
    mini=[]
    #ストレート判定
    for n,y in zip(numbers3,your_numbers):
        if n==y:
            straight.append(n)
        if len(straight)>=0:
            mini.append(n)
    #ボックス判定
    box=set(numbers3) & set(your_numbers)
    #ミニ判定
    mini_result="ミニ当選" if len(mini)==2 else "該当なし"
    print("NUMBERS3抽選結果（改良版）")
    print("当たり番号：",numbers3)
    print("あなたの番号：",your_numbers)
    print("ストレート",straight)
    print("ボックス",list(box))
    print("ミニ：",mini_result)
    print("----------------------------")
    return numbers3,your_numbers,straight,box,mini_result

st.title("NUMBERS3シミュレーター")
with st.form(key="numbers3"):
  st.write("以下の入力欄に０～９までの整数それぞれに入力してください")
  col_1,col_2,col_3=st.columns(3)
  with col_1:
      num1=st.number_input("数字１",value=1,min_value=1,max_value=43,step=1)
  with col_2:
      num2=st.number_input("数字２",value=1,min_value=1,max_value=43,step=1)
  with col_3:
      num3=st.number_input("数字３",value=1,min_value=1,max_value=43,step=1)
  submit_btn=st.form_submit_button("抽選する")

if submit_btn:
  numbers3,your_numbers,straight,box,mini_result=numbers3_simulator_customize(num1,num2,num3)
  st.write(f"当たり番号は{numbers3}です")
  st.write(f"あなたの番号は{your_numbers}です")
  if straight:
      st.write(f"ストレート一致した番号：{straight}")
  if box:
      st.write(f"ボックス一致した番号：{box}")
  st.write("三二：",mini_result)