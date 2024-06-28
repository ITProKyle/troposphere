# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer


class Definition(AWSProperty):
    """
    `Definition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html>`__
    """

    props: PropsDictType = {
        "Content": (str, False),
        "S3Location": (str, False),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html>`__
    """

    resource_type = "AWS::M2::Application"

    props: PropsDictType = {
        "Definition": (Definition, True),
        "Description": (str, False),
        "EngineType": (str, True),
        "KmsKeyId": (str, False),
        "Name": (str, True),
        "RoleArn": (str, False),
        "Tags": (dict, False),
    }


class HighAvailabilityConfig(AWSProperty):
    """
    `HighAvailabilityConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html>`__
    """

    props: PropsDictType = {
        "DesiredCapacity": (integer, True),
    }


class EfsStorageConfiguration(AWSProperty):
    """
    `EfsStorageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html>`__
    """

    props: PropsDictType = {
        "FileSystemId": (str, True),
        "MountPoint": (str, True),
    }


class FsxStorageConfiguration(AWSProperty):
    """
    `FsxStorageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html>`__
    """

    props: PropsDictType = {
        "FileSystemId": (str, True),
        "MountPoint": (str, True),
    }


class StorageConfiguration(AWSProperty):
    """
    `StorageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html>`__
    """

    props: PropsDictType = {
        "Efs": (EfsStorageConfiguration, False),
        "Fsx": (FsxStorageConfiguration, False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html>`__
    """

    resource_type = "AWS::M2::Environment"

    props: PropsDictType = {
        "Description": (str, False),
        "EngineType": (str, True),
        "EngineVersion": (str, False),
        "HighAvailabilityConfig": (HighAvailabilityConfig, False),
        "InstanceType": (str, True),
        "KmsKeyId": (str, False),
        "Name": (str, True),
        "PreferredMaintenanceWindow": (str, False),
        "PubliclyAccessible": (boolean, False),
        "SecurityGroupIds": ([str], False),
        "StorageConfigurations": ([StorageConfiguration], False),
        "SubnetIds": ([str], False),
        "Tags": (dict, False),
    }
