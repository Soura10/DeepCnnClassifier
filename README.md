# DeepClassifier

## Workflow

1.  Update config.yaml
2.  Update secrets.yaml [Optional]
3.  Update params.yaml
4.  Update the entity in src
5.  Update Configuration manager in src config
6.  Update the components
7.  Update the pipeline
8.  Test run pipeline stage
9.  Run tox for testing the package
10. Update dvc.yaml (in place of main.py here in this project we use dvc)
11. run "dvc repro" for running all the stages in pipeline (i.e. run dvc reproduce command)

 

![img](https://raw.githubusercontent.com/Soura10/DeepCnnClassifier/main/docs/images/Data%20Ingestion%402x.png)
