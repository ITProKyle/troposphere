# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class EgressEndpoint(AWSProperty):
    """
    `EgressEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html>`__
    """

    props: PropsDictType = {
        "PackagingConfigurationId": (str, True),
        "Url": (str, True),
    }


class Asset(AWSObject):
    """
    `Asset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html>`__
    """

    resource_type = "AWS::MediaPackage::Asset"

    props: PropsDictType = {
        "EgressEndpoints": ([EgressEndpoint], False),
        "Id": (str, True),
        "PackagingGroupId": (str, True),
        "ResourceId": (str, False),
        "SourceArn": (str, True),
        "SourceRoleArn": (str, True),
        "Tags": (Tags, False),
    }


class IngestEndpoint(AWSProperty):
    """
    `IngestEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Password": (str, True),
        "Url": (str, True),
        "Username": (str, True),
    }


class HlsIngest(AWSProperty):
    """
    `HlsIngest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-hlsingest.html>`__
    """

    props: PropsDictType = {
        "ingestEndpoints": ([IngestEndpoint], False),
    }


class LogConfiguration(AWSProperty):
    """
    `LogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogGroupName": (str, False),
    }


class Channel(AWSObject):
    """
    `Channel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html>`__
    """

    resource_type = "AWS::MediaPackage::Channel"

    props: PropsDictType = {
        "Description": (str, False),
        "EgressAccessLogs": (LogConfiguration, False),
        "HlsIngest": (HlsIngest, False),
        "Id": (str, True),
        "IngressAccessLogs": (LogConfiguration, False),
        "Tags": (Tags, False),
    }


class Authorization(AWSProperty):
    """
    `Authorization <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html>`__
    """

    props: PropsDictType = {
        "CdnIdentifierSecret": (str, True),
        "SecretsRoleArn": (str, True),
    }


class EncryptionContractConfiguration(AWSProperty):
    """
    `EncryptionContractConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html>`__
    """

    props: PropsDictType = {
        "PresetSpeke20Audio": (str, True),
        "PresetSpeke20Video": (str, True),
    }


class OriginEndpointSpekeKeyProvider(AWSProperty):
    """
    `OriginEndpointSpekeKeyProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html>`__
    """

    props: PropsDictType = {
        "CertificateArn": (str, False),
        "EncryptionContractConfiguration": (EncryptionContractConfiguration, False),
        "ResourceId": (str, True),
        "RoleArn": (str, True),
        "SystemIds": ([str], True),
        "Url": (str, True),
    }


class OriginEndpointCmafEncryption(AWSProperty):
    """
    `OriginEndpointCmafEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html>`__
    """

    props: PropsDictType = {
        "ConstantInitializationVector": (str, False),
        "EncryptionMethod": (str, False),
        "KeyRotationIntervalSeconds": (integer, False),
        "SpekeKeyProvider": (OriginEndpointSpekeKeyProvider, True),
    }


class OriginEndpointHlsManifest(AWSProperty):
    """
    `OriginEndpointHlsManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html>`__
    """

    props: PropsDictType = {
        "AdMarkers": (str, False),
        "AdTriggers": ([str], False),
        "AdsOnDeliveryRestrictions": (str, False),
        "Id": (str, True),
        "IncludeIframeOnlyStream": (boolean, False),
        "ManifestName": (str, False),
        "PlaylistType": (str, False),
        "PlaylistWindowSeconds": (integer, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "Url": (str, False),
    }


class StreamSelection(AWSProperty):
    """
    `StreamSelection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html>`__
    """

    props: PropsDictType = {
        "MaxVideoBitsPerSecond": (integer, False),
        "MinVideoBitsPerSecond": (integer, False),
        "StreamOrder": (str, False),
    }


class OriginEndpointCmafPackage(AWSProperty):
    """
    `OriginEndpointCmafPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html>`__
    """

    props: PropsDictType = {
        "Encryption": (OriginEndpointCmafEncryption, False),
        "HlsManifests": ([OriginEndpointHlsManifest], False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentPrefix": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class SpekeKeyProvider(AWSProperty):
    """
    `SpekeKeyProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html>`__
    """

    props: PropsDictType = {
        "EncryptionContractConfiguration": (EncryptionContractConfiguration, False),
        "RoleArn": (str, True),
        "SystemIds": ([str], True),
        "Url": (str, True),
    }


class OriginEndpointDashEncryption(AWSProperty):
    """
    `OriginEndpointDashEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html>`__
    """

    props: PropsDictType = {
        "KeyRotationIntervalSeconds": (integer, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointDashPackage(AWSProperty):
    """
    `OriginEndpointDashPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html>`__
    """

    props: PropsDictType = {
        "AdTriggers": ([str], False),
        "AdsOnDeliveryRestrictions": (str, False),
        "Encryption": (OriginEndpointDashEncryption, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "ManifestLayout": (str, False),
        "ManifestWindowSeconds": (integer, False),
        "MinBufferTimeSeconds": (integer, False),
        "MinUpdatePeriodSeconds": (integer, False),
        "PeriodTriggers": ([str], False),
        "Profile": (str, False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentTemplateFormat": (str, False),
        "StreamSelection": (StreamSelection, False),
        "SuggestedPresentationDelaySeconds": (integer, False),
        "UtcTiming": (str, False),
        "UtcTimingUri": (str, False),
    }


class OriginEndpointHlsEncryption(AWSProperty):
    """
    `OriginEndpointHlsEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html>`__
    """

    props: PropsDictType = {
        "ConstantInitializationVector": (str, False),
        "EncryptionMethod": (str, False),
        "KeyRotationIntervalSeconds": (integer, False),
        "RepeatExtXKey": (boolean, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointHlsPackage(AWSProperty):
    """
    `OriginEndpointHlsPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html>`__
    """

    props: PropsDictType = {
        "AdMarkers": (str, False),
        "AdTriggers": ([str], False),
        "AdsOnDeliveryRestrictions": (str, False),
        "Encryption": (OriginEndpointHlsEncryption, False),
        "IncludeDvbSubtitles": (boolean, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "PlaylistType": (str, False),
        "PlaylistWindowSeconds": (integer, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "SegmentDurationSeconds": (integer, False),
        "StreamSelection": (StreamSelection, False),
        "UseAudioRenditionGroup": (boolean, False),
    }


class MssEncryption(AWSProperty):
    """
    `MssEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html>`__
    """

    props: PropsDictType = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointMssPackage(AWSProperty):
    """
    `OriginEndpointMssPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html>`__
    """

    props: PropsDictType = {
        "Encryption": (MssEncryption, False),
        "ManifestWindowSeconds": (integer, False),
        "SegmentDurationSeconds": (integer, False),
        "StreamSelection": (StreamSelection, False),
    }


class OriginEndpoint(AWSObject):
    """
    `OriginEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html>`__
    """

    resource_type = "AWS::MediaPackage::OriginEndpoint"

    props: PropsDictType = {
        "Authorization": (Authorization, False),
        "ChannelId": (str, True),
        "CmafPackage": (OriginEndpointCmafPackage, False),
        "DashPackage": (OriginEndpointDashPackage, False),
        "Description": (str, False),
        "HlsPackage": (OriginEndpointHlsPackage, False),
        "Id": (str, True),
        "ManifestName": (str, False),
        "MssPackage": (OriginEndpointMssPackage, False),
        "Origination": (str, False),
        "StartoverWindowSeconds": (integer, False),
        "Tags": (Tags, False),
        "TimeDelaySeconds": (integer, False),
        "Whitelist": ([str], False),
    }


class CmafEncryption(AWSProperty):
    """
    `CmafEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html>`__
    """

    props: PropsDictType = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class HlsManifest(AWSProperty):
    """
    `HlsManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html>`__
    """

    props: PropsDictType = {
        "AdMarkers": (str, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "ManifestName": (str, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "RepeatExtXKey": (boolean, False),
        "StreamSelection": (StreamSelection, False),
    }


class CmafPackage(AWSProperty):
    """
    `CmafPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html>`__
    """

    props: PropsDictType = {
        "Encryption": (CmafEncryption, False),
        "HlsManifests": ([HlsManifest], True),
        "IncludeEncoderConfigurationInSegments": (boolean, False),
        "SegmentDurationSeconds": (integer, False),
    }


class DashEncryption(AWSProperty):
    """
    `DashEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html>`__
    """

    props: PropsDictType = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class DashManifest(AWSProperty):
    """
    `DashManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html>`__
    """

    props: PropsDictType = {
        "ManifestLayout": (str, False),
        "ManifestName": (str, False),
        "MinBufferTimeSeconds": (integer, False),
        "Profile": (str, False),
        "ScteMarkersSource": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class DashPackage(AWSProperty):
    """
    `DashPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html>`__
    """

    props: PropsDictType = {
        "DashManifests": ([DashManifest], True),
        "Encryption": (DashEncryption, False),
        "IncludeEncoderConfigurationInSegments": (boolean, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "PeriodTriggers": ([str], False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentTemplateFormat": (str, False),
    }


class HlsEncryption(AWSProperty):
    """
    `HlsEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html>`__
    """

    props: PropsDictType = {
        "ConstantInitializationVector": (str, False),
        "EncryptionMethod": (str, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class HlsPackage(AWSProperty):
    """
    `HlsPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html>`__
    """

    props: PropsDictType = {
        "Encryption": (HlsEncryption, False),
        "HlsManifests": ([HlsManifest], True),
        "IncludeDvbSubtitles": (boolean, False),
        "SegmentDurationSeconds": (integer, False),
        "UseAudioRenditionGroup": (boolean, False),
    }


class MssManifest(AWSProperty):
    """
    `MssManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html>`__
    """

    props: PropsDictType = {
        "ManifestName": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class MssPackage(AWSProperty):
    """
    `MssPackage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html>`__
    """

    props: PropsDictType = {
        "Encryption": (MssEncryption, False),
        "MssManifests": ([MssManifest], True),
        "SegmentDurationSeconds": (integer, False),
    }


class PackagingConfiguration(AWSObject):
    """
    `PackagingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html>`__
    """

    resource_type = "AWS::MediaPackage::PackagingConfiguration"

    props: PropsDictType = {
        "CmafPackage": (CmafPackage, False),
        "DashPackage": (DashPackage, False),
        "HlsPackage": (HlsPackage, False),
        "Id": (str, True),
        "MssPackage": (MssPackage, False),
        "PackagingGroupId": (str, True),
        "Tags": (Tags, False),
    }


class PackagingGroup(AWSObject):
    """
    `PackagingGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html>`__
    """

    resource_type = "AWS::MediaPackage::PackagingGroup"

    props: PropsDictType = {
        "Authorization": (Authorization, False),
        "EgressAccessLogs": (LogConfiguration, False),
        "Id": (str, True),
        "Tags": (Tags, False),
    }
