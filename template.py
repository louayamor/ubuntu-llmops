from pathlib import Path

PROJECT_NAME = "ubuntu-llmops"

DIRS = [
    "agents",
    "chains",
    "graphs",
    "pipelines",
    "inference",
    "models/ollama",
    "models/weights",
    "prompts",
    "data/snapshots",
    "data/aggregates",
    "eval",
    "cli",
    "config",
    "docker",
    "scripts",
    "tests",
    "logs"
]

FILES = {
    "agents/__init__.py": "",
    "agents/report_router.py": "",
    "agents/incident_agent.py": "",

    "chains/__init__.py": "",
    "chains/health_report_chain.py": "",
    "chains/memory_analysis_chain.py": "",

    "graphs/__init__.py": "",
    "graphs/report_graph.py": "",

    "pipelines/__init__.py": "",
    "pipelines/collect_snapshot.py": "",
    "pipelines/normalize_metrics.py": "",
    "pipelines/generate_report.py": "",

    "inference/__init__.py": "",
    "inference/base_client.py": "",
    "inference/ollama_client.py": "",

    "models/ollama/modelfile": "",
    "models/ollama/metadata.yaml": "",
    "models/registry.yaml": "",

    "prompts/health_report_v1.yaml": "",
    "prompts/memory_analysis_v1.yaml": "",

    "eval/metric_consistency.py": "",
    "eval/hallucination_guard.py": "",

    "cli/main.py": "",

    "config/settings.yaml": "",

    "docker/Dockerfile": "",
    "docker/docker-compose.yml": "",

    ".env.example": "",
    ".gitignore": "__pycache__/\n.env\nlogs/\ndata/\nmodels/weights/\n",

    "README.md": "# ubuntu-llmops\n\nLLM-powered Ubuntu system reporting agent.\n"
}

def create_project_structure(base_path: Path):
    for dir_path in DIRS:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)

    for file_path, content in FILES.items():
        path = base_path / file_path
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

if __name__ == "__main__":
    root = Path(PROJECT_NAME)
    root.mkdir(exist_ok=True)
    create_project_structure(root)
