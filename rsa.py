import random

import streamlit as st 
import math
st.title("RSA Encryption idriss ")
m=st.text_input("entrer le message : ")
p=st.number_input("donner le p : ",step=1,format="%d")
q=st.number_input("donner le q : ",step=1,format="%d")
mode = st.radio("Choisir e :", ["Auto-generate e", "Enter e manually"])
tab=[]
e_input = None

if mode == "Enter e manually":
    e_input = st.number_input("Enter value of e", step=1)
def inverse(e,totient):
    for x in range(1,totient):
        if (e*x)%totient==1:
            return x
def dechiffrement(C,d,n): 
    return pow(C,d,n)

def prime(x): 
    if x<2: 
        return False 
    for i in range(2,x//2+1): 
        if x%i==0:
            return False
    return True 
def totient(p,q): 
    return (p-1)*(q-1)
def check_e(e,totient):
    if (math.gcd(e,totient)==1) and (3<e<totient):
        return True
    else:
        return False
def generation_e(totient):
    tab_e=[i for i in range(3,totient) if math.gcd(i,totient)==1]   
    return random.choice(tab_e) if tab_e else None
if prime(p) and prime(q):
    n=p*q
    tot=totient(p,q)
    if mode == "Auto-generate e":
        e=generation_e(tot)
    else:        
        e=e_input
        if not check_e(e,tot):
            st.write("e=",e,"n'est pas valide pour le totient=",tot)
            st.stop()
    cyphertext = ""
    dechiffrement_message=""
    for x in m : 
        
        C=pow(ord(x),e,n)
        cyphertext += str(hex(C)[2:]) + " "
        
        print(C)
        
        tab.append(C)
    st.write("le message chiffré est : ",cyphertext)
    d=inverse(e,tot)
    st.write("la clé de déchiffrement d=",d)
    
    if st.button("Déchiffrer"): 
        for i in range(len(tab)):
            print((dechiffrement(tab[i],d,n)))
            dechiffrement_message += chr(dechiffrement(tab[i],d,n))
        st.write("le message déchiffré est : ",dechiffrement_message) 
    
else:
    st.write("p et q doivent être des nombres premiers")    

