from langgraph.graph import StateGraph, END

from app.state.movie_state import MovieState


workflow = StateGraph(MovieState)