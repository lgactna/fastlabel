"""
Auto-generated classes from the YAML declarations in kubernetes.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class KubernetesCertificates(GRRArtifactBase):
    """
    Certificate files that are used for a Kubernetes cluster.

    The files are typically only present on the control-plane node.

    Reference URLs:
    https://kubernetes.io/docs/setup/best-practices/certificates/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/kubernetes/admin.conf",
                    "/etc/kubernetes/controller-manager.conf",
                    "/etc/kubernetes/kubelet.conf",
                    "/etc/kubernetes/scheduler.conf",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesClusterDatabase(GRRArtifactBase):
    """
    Kubernetes cluster (etcd) database.

    The cluster database is hosted within a Pod and can be configured to be
    deployed as distributed environment or single intance. The database is
    mounted from the local file system into the corresponding containers
    scheduled by a pod.

    The database contains information about the clusters state, deployed
    resourcees and also deleted components.

    Reference URLs:
    https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
    https://github.com/etcd-io/etcd
    https://github.com/etcd-io/etcd/tree/main/tools/etcd-dump-db
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/lib/etcd/member/snap/db"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubelet(GRRArtifactBase):
    """
    Installation path of the (Kubernetes) Kubelet component.

    This component is installed on all nodes that are member of a Kubernetes
    cluster.

    Reference URLs:
    https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
    """

    SOURCES = [{"type": "PATH", "attributes": {"paths": ["/var/lib/kubelet"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletConfiguration(GRRArtifactBase):
    """
    Files that stores the configuration of the local (Kubernetes) Kubelet.

    Reference URLs:
    https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/
    https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/lib/kubelet/config.yaml",
                    "/etc/kubernetes/kubelet.conf",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletNetworkPKI(GRRArtifactBase):
    """
    Certificates and other keyfiles used for Kubelet and Kubernetes general PKI.

    Reference URLs: https://kubernetes.io/docs/setup/best-practices/certificates
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["/etc/kubernetes/pki", "/var/lib/kubelet/pki"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletPod(GRRArtifactBase):
    """
    Path of (Kubernetes) Kubelet component information about Pods scheduled to
    run on a particular node.
    """

    SOURCES = [{"type": "PATH", "attributes": {"paths": ["/var/lib/kubelet/pods"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletPodManifest(GRRArtifactBase):
    """
    Manifest file that has been used to deploy a (Kubernetes) Pod.

    The manifest contains the Pods specification.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/etc/kubernetes/manifests/*.yaml"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletPodContainer(GRRArtifactBase):
    """
    Path where the container resources created within a (Kubernetes) Pod are
    located.

    The paths naming would explain as the following:
    '/var/lib/kubelet/pods/<pod_id>/containers/<container_name>/*'

    The Pod itself gets created/scheduled by the Kubelet component. The path
    'containers/' does contain a directory for each container scheduled in that
    Pod. In each of that path there is a file located that gets mounted into the
    container at '/dev/termination-log'.

    This is the logfile that stores termination information in case a container
    terminates. The pod identifier of that file can be correlated to the
    container runtime installed on the host to find out the mount configuration.

    Reference URLs:
    https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#container-v1-core
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["/var/lib/kubelet/pods/*/containers"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletPodVolumes(GRRArtifactBase):
    """
    Volumes and other objects that are mounted into a (Kubernetes) Pod and
    respectively into the scheduled container(s).

    The type of volumes (or objects) are identified by the name appended to a
    tilde.

    Examples: * 'volumes/kubernetes.io~projected' -> describes a projected
    volume * 'volumes/kubernetes.io~configmap' -> describes a Kubernetes
    ConfigMap resource

    Reference URLs: https://kubernetes.io/docs/concepts/storage/volumes
    https://kubernetes.io/docs/concepts/storage/projected-volumes/
    https://kubernetes.io/docs/concepts/storage/volumes/#configmap
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["/var/lib/kubelet/pods/*/volumes/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesKubeletPodLogs(GRRArtifactBase):
    """
    Location where the log data of (Kubernetes) Pods can be found.

    The path's name would contain the following elements:
    '/var/log/pods/<namespace>_<pod_name>_<pod_id>/<container_name>/<num>.log'
    Includes also redirected stdout, stderr and (if applicable) stdin of
    container executions.

    Reference URLs: https://github.com/kubernetes/kubernetes/pull/74441
    https://kubernetes.io/docs/concepts/cluster-administration/logging/
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/pods/*/*/*.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KubernetesLogs(GRRArtifactBase):
    """
    Log files that contain information about the Kubernetes installation of a
    node.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/syslog*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
