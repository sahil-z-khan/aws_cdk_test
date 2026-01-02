from aws_cdk import (
    Duration,
    Stack,
    aws_route53 as route53,
)
from constructs import Construct


class Route53(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        hosted_zone = self._import_hosted_zone(
            hosted_zone_id="Z1234567890ABCDEF",  # replace with your Hosted Zone ID
            zone_name="example.com",  # replace with your domain
        )
        self._create_a_record(
            hosted_zone,
            record_name="app.example.com",  # replace with your record name
            target_ip="203.0.113.10",  # replace with your target IP or swap for Alias
        )

    def _import_hosted_zone(self, hosted_zone_id: str, zone_name: str) -> route53.IHostedZone:
        return route53.HostedZone.from_hosted_zone_attributes(
            self,
            "ImportedZone",
            hosted_zone_id=hosted_zone_id,
            zone_name=zone_name,
        )

    def _create_a_record(
        self, hosted_zone: route53.IHostedZone, record_name: str, target_ip: str
    ) -> None:
        route53.ARecord(
            self,
            "AppARecord",
            zone=hosted_zone,
            record_name=record_name,
            target=route53.RecordTarget.from_ip_addresses(target_ip),
            ttl=Duration.minutes(5),
        )
