
import streamlit as st
import random

def LOTO6_simulator(num1,num2,num3,num4,num5,num6): 
  LOTO6=random.sample(range(1,44),6) #ランダムに6個の整数を生成
  your_numbers=[num1,num2,num3,num4,num5,num6] #購入者の番号用の枠
  hit_numbers=[] #一致した番号を格納する枠
  for i in LOTO6:
    for j in your_numbers:
      if i==j:
        hit_numbers.append(i)
      else:
        pass
  print("LOTO6抽選結果")
  print("当たり番号：",LOTO6)
  print("あなたの番号：",your_numbers)
  print("ヒットした番号：",hit_numbers)
  print("----------------------------")
  return LOTO6, your_numbers, hit_numbers

st.title("LOTO6シミュレーター")
with st.form(key="loto_num"):
  st.write("以下の入力欄に１～４３までの整数それぞれに入力してください")
  col_1,col_2,col_3,col_4,col_5,col_6=st.columns(6)
  with col_1:
      num1=st.number_input("数字１",value=1,min_value=1,max_value=43,step=1)
  with col_2:
      num2=st.number_input("数字２",value=1,min_value=1,max_value=43,step=1)
  with col_3:
      num3=st.number_input("数字３",value=1,min_value=1,max_value=43,step=1)
  with col_4:
      num4=st.number_input("数字４",value=1,min_value=1,max_value=43,step=1)
  with col_5:
      num5=st.number_input("数字５",value=1,min_value=1,max_value=43,step=1)
  with col_6:
      num6=st.number_input("数字６",value=1,min_value=1,max_value=43,step=1)
  submit_btn=st.form_submit_button("抽選する")

if submit_btn:
  LOTO6,your_numbers,hit_numbers=LOTO6_simulator(num1,num2,num3,num4,num5,num6)
  st.write(f"当たり番号は{LOTO6}です")
  st.write(f"あなたの番号は{your_numbers}です")
  if hit_numbers:
      st.write(f"一致した番号は{hit_numbers}です")
  else:
      st.write(f"一致した番号はありません")