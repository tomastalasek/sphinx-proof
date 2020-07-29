from pathlib import Path
from typing import Any, Dict
from sphinx.application import Sphinx
from .proof import ProofDomain, proof_node, visit_proof_node, depart_proof_node

def setup(app: Sphinx) -> Dict[str, Any]:

	static_path = Path(__file__).parent.parent.parent.joinpath('_static').absolute()
	app.config.html_static_path.append(str(static_path))
	app.config.html_css_files.append('proof.css')

	app.add_node(proof_node, html=(visit_proof_node, depart_proof_node))
	app.add_domain(ProofDomain)

	return {
		"version": "builtin",
		"parallel_read_safe": True,
		"parallel_write_safe": True,
	}
