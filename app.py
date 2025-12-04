import streamlit as st
import os
from adk.client import Client
from agents.client_agent import ClientAgent # يجب أن يكون هذا الاستيراد صحيحاً بعد إصلاح Git

# يجب توفير مفتاح Gemini API
if "GEMINI_API_KEY" not in os.environ:
    st.error("⚠️ يرجى تعيين متغير بيئة GEMINI_API_KEY لتشغيل التطبيق.")
    st.stop()

# 1. تهيئة العميل (Client) والوكيل (Agent)
agent_client = Client(ClientAgent, gemini_api_key=os.environ["GEMINI_API_KEY"])

st.set_page_config(page_title="🤖 مطعم ADK", layout="wide")
st.title("مطعم ADK الذكي 🍔")
st.caption("يعمل هذا التطبيق بوكيل ADK مباشرة على Streamlit Cloud.")

user_input = st.text_input("أدخل طلبك هنا، مثال: أريد طلب برجر وبيتزا", key="user_input")

if st.button("أرسل الطلب"):
    if user_input:
        st.info(f"إرسال الطلب: {user_input}")
        
        try:
            # تشغيل الوكيل مباشرة عبر كود بايثون
            response = agent_client.run(user_input)
            
            st.success("✅ استجابة الوكيل:")
            # افتراض أن الاستجابة تحتوي على مفتاح 'output'
            st.markdown(f"**{response.output}**") 

        except Exception as e:
            st.error(f"❌ خطأ في تشغيل الوكيل: {e}")