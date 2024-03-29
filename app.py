import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
st.set_option('deprecation.showfileUploaderEncoding', False)
def find_associatio_rule(support):
  # Load the pickled model
  model = pickle.load(open('/content/drive/My Drive/aprioriexample.pkl','rb'))     
  if uploaded_file is not None:
    dataset= pd.read_csv(uploaded_file)
  else:
    dataset= pd.read_csv('/content/drive/My Drive/retail_dataset.csv')

  #Create list 
  transactions = []
  for i in range(0, 9835):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 33)])

  from mlxtend.preprocessing import TransactionEncoder
  te = TransactionEncoder()
  te_ary = te.fit(transactions).transform(transactions)
  df = pd.DataFrame(te_ary, columns=te.columns_)
  df=df[['citrus fruit',
  'other vegetables',
  'whole milk',
  'dessert',
  'yogurt',
  'frozen vegetables',
  'fruit/vegetable juice',
  'bottled beer',
  'salty snack',
  'curd',
  'yogurt',
  'spread cheese',
  'sugar',
  'canned vegetables',
  'beef',
  'UHT-milk',
  'salt',
  'soda',
  'specialty chocolate',
  'shopping bags']]
  freq_items = apriori(df, min_support=support, use_colnames=True)
  rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
  return rules
def find_frequent_items(support):
  # Load the pickled model
  model = pickle.load(open('apriori.pkl','rb'))     
  if uploaded_file is not None:
    dataset= pd.read_csv(uploaded_file)
  else:
    dataset= pd.read_csv('Apriori2 dataset.csv')
  #Create list 
  transactions = []
  for i in range(0, 9835):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 33)])

  from mlxtend.preprocessing import TransactionEncoder
  te = TransactionEncoder()
  te_ary = te.fit(transactions).transform(transactions)
  df = pd.DataFrame(te_ary, columns=te.columns_)
  df=df[['citrus fruit',
  'other vegetables',
  'whole milk',
  'dessert',
  'yogurt',
  'frozen vegetables',
  'fruit/vegetable juice',
  'bottled beer',
  'salty snack',
  'curd',
  'yogurt',
  'spread cheese',
  'sugar',
  'canned vegetables',
  'beef',
  'UHT-milk',
  'salt',
  'soda',
  'specialty chocolate',
  'shopping bags']]
  freq_items = apriori(df, min_support=support, use_colnames=True)
  rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
  
  return freq_items
html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">endterm Practical</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
st.header("Identification of items frequently purchased together ")
  
uploaded_file = st.file_uploader("Upload dataset", help='Please upload retail_dataset.csv otherwise leave  blank') 
support = st.number_input('Insert a minimum suppport to find association rule ',0,1)


  
if st.button("Association Rule"):
  rules=find_associatio_rule(support)
  st.success('Apriori found Following rules {}'.format(rules))
if st.button("Frequent Items"):
  frequent_items=find_frequent_items(support)
  st.success('Apriori found Frequent itemsets {}'.format(frequent_items))      
if st.button("About"):
  st.subheader("Developed by Divyam Sharma")
  st.subheader("PIET18CS050")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Machine learning Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)