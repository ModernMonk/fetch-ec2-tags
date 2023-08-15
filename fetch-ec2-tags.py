import boto3

def get_tag_value(ec2_resource, private_ip, tag_key):
    instances = ec2_resource.instances.filter(Filters=[{'Name': 'private-ip-address', 'Values': [private_ip]}])
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == tag_key:
                return tag['Value']
    return None

def main():
    ec2_resource = boto3.resource('ec2')

    ips = [
        # List of IP addresses
    ]
    tag_key = input("Enter the tag key: ")

    for ip in ips:
        tag_value = get_tag_value(ec2_resource, ip, tag_key)
        if tag_value:
            print(f"IP: {ip}, {tag_key} Tag Value: {tag_value}")
        else:
            print(f"IP: {ip}, {tag_key} Tag not found")

if __name__ == "__main__":
    main()
