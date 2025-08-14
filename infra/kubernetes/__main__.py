from pulumi_kubernetes.kustomize import Directory

bootstrap = Directory("bootstrap-dir", directory="../../deploy/bootstrap")
