from ..core import ModelState
from .diagrams import GraphMachine
from .diagrams_base import BaseGraph, GraphProtocol
from logging import Logger
from typing import Type, Optional, Dict, List, Union, DefaultDict, Any, BinaryIO, Set

_LOGGER: Logger

class Graph(BaseGraph):
    custom_styles: Dict[str, DefaultDict[str, Union[str, DefaultDict[str, str]]]]
    def __init__(self, machine: Type[GraphMachine]) -> None: ...
    def set_previous_transition(self, src: str, dst: str) -> None: ...
    def set_node_style(self, state: ModelState, style: str) -> None: ...
    def reset_styling(self) -> None: ...
    def _add_nodes(self, states: List[Dict[str, str]],
                   container: List[str]) -> None: ...
    def _add_edges(self, transitions: List[Dict[str, str]],
                   container: List[str]) -> None: ...
    def generate(self) -> None: ...
    def get_graph(self, title: Optional[str] = ...,
                  roi_state: Optional[str] = ...) -> DigraphMock: ...

class NestedGraph(Graph):
    _cluster_states: List[str]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_previous_transition(self, src: str, dst: str) -> None: ...
    def _add_nodes(self, states: List[Dict[str, str]],
                   container: List[str]) -> None: ...
    def _add_nested_nodes(self,
                          states: List[Dict[str, Union[str, List[Dict[str, str]]]]],
                          container: List[str],
                          prefix: str, default_style: str) -> None: ...
    def _add_edges(self, transitions: List[Dict[str, str]],
                   container: List[str]) -> None: ...
    def _create_edge_attr(self, src: str, dst: str, transition: Dict[str, str]) -> Dict[str, Any]: ...


class DigraphMock(GraphProtocol):

    source: str

    def __init__(self, source: str) -> None: ...

    def draw(self, filename: Optional[Union[str, BinaryIO]], format:Optional[str] = ...,
             prog: Optional[str] = ..., args:str = ...) -> Optional[str]: ...

invalid = Set[str]
convertible = Dict[str, str]

def _to_css(style_attrs: Dict[str, str]) -> str: ...
