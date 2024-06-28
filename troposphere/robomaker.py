# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html>`__
    """

    resource_type = "AWS::RoboMaker::Fleet"

    props: PropsDictType = {
        "Name": (str, False),
        "Tags": (dict, False),
    }


class Robot(AWSObject):
    """
    `Robot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html>`__
    """

    resource_type = "AWS::RoboMaker::Robot"

    props: PropsDictType = {
        "Architecture": (str, True),
        "Fleet": (str, False),
        "GreengrassGroupId": (str, True),
        "Name": (str, False),
        "Tags": (dict, False),
    }


class RobotSoftwareSuite(AWSProperty):
    """
    `RobotSoftwareSuite <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Version": (str, False),
    }


class SourceConfig(AWSProperty):
    """
    `SourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html>`__
    """

    props: PropsDictType = {
        "Architecture": (str, True),
        "S3Bucket": (str, True),
        "S3Key": (str, True),
    }


class RobotApplication(AWSObject):
    """
    `RobotApplication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html>`__
    """

    resource_type = "AWS::RoboMaker::RobotApplication"

    props: PropsDictType = {
        "CurrentRevisionId": (str, False),
        "Environment": (str, False),
        "Name": (str, False),
        "RobotSoftwareSuite": (RobotSoftwareSuite, True),
        "Sources": ([SourceConfig], False),
        "Tags": (dict, False),
    }


class RobotApplicationVersion(AWSObject):
    """
    `RobotApplicationVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html>`__
    """

    resource_type = "AWS::RoboMaker::RobotApplicationVersion"

    props: PropsDictType = {
        "Application": (str, True),
        "CurrentRevisionId": (str, False),
    }


class RenderingEngine(AWSProperty):
    """
    `RenderingEngine <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Version": (str, True),
    }


class SimulationSoftwareSuite(AWSProperty):
    """
    `SimulationSoftwareSuite <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Version": (str, False),
    }


class SimulationApplication(AWSObject):
    """
    `SimulationApplication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html>`__
    """

    resource_type = "AWS::RoboMaker::SimulationApplication"

    props: PropsDictType = {
        "CurrentRevisionId": (str, False),
        "Environment": (str, False),
        "Name": (str, False),
        "RenderingEngine": (RenderingEngine, False),
        "RobotSoftwareSuite": (RobotSoftwareSuite, True),
        "SimulationSoftwareSuite": (SimulationSoftwareSuite, True),
        "Sources": ([SourceConfig], False),
        "Tags": (dict, False),
    }


class SimulationApplicationVersion(AWSObject):
    """
    `SimulationApplicationVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html>`__
    """

    resource_type = "AWS::RoboMaker::SimulationApplicationVersion"

    props: PropsDictType = {
        "Application": (str, True),
        "CurrentRevisionId": (str, False),
    }
