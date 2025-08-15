import pulumi
import pulumi_digitalocean as do

cluster = do.KubernetesCluster(
    "devops-interview-sample-k8s-cluster",
    node_pool=do.KubernetesClusterNodePoolArgs(
        name="default-pool",
        size="s-1vcpu-2gb",
        auto_scale=False,
        node_count=1,
    ),
    region=do.Region.NYC1,
    version="1.33.1-do.3",
    name="devops-interview-sample",
)

pulumi.export("kubeconfig", cluster.kube_configs)
