"""Main entry point for the multi-agent content generation system."""

import json
from pathlib import Path
from orchestrator.pipeline_orchestrator import PipelineOrchestrator


def main():
    """Execute the multi-agent content generation pipeline."""
    # Load product data
    data_path = Path("data/product_data.json")
    with open(data_path, 'r', encoding='utf-8') as f:
        product_data = json.load(f)
    
    # Initialize orchestrator
    orchestrator = PipelineOrchestrator()
    
    # Execute pipeline
    print("Starting multi-agent content generation pipeline...")
    output_files = orchestrator.execute(product_data)
    
    # Print results
    print("\nPipeline execution completed successfully!")
    print("\nGenerated output files:")
    for page_type, file_path in output_files.items():
        print(f"  - {page_type}: {file_path}")
    
    print("\nExecution flow:")
    flow = orchestrator.get_execution_flow()
    for step in flow["pipeline_steps"]:
        agent_name = step.get("agent") or step.get("agents") or step.get("action")
        print(f"  Step {step['step']}: {agent_name}")


if __name__ == "__main__":
    main()

