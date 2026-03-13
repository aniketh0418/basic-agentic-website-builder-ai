from langgraph.graph import StateGraph

from planner import planner
from coder import coder
from file_tools import write_files
from deploy import deploy


class AgentState(dict):
    prompt: str
    plan: str
    code: str
    files_written: bool
    deployed: bool


graph = StateGraph(AgentState)

graph.add_node("planner", planner)
graph.add_node("coder", coder)
graph.add_node("writer", write_files)
graph.add_node("deploy", deploy)

graph.set_entry_point("planner")

graph.add_edge("planner", "coder")
graph.add_edge("coder", "writer")
graph.add_edge("writer", "deploy")

app = graph.compile()


prompt = input("Enter website idea: ")

app.invoke({"prompt": prompt})