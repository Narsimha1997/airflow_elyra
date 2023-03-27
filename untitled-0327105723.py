from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-0327105723",
}

dag = DAG(
    "untitled-0327105723",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.3 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: work/test.py

op_1ab8f370_f356_4d0f_a05e_ef8939ef2a1b = KubernetesPodOperator(
    name="test",
    namespace="default",
    image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.3/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.3/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.3/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.3/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled' --cos-endpoint http://10.21.34.197:9000/browser/narsimha-elyra/ --cos-bucket narsimha-elyra --cos-directory 'untitled-0327105723' --cos-dependencies-archive 'test-1ab8f370-f356-4d0f-a05e-ef8939ef2a1b.tar.gz' --file 'work/test.py' "
    ],
    task_id="test",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "narsimha-key",
        "AWS_SECRET_ACCESS_KEY": "Taashee@1997",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
