import sys
import plotly.graph_objects as go


#data = str(sys.argv[1])
#print(sys.argv)
lst3 = [1,2,4]
fig = go.Figure(
    data=[go.Bar(y=lst3)],
    layout_title_text="Rami levi left \t\t\t Yenot Bitan  "
)
fig.show()