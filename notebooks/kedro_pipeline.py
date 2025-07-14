from package_name.pipeline_registry import register_pipelines  
pipelines = register_pipelines()
for pipeline, nodes in pipelines.items():                
    print(f"All nodes in {pipeline}:")
    for node in nodes.nodes:
        print(f" • {node.name!r} — inputs={node.inputs}, outputs={node.outputs}")
