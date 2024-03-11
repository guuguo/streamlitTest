import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 设置页面标题和图标
st.set_page_config(page_title="表白箫箫", page_icon=":heart:")

# 添加标题和表白的话
st.title("亲爱的箫箫")
st.header("我是郭德清")
st.subheader("我想对你说：")
st.markdown("""
    :rose: :rose: :rose:  
    **你是我生命中的一道光，照亮了我前行的道路。**  
    **在这个特别的日子里，我想告诉你，我喜欢你，箫箫。**  
    **愿意和我一起走吗？**  
    :rose: :rose: :rose:  
""")

# 添加一些花里胡哨的效果
# 显示一张图片
response = requests.get("https://source.unsplash.com/featured/?heart")
image = Image.open(BytesIO(response.content))
st.image(image, caption="爱在心中", use_column_width=True)

# 添加一个按钮，当点击时显示更多的爱意
if st.button("点击这里"):
    st.balloons()
    st.success("箫箫，我会用我的全部去爱你和守护你！")

# 运行这个应用程序，你需要将这段代码保存为一个`.py`文件
# 然后使用命令行运行`streamlit run your_script.py`