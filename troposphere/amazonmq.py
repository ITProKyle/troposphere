# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.amazonmq import validate_tags_or_list


class ConfigurationId(AWSProperty):
    """
    `ConfigurationId <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Revision": (integer, True),
    }


class EncryptionOptions(AWSProperty):
    """
    `EncryptionOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "UseAwsOwnedKey": (boolean, True),
    }


class LdapServerMetadata(AWSProperty):
    """
    `LdapServerMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html>`__
    """

    props: PropsDictType = {
        "Hosts": ([str], True),
        "RoleBase": (str, True),
        "RoleName": (str, False),
        "RoleSearchMatching": (str, True),
        "RoleSearchSubtree": (boolean, False),
        "ServiceAccountPassword": (str, True),
        "ServiceAccountUsername": (str, True),
        "UserBase": (str, True),
        "UserRoleName": (str, False),
        "UserSearchMatching": (str, True),
        "UserSearchSubtree": (boolean, False),
    }


class LogsConfiguration(AWSProperty):
    """
    `LogsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html>`__
    """

    props: PropsDictType = {
        "Audit": (boolean, False),
        "General": (boolean, False),
    }


class MaintenanceWindow(AWSProperty):
    """
    `MaintenanceWindow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html>`__
    """

    props: PropsDictType = {
        "DayOfWeek": (str, True),
        "TimeOfDay": (str, True),
        "TimeZone": (str, True),
    }


class User(AWSProperty):
    """
    `User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html>`__
    """

    props: PropsDictType = {
        "ConsoleAccess": (boolean, False),
        "Groups": ([str], False),
        "Password": (str, True),
        "Username": (str, True),
    }


class Broker(AWSObject):
    """
    `Broker <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html>`__
    """

    resource_type = "AWS::AmazonMQ::Broker"

    props: PropsDictType = {
        "AuthenticationStrategy": (str, False),
        "AutoMinorVersionUpgrade": (boolean, True),
        "BrokerName": (str, True),
        "Configuration": (ConfigurationId, False),
        "DataReplicationMode": (str, False),
        "DataReplicationPrimaryBrokerArn": (str, False),
        "DeploymentMode": (str, True),
        "EncryptionOptions": (EncryptionOptions, False),
        "EngineType": (str, True),
        "EngineVersion": (str, True),
        "HostInstanceType": (str, True),
        "LdapServerMetadata": (LdapServerMetadata, False),
        "Logs": (LogsConfiguration, False),
        "MaintenanceWindowStartTime": (MaintenanceWindow, False),
        "PubliclyAccessible": (boolean, True),
        "SecurityGroups": ([str], False),
        "StorageType": (str, False),
        "SubnetIds": ([str], False),
        "Tags": (validate_tags_or_list, False),
        "Users": ([User], True),
    }


class Configuration(AWSObject):
    """
    `Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html>`__
    """

    resource_type = "AWS::AmazonMQ::Configuration"

    props: PropsDictType = {
        "AuthenticationStrategy": (str, False),
        "Data": (str, True),
        "Description": (str, False),
        "EngineType": (str, True),
        "EngineVersion": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class ConfigurationAssociation(AWSObject):
    """
    `ConfigurationAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html>`__
    """

    resource_type = "AWS::AmazonMQ::ConfigurationAssociation"

    props: PropsDictType = {
        "Broker": (str, True),
        "Configuration": (ConfigurationId, True),
    }
