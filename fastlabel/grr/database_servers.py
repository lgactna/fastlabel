"""
Auto-generated classes from the YAML declarations in database_servers.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class ElasticsearchAccessLog(GRRArtifactBase):
    """
    Location where Elasticsearch access logs are stored.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/log/elasticsearch/*_access.log"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ElasticsearchAuditLog(GRRArtifactBase):
    """
    Location where Elasticsearch audit logs are stored.

    Reference URLs:
    https://www.elastic.co/guide/en/elasticsearch/reference/current/audit-log-output.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/elasticsearch/*_audit.json",
                    "/var/log/elasticsearch/*_audit.log",
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


class ElasticsearchGCLog(GRRArtifactBase):
    """
    Location where Elasticsearch GC logs are stored.

    Reference URLs:
    https://www.elastic.co/guide/en/elasticsearch/reference/current/important-settings.html#gc-logging
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/elasticsearch/gc.log",
                    "/var/log/elasticsearch/gc.log.[0-9]",
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


class ElasticsearchLogs(GRRArtifactBase):
    """
    Location where Elasticsearch logs are stored.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/elasticsearch/*.log",
                    "/var/log/elasticsearch/*.json",
                    "/var/log/elasticsearch/*.json.gz",
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


class ElasticsearchServerLog(GRRArtifactBase):
    """
    Location where Elasticsearch server logs are stored.

    Reference URLs:
    https://www.elastic.co/guide/en/elasticsearch/reference/current/logging.html#loggin-configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/elasticsearch/*_server.json",
                    "/var/log/elasticsearch/*-*.json",
                    "/var/log/elasticsearch/*-*.json.gz",
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


class MongoDBConfigurationFile(GRRArtifactBase):
    """
    MongoDB configuration file.

    Reference URLs:
    https://www.mongodb.com/docs/manual/reference/configuration-options/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/usr/local/etc/mongod.conf", "/opt/homebrew/etc/mongod.conf"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/mongod.conf"]},
            "supported_os": ["Linux"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MongoDBDatabasePath(GRRArtifactBase):
    """
    MongoDB database Path.

    Reference URLs:
    https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-storage.dbPath
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/usr/local/var/mongodb/*"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "PATH",
            "attributes": {
                "paths": ["/data/db/*", "/var/lib/mongo/*", "/var/lib/mongodb/*"]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["\\data\\db\\*"], "separator": "\\"},
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MongoDBLogFiles(GRRArtifactBase):
    """
    MongoDB log files.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/log/mongodb/mongod.log*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MySQLConfigurationFiles(GRRArtifactBase):
    """
    MySQL configuration files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/my.cnf", "/etc/mysql/mysql.conf.d/mysqld.cnf"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MySQLDataDictionary(GRRArtifactBase):
    """
    MySQL data dictionary.

    Reference URLs:
    https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-transactional-storage.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/lib/mysql/mysql.ibd"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MySQLDataDirectory(GRRArtifactBase):
    """
    MySQL data directory.

    Reference URLs: https://dev.mysql.com/doc/refman/8.0/en/data-directory.html
    https://dev.mysql.com/doc/refman/8.0/en/innodb-architecture.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/lib/mysql/*", "/var/lib/mysql/*/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MySQLLogFiles(GRRArtifactBase):
    """
    MySQL log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/mysql/error.log*",
                    "/var/log/mysql.log*",
                    "/var/log/*.log*",
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


class OpenSearchLogFiles(GRRArtifactBase):
    """
    OpenSearch log files.

    Reference URLs: https://opensearch.org/docs/latest/opensearch/logs/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/log/opensearch/*.log", "/var/log/opensearch/*.json"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class PostgreSQLConfigurationFiles(GRRArtifactBase):
    """
    PostgreSQL configuration files.

    Reference URLs:
    https://www.postgresql.org/docs/current/runtime-config-file-locations.html
    https://docs.fedoraproject.org/en-US/quick-docs/postgresql/
    https://wiki.debian.org/PostgreSql
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/postgresql/*/*/postgresql.conf",
                    "/etc/postgresql/*/*/pg_hba.conf",
                    "/etc/postgresql/*/*/pg_ident.conf",
                    "/var/lib/pgsql/postgresql.conf",
                    "/var/lib/pgsql/pg_hba.conf",
                    "/var/lib/pgsql/pg_ident.conf",
                    "/var/lib/pgsql/data/postgresql.conf",
                    "/var/lib/pgsql/data/pg_hba.conf",
                    "/var/lib/pgsql/data/pg_ident.conf",
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


class PostgreSQLDataDirectory(GRRArtifactBase):
    """
    PostgreSQL data directory.

    Reference URLs:
    https://www.postgresql.org/docs/current/storage-file-layout.html
    https://docs.fedoraproject.org/en-US/quick-docs/postgresql/
    https://wiki.debian.org/PostgreSql
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/lib/pgsql/data/*",
                    "/var/lib/pgsql/data-old/*",
                    "/var/lib/pgsql/*/*",
                    "/var/lib/postgresql/*/main/*/*",
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


class PostgreSQLLogFiles(GRRArtifactBase):
    """
    PostgreSQL log files.

    Reference URLs:
    https://www.postgresql.org/docs/14/runtime-config-logging.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/postgresql/postgresql.log*",
                    "/var/log/postgresql/postgresql.csv*",
                    "/var/log/postgresql/postgresql-*.log*",
                    "/var/log/postgresql/postgresql-*.csv*",
                    "/var/log/postgresql/postgresql-*-*.log*",
                    "/var/log/postgresql/postgresql-*-*.csv*",
                    "/var/lib/pgsql/data/log/postgresql.log*",
                    "/var/lib/pgsql/data/log/postgresql.csv*",
                    "/var/lib/pgsql/data/log/postgresql-*.log*",
                    "/var/lib/pgsql/data/log/postgresql-*.csv*",
                    "/var/lib/pgsql/data/log/postgresql-*-*.log*",
                    "/var/lib/pgsql/data/log/postgresql-*-*.csv*",
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


class RedisConfigurationFile(GRRArtifactBase):
    """
    Redis configuration files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/redis/*", "/etc/init.d/redis_*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class RedisDataDirectory(GRRArtifactBase):
    """
    Redis Data Directory.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/redis/*", "/var/redis/*/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class RedisLogFiles(GRRArtifactBase):
    """
    Redis log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/log/redis/redis*.log*", "/var/log/redis*.log*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
