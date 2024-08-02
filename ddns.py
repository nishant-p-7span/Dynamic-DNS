import boto3
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json().get('ip')
        return ip
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

def get_current_dns_ip(zone_id, domain_name, aws_access_key_id, aws_secret_access_key):
    client = boto3.client(
        'route53',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    try:
        response = client.list_resource_record_sets(
            HostedZoneId=zone_id,
            StartRecordName=domain_name,
            StartRecordType='A',
            MaxItems='1'
        )
        
        for record_set in response['ResourceRecordSets']:
            if record_set['Name'] == domain_name + '.' and record_set['Type'] == 'A':
                return record_set['ResourceRecords'][0]['Value']
                
        return None
    except Exception as e:
        print(f"Error getting current DNS IP: {e}")
        return None

def update_route53_record(zone_id, domain_name, public_ip, aws_access_key_id, aws_secret_access_key):
    client = boto3.client(
        'route53',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        response = client.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                'Comment': 'Update record to reflect new public IP address',
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': domain_name,
                            'Type': 'A',
                            'TTL': 300,
                            'ResourceRecords': [{'Value': public_ip}]
                        }
                    }
                ]
            }
        )
        print("DNS record updated successfully:", response)
    except Exception as e:
        print(f"Error updating DNS record: {e}")

def main():
    # Define your hosted zone ID and domain name
    zone_id = 'YOUR_HOSTED_ZONE_ID'
    domain_name = 'yourdomain.example.com'
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
    aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'

    public_ip = get_public_ip()
    if public_ip:
        current_dns_ip = get_current_dns_ip(zone_id, domain_name, aws_access_key_id, aws_secret_access_key)
        if public_ip != current_dns_ip:
            update_route53_record(zone_id, domain_name, public_ip, aws_access_key_id, aws_secret_access_key)
        else:
            print("IP address is already up to date.")
    else:
        print("Failed to get public IP address.")

if __name__ == "__main__":
    main()
